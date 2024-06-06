import json
import time
import traceback
from decimal import Decimal

from common.AssertClass import assert_value
from common.casemethod import CaseMethods
from common.exesql import ExeSql
from common.jsontools import reponse
from common.player import Player
from common.request_case import Api
from error_message import MessageEnum
from app.models import *
from common.log import logger


class ExecuteHandler(object):

    def __init__(self, case_id, env_id):
        self.case_id = case_id
        self.env_id = env_id
        self.is_single = False
        self.is_dbf = False

    def dbfconf(self, case_id=None):
        if not case_id:
            case_id = self.case_id
        case = InterfaceCase.query.filter_by(case_id=case_id).first()
        if not case.rely_dbf:
            self.is_dbf = False
            return "No dbf"
        else:
            self.is_dbf = True
            return case.rely_dbf

    def exepredbf(self, dbf_id):
        dbfac = DataFactory.query.filter_by(id=dbf_id).first()
        if not dbfac:
            return reponse(code=MessageEnum.dbfac_search_error.value[0],
                           message=MessageEnum.dbfac_search_error.value[1])

        dbinf = dbfac.dbconf
        logger.info(dbinf.to_json())

        env_mapping = {
            0: ('url', 'username', 'password'),
            1: ('test_url', 'test_username', 'test_password'),
            2: ('dev_url', 'dev_username', 'dev_password'),
            3: ('stg_url', 'stg_username', 'stg_password'),
            4: ('prod_url', 'prod_username', 'prod_password')
        }

        env_key = env_mapping.get(dbfac.sql_run_dev)
        if not env_key:
            return reponse(code=MessageEnum.test_sql_query_error.value[0],
                           message=MessageEnum.test_sql_query_error.value[1])

        sqlurl = getattr(dbinf, env_key[0])
        sqlusername = getattr(dbinf, env_key[1])
        sqlpassword = getattr(dbinf, env_key[2])

        toexecsqls = dbfac.sql_str.split(';') if ';' in dbfac.sql_str else [dbfac.sql_str]

        linkurl = f"mysql+pymysql://{sqlusername}:{sqlpassword}@{sqlurl}"
        exesql = ExeSql(linkurl)
        results = []

        try:
            for sql in toexecsqls:
                if sql.strip():
                    result = exesql.exe_sql(sql.strip())
                    results.append({'sql': sql.strip(), 'result': result})
            logger.info('执行结果是: {}'.format(results))
            return '执行成功'
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.test_sql_query_error.value[0],
                           message=MessageEnum.test_sql_query_error.value[1])

    def execute_task_http(self, case_id=None, env_id=None, task_id=None):
        try:
            start_time = time.time()
            if not case_id:
                case_id = self.case_id
            if not env_id:
                env_id = self.env_id

            rely_dbf_id = InterfaceCase.query.filter_by(case_id=case_id).first().rely_dbf
            if rely_dbf_id and rely_dbf_id != 0:
                dbfresult = self.exepredbf(dbf_id=rely_dbf_id)
                logger.info(dbfresult)

            parameterdic = self.assemble_parameters(case_id=case_id, env_id=env_id)
            if not parameterdic:
                return '{"result": "组装参数失败"}', None

            if parameterdic['protocol'] == 0:
                api = Api(
                    url=parameterdic['case_url'],
                    method=parameterdic['case_method'],
                    params=parameterdic['case_params'],
                    headers=parameterdic['case_headers']
                )
                apijson = api.getJson()
                end_time = time.time()
                spend = str("{:.2f}".format(end_time - start_time))
                if apijson == '请求出错了':
                    self.save_case_result(apijson, case_id, ispass=False, testevir=env_id, spend=spend)
                    return '{"result": "请求出错了"}', None
                res = self.judgecase(apijson, case_id)[0]
                if res is True:
                    self.save_taskcase_result(apijson, case_id, ispass=True, testevir=env_id, spend=spend,
                                              task_id=task_id)
                    return '{"result": "断言通过"}', apijson
                else:
                    self.save_taskcase_result(apijson, case_id, ispass=False, testevir=env_id, spend=spend,
                                              task_id=task_id)
                    return '{"result": "断言失败"}', apijson

            elif parameterdic['protocol'] == 1:
                # 处理其他协议的情况
                pass
            else:
                return '{"result": "协议错误"}', None

        except Exception as e:
            logger.exception(e)
            return '{"result": "执行过程中发生异常"}', None

    def save_taskcase_result(self, result, caseid, ispass, testevir, spend=None, task_id=None):
        new_case = TestcaseResult(result=str(result),
                                  case_id=caseid,
                                  ispass=ispass, testevent_id=testevir, spend=spend, date=datetime.now(),
                                  task_id=task_id)
        db.session.add(new_case)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.info('用例：%s保存测试结果失败!原因：%s' % (caseid, e))

    def exesinglecase(self, case_id=None, env_id=None):
        try:
            start_time = time.time()
            if not case_id:
                case_id = self.case_id
            if not env_id:
                env_id = self.env_id

            rely_dbf_id = InterfaceCase.query.filter_by(case_id=case_id).first().rely_dbf
            if rely_dbf_id and rely_dbf_id != 0:
                dbfresult = self.exepredbf(dbf_id=rely_dbf_id)
                logger.info(dbfresult)

            parameterdic = self.assemble_parameters(case_id=case_id, env_id=env_id)
            if not parameterdic:
                return '{"result": "组装参数失败"}', None
            logger.info('parameterdic is :{}', parameterdic)

            if parameterdic['protocol'] == 0:
                api = Api(
                    url=parameterdic['case_url'],
                    method=parameterdic['case_method'],
                    params=parameterdic['case_params'],
                    headers=parameterdic['case_headers']
                )
                apijson = api.getJson()
                end_time = time.time()
                spend = str("{:.2f}".format(end_time - start_time))
                if apijson == '请求出错了':
                    self.save_case_result(apijson, case_id, ispass=False, testevir=env_id, spend=spend)
                    return '{"result": "请求出错了"}', None
                res = self.judgecase(apijson, case_id)[0]
                if res is True:
                    self.save_case_result(apijson, case_id, ispass=True, testevir=env_id, spend=spend)
                    return json.dumps({'result': "断言通过", 'response': apijson}), apijson
                else:
                    self.save_case_result(apijson, case_id, ispass=False, testevir=env_id, spend=spend)
                    return json.dumps({'result': "断言失败", 'response': apijson}), apijson

            elif parameterdic['protocol'] == 1:
                # 处理其他协议的情况
                pass

            else:
                return '{"result": "协议错误"}', None

        except Exception as e:
            logger.exception(e)
            return '{"result": "执行过程中发生异常"}', None

    def exemulticase(self, case_id=None, env_id=None):
        try:
            if not case_id:
                case_id = self.case_id
            if not env_id:
                env_id = self.env_id

            # 执行前置用例
            precasesinfos = self.execute_precases(case_id, env_id)
            logger.info(precasesinfos)
            if not precasesinfos:
                return '{"result": "前置用例执行失败"}', None

            rely_dbf_id = InterfaceCase.query.filter_by(case_id=case_id).first().rely_dbf
            if rely_dbf_id and rely_dbf_id != 0:
                dbfresult = self.exepredbf(dbf_id=rely_dbf_id)
                logger.info(dbfresult)

            # 组装请求参数
            parameterdic = self.assemble_parameters(case_id, env_id)
            if not parameterdic:
                return '{"result": "组装参数失败"}', None

            # 替换参数
            self.replace_parameters(precasesinfos, parameterdic)

            # 发送请求并进行断言
            result, apijson, spend = self.send_request_and_assert(parameterdic, case_id, env_id)
            self.save_case_result(apijson, case_id, ispass=result, testevir=env_id, spend=spend)

            if result:
                return json.dumps({'result': "断言通过", 'response': apijson}), apijson
            else:
                return json.dumps({'result': "断言失败", 'response': apijson}), apijson

        except Exception as e:
            logger.exception(e)
            return '{"result": "执行过程中发生异常"}', None

    def execute_precases(self, case_id, env_id):
        precasesinfos = []
        precases = Precase.query.filter_by(parent_case_id=case_id, status=1).order_by(Precase.order).all()
        for precase in precases:
            caseid = precase.pre_case_id
            extract_expression = precase.extract_expression
            try:
                exerespon = self.exesinglecase(case_id=caseid, env_id=env_id)
                if not exerespon or json.loads(exerespon[0])['result'] in ['断言失败', '请求出错了']:
                    return None
                if extract_expression:
                    keys = extract_expression.split('.')
                    current = exerespon[1]
                    for key in keys:
                        if isinstance(current, list):
                            current = current[int(key)]
                        else:
                            current = current[key]

                    precaseinfo = {
                        'extract_result': current,
                        'extract_expression': extract_expression,
                        'pre_case_id': caseid
                    }
                    precasesinfos.append(precaseinfo)
            except Exception as e:
                logger.exception(e)
                return None
        return precasesinfos

    def replace_parameters(self, precasesinfos, parameterdic):
        for precaseinfo in precasesinfos:
            extract_expression = precaseinfo.get("extract_expression")
            if '${' + extract_expression + '}' in parameterdic['case_params']:
                parameterdic['case_params'] = parameterdic['case_params'].replace(
                    '${' + extract_expression + '}',
                    str(precaseinfo.get("extract_result"))
                )
        logger.info('替换后的参数是: {}'.format(parameterdic['case_params']))

    def send_request_and_assert(self, parameterdic, case_id, env_id):
        if parameterdic['protocol'] == 0:
            api = Api(
                url=parameterdic['case_url'],
                method=parameterdic['case_method'],
                params=parameterdic['case_params'],
                headers=parameterdic['case_headers']
            )
            apijson = api.getJson()
            spend = api.spend()
            if apijson == '请求出错了':
                return False, apijson, spend
            result = self.judgecase(apijson, case_id=case_id)[0]
            return result, apijson, spend
        else:
            return False, '{"result": "协议错误"}', None

    def judgecase(self, result, case_id=None):
        try:
            if not case_id:
                case_id = self.case_id
            flag = False
            caseasserts = InterfaceCaseAssert.query.filter_by(case_id=case_id, status=1).order_by(
                InterfaceCaseAssert.order).all()
            if not caseasserts:
                flag = True
                return flag, {'断言为空,默认通过'}

            assert_operators = {
                0: 'is_equal_to',
                1: 'is_less_than',
                2: 'is_greater_than',
                3: 'is_less_than_or_equal_to',
                4: 'is_greater_than_or_equal_to',
                5: 'string_equal_to',
                6: 'is_not_equal_to',
                7: 'matches',
                8: 'is_none',
                9: 'is_not_none',
                10: 'contains',
                11: 'is_empty',
                12: 'is_not_empty',
            }

            assertsinfs = []
            for i in caseasserts:
                assertinf = {'expression': i.expression, 'operator': i.operator, 'excepted_result': i.excepted_result}
                assertsinfs.append(assertinf)

            if not assertsinfs:
                return flag, {'组装断言信息出错'}

            logger.info('用例:{}'.format(case_id) + '  断言信息是: {}'.format(assertsinfs))
            for i in assertsinfs:
                try:
                    expression = i['expression']
                    operator = assert_operators.get(i['operator'])
                    expected_result = i['excepted_result']
                    assertflg = assert_value(result, expression, expected_result, operator)
                    if not assertflg:
                        return flag, {'断言失败'}
                except Exception as e:
                    logger.exception(e)
                    return flag, {'断言失败'}

            flag = True
            return flag, {'断言通过'}

        except Exception as e:
            logger.exception(e)
            return flag, {'执行过程中发生异常'}

    def assemble_parameters(self, case_id, env_id):
        """根据用例信息和环境信息组装参数"""
        res = {'case_url': None, 'case_method': None, 'case_params': None, 'case_headers': None, 'protocol': None}

        try:
            case = InterfaceCase.query.filter_by(case_id=case_id).first()
            env = Environment.query.filter_by(id=env_id).first()
            if case is None or env is None:
                return res
        except Exception as e:
            logger.exception(e)
            return res

        if env.url is None:
            return res

        if env.port is None:
            env_url = env.url
        else:
            env_url = env.url + ':' + env.port

        res['protocol'] = case.case_protocol

        if case.case_protocol == 0:  # HTTP 协议
            res['case_url'] = env_url + case.url
            res['case_method'] = CaseMethods(case.method).name
            res['case_headers'] = case.headers

            if case.method == 0:  # GET 方法
                res['case_params'] = case.params
            elif case.method == 1:  # POST 方法
                res['case_params'] = case.raw
        return res

    def save_case_result(self, result, caseid, ispass, testevir, spend=None):
        new_case = TestcaseResult(result=str(result),
                                  case_id=caseid,
                                  ispass=ispass, testevent_id=testevir, spend=spend, date=datetime.now())
        db.session.add(new_case)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.info('用例：%s保存测试结果失败!原因：%s' % (caseid, e))
