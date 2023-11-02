import json
from decimal import Decimal

from common.casemethod import CaseMethods
from common.exesql import ExeSql
from common.jsontools import reponse
from common.player import Player
from common.request_case import Api
from error_message import MessageEnum
from app.models import *
from common.systemlog import logger
from assertpy import assert_that


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
        if dbfac.sql_run_dev == 0:
            sqlurl = dbinf.url
            sqlusername = dbinf.username
            sqlpassword = dbinf.password
        elif dbfac.sql_run_dev == 1:
            sqlurl = dbinf.test_url
            sqlusername = dbinf.test_username
            sqlpassword = dbinf.test_password
        elif dbfac.sql_run_dev == 2:
            sqlurl = dbinf.dev_url
            sqlusername = dbinf.dev_username
            sqlpassword = dbinf.dev_password
        elif dbfac.sql_run_dev == 3:
            sqlurl = dbinf.stg_url
            sqlusername = dbinf.stg_username
            sqlpassword = dbinf.stg_password
        elif dbfac.sql_run_dev == 4:
            sqlurl = dbinf.prod_url
            sqlusername = dbinf.prod_username
            sqlpassword = dbinf.prod_password
        else:
            return reponse(code=MessageEnum.test_sql_query_error.value[0],
                           message=MessageEnum.test_sql_query_error.value[1])

        toexecsql = dbfac.sql_str
        linkurl = "mysql+pymysql://" + sqlusername + ":" + sqlpassword + "@" + sqlurl
        exesql = ExeSql(linkurl)
        result = exesql.exe_sql(toexecsql)

        return result

    def exesinglecase(self, case_id=None, env_id=None):  # 单个用例执行
        if not case_id:
            case_id = self.case_id
        if not env_id:
            env_id = self.env_id

        # 检查用例是否存在数据依赖并执行
        try:
            rely_dbf_id = InterfaceCase.query.filter_by(case_id=case_id).first().rely_dbf
            if not rely_dbf_id or rely_dbf_id == 0:
                pass
            else:
                dbfresult = self.exepredbf(dbf_id=rely_dbf_id)
                logger.info(dbfresult)
        except Exception as e:
            logger.exception(e)
            return '{"result": "case存在数据依赖，但是执行dbf失败"}', None

        try:  # 根据用例类型来组织请求参数
            parameterdic = self.assemble_parameters(case_id=case_id, env_id=env_id)
            if not parameterdic:
                return '{"result": "组装参数失败"}', None
        except Exception as e:
            logger.exception(e)
            return '{"result": "组装参数失败"}', None
        logger.info('parameterdic is :{}', parameterdic)
        if parameterdic['protocol'] == 0:
            api = Api(url=parameterdic['case_url'],
                      method=parameterdic['case_method'],
                      params=parameterdic['case_params'],
                      headers=parameterdic['case_headers'])
            apijson = api.getJson()
            spend = api.spend()
            if apijson == '请求出错了':
                self.save_case_result(apijson, case_id, ispass=False, testevir=env_id, spend=spend)
                return '{"result": "请求出错了"}', None
            res = self.judgecase(apijson, case_id)[0]
            if res is True:
                self.save_case_result(apijson, case_id, ispass=True, testevir=env_id, spend=spend)
                return '{"result": "断言通过"}', apijson
            else:
                self.save_case_result(apijson, case_id, ispass=False, testevir=env_id, spend=spend)
                return '{"result": "断言失败"}', apijson
        elif parameterdic['protocol'] == 1:
            pass
        elif parameterdic['protocol'] == 2:
            player = \
                Player(parameterdic['uid'], parameterdic['host'], parameterdic['port']).login_by_uid(
                    parameterdic['uid'])[1]
            client = player.client
            logger.info('parameterdic is :{}', parameterdic)
            starttime = datetime.datetime.now()
            client.send(parameterdic['case_req'], parameterdic['case_params'])
            msg = client.recv(parameterdic['case_rsp'])
            logger.info(msg.body)
            endtime = datetime.datetime.now()
            spend = (endtime - starttime).total_seconds()
            res = self.judgecase(msg.body, case_id)[0]
            if res is True:
                self.save_case_result(msg.body, case_id, ispass=True, testevir=env_id, spend=spend)
                return '{"result": "断言通过"}', msg.body
            else:
                self.save_case_result(msg.body, case_id, ispass=False, testevir=env_id, spend=spend)
                return '{"result": "断言失败"}', msg.body
        else:
            return '{"result": "协议错误"}', None

    def exemulticase(self, case_id=None, env_id=None):
        if not case_id:
            case_id = self.case_id
        if not env_id:
            env_id = self.env_id
        # 检查用例是否存在数据依赖并执行
        try:
            rely_dbf_id = InterfaceCase.query.filter_by(case_id=case_id).first().rely_dbf
            if not rely_dbf_id:
                pass
            else:
                dbfresult = self.exepredbf(dbf_id=rely_dbf_id)
                logger.info(dbfresult)
        except Exception as e:
            logger.exception(e)
            return '{"result": "case存在数据依赖，但是执行dbf失败"}', None

        try:
            precases = Precase.query.filter_by(parent_case_id=case_id).filter_by(status=1).order_by(Precase.order).all()
            if not precases:
                return '{"result": "前置用例查询为空"}', None
        except Exception as e:
            logger.exception(e)
            return '{"result": "前置用例查询失败"}', None
        precasesinfos = []
        for i in precases:  # 执行前置用例
            precaseinfo = {}
            caseid = i.pre_case_id
            extract_expression = i.extract_expression
            try:
                exerespon = self.exesinglecase(case_id=caseid, env_id=env_id)
                if not exerespon:
                    return '{"result":"前置用例' + str(caseid) + '执行失败"}', None
                else:
                    res = json.loads(exerespon[0])
                    if res['result'] == '断言失败':
                        return '{"result":"前置用例' + str(caseid) + '断言失败"}', None
                    elif res['result'] == '请求出错了':
                        return '{"result":"前置用例' + str(caseid) + '请求出错了"}', None
                    else:
                        precaseinfo['extract_result'] = exerespon[1][extract_expression[3:]]
                        precaseinfo['extract_expression'] = extract_expression
                        precaseinfo['pre_case_id'] = caseid
                        precasesinfos.append(precaseinfo)
            except Exception as e:
                logger.exception(e)
                return '{"result":"前置用例' + str(caseid) + '执行失败"}', None

        try:  # 根据用例类型来组织请求参数
            parameterdic = self.assemble_parameters(case_id=case_id, env_id=env_id)
            if not parameterdic:
                return '{"result": "组装参数失败"}', None
        except Exception as e:
            logger.exception(e)
            return '{"result": "组装参数失败"}', None

        for i in precasesinfos:  # 替换参数
            if i.get("extract_expression") in parameterdic['case_params']:
                parameterdic['case_params'] = parameterdic['case_params'].replace(i.get("extract_expression"),
                                                                                  str(i.get("extract_result")))
            else:
                pass

        logger.info('parameterdic is :{}', parameterdic)
        if parameterdic['protocol'] == 0:
            api = Api(url=parameterdic['case_url'],
                      method=parameterdic['case_method'],
                      params=parameterdic['case_params'],
                      headers=parameterdic['case_headers'])
            logger.info(api.to_json())
            apijson = api.getJson()
            spend = api.spend()
            if apijson == '请求出错了':
                self.save_case_result(apijson, self.case_id, ispass=False, testevir=self.env_id, spend=spend)
                return '{"result": "请求出错了"}', None
            res = self.judgecase(apijson, case_id=case_id)[0]
            if res is True:
                self.save_case_result(apijson, self.case_id, ispass=True, testevir=self.env_id, spend=spend)
                return '{"result": "断言通过"}', apijson
            else:
                self.save_case_result(apijson, self.case_id, ispass=False, testevir=self.env_id, spend=spend)
                return '{"result": "断言失败"}', apijson
        elif parameterdic['protocol'] == 1:
            pass  # todo grpc协议后续处理
        elif parameterdic['protocol'] == 2:
            player = \
                Player(parameterdic['uid'], parameterdic['host'], parameterdic['port']).login_by_uid(
                    parameterdic['uid'])[1]
            client = player.client
            logger.info('parameterdic is :{}', parameterdic)
            starttime = datetime.datetime.now()
            client.send(parameterdic['case_req'], parameterdic['case_params'])
            msg = client.recv(parameterdic['case_rsp'])
            logger.info(msg.body)
            endtime = datetime.datetime.now()
            spend = (endtime - starttime).total_seconds()
            res = self.judgecase(msg.body, case_id)[0]
            if res is True:
                self.save_case_result(msg.body, case_id, ispass=True, testevir=env_id, spend=spend)
                return '{"result": "断言通过"}', msg.body
            else:
                self.save_case_result(msg.body, case_id, ispass=False, testevir=env_id, spend=spend)
                return '{"result": "断言失败"}', msg.body
        else:
            return '{"result": "协议错误"}', None

    def judgecase(self, result, case_id=None):
        if not case_id:
            case_id = self.case_id
        flag = False
        caseasserts = InterfaceCaseAssert.query.filter_by(case_id=case_id).order_by(InterfaceCaseAssert.order).all()
        if not caseasserts:
            flag = True
            return flag, {'断言为空,默认通过'}
        else:
            assertsinfs = []
            for i in caseasserts:
                assertinf = {}
                assertinf['expression'] = i.expression[3:]
                assertinf['operator'] = i.operator
                assertinf['excepted_result'] = i.excepted_result
                assertsinfs.append(assertinf)
        if not assertsinfs:
            return flag, {'组装断言信息出错'}
        else:
            logger.info(assertsinfs)
            try:
                for i in assertsinfs:
                    if i['operator'] == 0:
                        assert_that(Decimal(result[i['expression']])).is_equal_to(Decimal(i['excepted_result']))
                    elif i['operator'] == 1:
                        assert_that(Decimal(result[i['expression']])).is_less_than(Decimal(i['excepted_result']))
                    elif i['operator'] == 2:
                        assert_that(Decimal(result[i['expression']])).is_greater_than(Decimal(i['excepted_result']))
                    elif i['operator'] == 3:
                        assert_that(Decimal(result[i['expression']])).is_less_than_or_equal_to(
                            Decimal(i['excepted_result']))
                    elif i['operator'] == 4:
                        assert_that(Decimal(result[i['expression']])).is_greater_than_or_equal_to(
                            Decimal(i['excepted_result']))
                    elif i['operator'] == 5:
                        assert_that(str(result[i['expression']])).is_equal_to(str(i['excepted_result']))
                    elif i['operator'] == 6:
                        assert_that(Decimal(result[i['expression']])).is_not_equal_to(Decimal(i['excepted_result']))
                    elif i['operator'] == 7:
                        assert_that(str(result[i['expression']])).matches(i['excepted_result'])
                    elif i['operator'] == 8:
                        assert_that(str(result[i['expression']])).is_none()
                    elif i['operator'] == 9:
                        assert_that(str(result[i['expression']])).is_not_none()
                    elif i['operator'] == 10:
                        assert_that(str(result[i['expression']])).contains(i['excepted_result'])
                    elif i['operator'] == 11:
                        assert_that(str(result[i['expression']])).is_empty()
                    elif i['operator'] == 12:
                        assert_that(str(result[i['expression']])).is_not_empty()
                    else:
                        return flag, {'断言符号错误'}
                flag = True
                return flag, {'断言通过'}
            except Exception as e:
                logger.exception(e)
                pass
        return flag, {'断言失败'}

    def assemble_parameters(self, case_id, env_id):  # 根据用例信息和环境信息组装参数
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
            env_url = env.url + ':' + env.port  # 拼接主url的域名
        # 用例信息的组装，需要根据用例的协议来组装，先处理http协议的。get和post的组装方式也不同，get参数放在表里的params字段，post参数放在表里的raw字段
        if case.case_protocol == 0:
            if case.method == 0:
                res['protocol'] = case.case_protocol
                res['case_url'] = env_url + case.url
                res['case_method'] = CaseMethods(case.method).name
                res['case_params'] = case.params
                res['case_headers'] = case.headers
            elif case.method == 1:
                res['protocol'] = case.case_protocol
                res['case_url'] = env_url + case.url
                res['case_method'] = CaseMethods(case.method).name
                res['case_params'] = case.raw
                res['case_headers'] = case.headers
        elif case.case_protocol == 1:
            pass  # todo 处理grpc协议的用例
        elif case.case_protocol == 2:  # 处理socket协议的用例参数
            res['protocol'] = case.case_protocol
            res['case_req'] = case.socketreq
            res['case_params'] = eval(case.raw)['req']
            res['case_rsp'] = case.socketrsp
            res['host'] = env.url
            res['port'] = env.port
            res['uid'] = eval(case.raw)['uid']
        elif case.case_protocol == 3:
            pass  # todo 处理ws协议的用例
        else:
            return res
        return res

    def save_case_result(self, result, caseid, ispass, testevir, spend=None):
        new_case = TestcaseResult(result=str(result),
                                  case_id=caseid,
                                  ispass=ispass, testevent_id=testevir, spend=spend)
        db.session.add(new_case)
        try:
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            logger.info('用例：%s保存测试结果失败!原因：%s' % (caseid, e))
