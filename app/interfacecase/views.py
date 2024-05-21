import gzip
import importlib
import io
import json
import multiprocessing
import os
import pickle
import sys
import time
from datetime import datetime
import traceback
from enum import Enum
from socket import socket

from flask import Blueprint, request, jsonify
from flask.views import MethodView
from flask_login import login_required, current_user
from sqlalchemy.orm import Session

from app.models import *
from common import GenerateProto
from common.AutoGenerateCase import generate_test_cases
from common.Client import Client
from common.jsontools import reponse
from common.player import Player
from error_message import MessageEnum
from common.log import logger
from common.executehandler import ExecuteHandler
from common.AnalysisPB import ProtoHandler, ProtoDir
from common.GenerateProto import *

from lib.CustomException import TimeOutException

interfacecase = Blueprint('interfacecase', __name__)

PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
largeResCache = Cache(user_home + "/cachefile")


class DataType(Enum):
    TYPE_DOUBLE = 1
    TYPE_FLOAT = 2
    TYPE_INT64 = 3
    TYPE_UINT64 = 4
    TYPE_INT32 = 5
    TYPE_FIXED64 = 6
    TYPE_FIXED32 = 7
    TYPE_BOOL = 8
    TYPE_STRING = 9
    TYPE_GROUP = 10
    TYPE_MESSAGE = 11
    TYPE_BYTES = 12
    TYPE_UINT32 = 13
    TYPE_ENUM = 14
    TYPE_SFIXED32 = 15
    TYPE_SFIXED64 = 16
    TYPE_SINT32 = 17
    TYPE_SINT64 = 18
    MAX_TYPE = 19


class ProcessManager:
    def __init__(self):
        self.process_dict = {}

    def get_process(self, branch_name):
        return self.process_dict.get(branch_name)

    def create_process(self, branch_name):
        if branch_name not in self.process_dict:
            process = multiprocessing.Process(target=self.worker_function, args=(branch_name,))
            self.process_dict[branch_name] = process
            process.start()
            return process
        else:
            return self.process_dict[branch_name]

    @staticmethod
    def worker_function(branch_name):
        # 在这里执行 branch_name 对应的任务
        # 例如：创建进程池，处理相关逻辑
        try:
            # 在这里执行 branch_name 对应的任务
            # 例如：创建进程池，处理相关逻辑
            pass
        except Exception as e:
            # 记录异常信息
            logger.error(f"Error in worker_function for branch {branch_name}: {str(e)}")
        finally:
            logger.info(f"Process for branch {branch_name} finished")


process_manager = ProcessManager()


class CreateCase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            interfacecase = InterfaceCase()
            interfacecase.project_id = data.get('project_id')
            interfacecase.model_id = data.get('model_id')
            interfacecase.case_protocol = data.get('case_protocol')
            interfacecase.is_relycase = data.get('is_relycase')
            interfacecase.rely_dbf = data.get('rely_dbf')
            interfacecase.url = data.get('url')
            interfacecase.method = data.get('method')
            interfacecase.desc = data.get('desc')
            interfacecase.headers = data.get('headers')
            interfacecase.params = data.get('params')
            interfacecase.form_data_encoded = data.get('form_data_encoded')
            interfacecase.form_data = data.get('form_data')
            interfacecase.socketreq = data.get('socketreq')
            interfacecase.socketrsp = data.get('socketrsp')
            interfacecase.raw = data.get('raw')
            interfacecase.raw_type = data.get('raw_type')
            interfacecase.body_type = data.get('body_type')
            interfacecase.creater = current_user.user_id
            interfacecase.created_time = data.get('created_time')
            interfacecase.update_time = data.get('update_time')
            interfacecase.source = data.get('source')
            interfacecase.import_no = data.get('import_no')

            db.session.add(interfacecase)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.add_case_erro.value[0], message=MessageEnum.add_case_erro.value[1])


class ModifyCase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            interfacecase = InterfaceCase.query.filter_by(case_id=data.get('case_id')).first()
            if not interfacecase:
                return reponse(code=MessageEnum.case_edit_error.value[0], message=MessageEnum.case_edit_error.value[1])

            interfacecase.project_id = data.get('project_id')
            interfacecase.model_id = data.get('model_id')
            interfacecase.case_protocol = data.get('case_protocol')
            interfacecase.is_relycase = data.get('is_relycase')
            interfacecase.rely_dbf = data.get('rely_dbf')
            interfacecase.url = data.get('url')
            interfacecase.method = data.get('method')
            interfacecase.desc = data.get('desc')
            interfacecase.headers = data.get('headers')
            interfacecase.params = data.get('params')
            interfacecase.form_data_encoded = data.get('form_data_encoded')
            interfacecase.form_data = data.get('form_data')
            interfacecase.socketreq = data.get('socketreq')
            interfacecase.socketrsp = data.get('socketrsp')
            interfacecase.raw = data.get('raw')
            interfacecase.raw_type = data.get('raw_type')
            interfacecase.body_type = data.get('body_type')
            interfacecase.creater = current_user.user_id
            interfacecase.created_time = data.get('created_time')
            interfacecase.update_time = data.get('update_time')
            interfacecase.source = data.get('source')
            interfacecase.import_no = data.get('import_no')

            db.session.add(interfacecase)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.case_edit_error.value[0], message=MessageEnum.case_edit_error.value[1])


class CreateAssert(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            interfacecaseassert = InterfaceCaseAssert()
            interfacecaseassert.assert_name = data.get('assert_name')
            interfacecaseassert.case_id = data.get('case_id')
            interfacecaseassert.type = data.get('type')
            interfacecaseassert.expression = data.get('expression')
            interfacecaseassert.operator = data.get('operator')
            interfacecaseassert.excepted_result = data.get('excepted_result')
            interfacecaseassert.order = data.get('order')
            interfacecaseassert.created_time = data.get('created_time')
            interfacecaseassert.update_time = data.get('update_time')

            db.session.add(interfacecaseassert)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.add_assert_erro.value[0], message=MessageEnum.add_assert_erro.value[1])


class GetCaseAssert(MethodView):
    @login_required
    def get(self):
        try:
            case_id = request.args.get('case_id')
            if not case_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            interfacecaseassert = InterfaceCaseAssert.query.filter_by(case_id=case_id, status=1).all()
            if not interfacecaseassert:
                return reponse(code=MessageEnum.get_assert_error.value[0],
                               message=MessageEnum.get_assert_error.value[1])
            res = []
            for i in interfacecaseassert:
                res.append(i.to_json())
            ret = {"list": res, "total": len(interfacecaseassert)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_assert_error.value[0], message=MessageEnum.get_assert_error.value[1])


class ModifyAssert(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            olddata = InterfaceCaseAssert.query.filter_by(case_id=data.get('caseid')).all()
            oldassertids = []
            for i in olddata:
                oldassertids.append(i.assert_id)
            newdata = data.get('asserts')
            if not newdata or len(newdata) == 0:
                for j in oldassertids:
                    logger.info('old assertid:{} not in newasserts', j)
                    interfacecaseassert = InterfaceCaseAssert.query.filter_by(assert_id=j).first()
                    interfacecaseassert.status = 0
                    interfacecaseassert.update_time = datetime.now()
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        return reponse(code=MessageEnum.edit_assert_error.value[0],
                                       message=MessageEnum.edit_assert_error.value[1])
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            logger.info("老数据是：{}".format(oldassertids))
            for i in newdata:
                if i['assert_id'] and i['assert_id'] in oldassertids:
                    logger.info('新传过来的 assertid:{}  在老数据里，是更新操作', i['assert_id'])
                    interfacecaseassert = InterfaceCaseAssert.query.filter_by(assert_id=i['assert_id']).first()
                    interfacecaseassert.assert_name = i['desc']
                    interfacecaseassert.case_id = data.get('caseid')
                    interfacecaseassert.type = 0
                    interfacecaseassert.expression = i['exp']
                    interfacecaseassert.operator = i['operator']
                    interfacecaseassert.excepted_result = i['expres']
                    interfacecaseassert.order = i['sort_id']
                    interfacecaseassert.status = 1
                    interfacecaseassert.update_time = datetime.now()
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        return reponse(code=MessageEnum.edit_assert_error.value[0],
                                       message=MessageEnum.edit_assert_error.value[1])
                else:
                    logger.info('old assertid:{} not in newasserts', i['assert_id'])
                    interfacecaseassert = InterfaceCaseAssert()
                    interfacecaseassert.assert_name = i['desc']
                    interfacecaseassert.case_id = data.get('caseid')
                    interfacecaseassert.type = 0
                    interfacecaseassert.expression = i['exp']
                    interfacecaseassert.operator = i['operator']
                    interfacecaseassert.excepted_result = i['expres']
                    interfacecaseassert.order = i['sort_id']
                    interfacecaseassert.created_time = datetime.now()
                    interfacecaseassert.update_time = datetime.now()
                    try:
                        db.session.add(interfacecaseassert)
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        return reponse(code=MessageEnum.edit_assert_error.value[0],
                                       message=MessageEnum.edit_assert_error.value[1])
            for j in oldassertids:
                if j not in [i['assert_id'] for i in newdata]:
                    logger.info('old assertid:{} not in newasserts', j)
                    interfacecaseassert = InterfaceCaseAssert.query.filter_by(assert_id=j).first()
                    interfacecaseassert.status = 0
                    interfacecaseassert.update_time = datetime.now()
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        return reponse(code=MessageEnum.edit_assert_error.value[0],
                                       message=MessageEnum.edit_assert_error.value[1])
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.edit_assert_error.value[0], message=MessageEnum.edit_assert_error.value[1])


class GetCaseByMod(MethodView):
    @login_required
    def get(self):
        try:
            model_id = request.args.get('model_id')
            if not model_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            page_index = 1
            page_number = 10
            if request.args.get("page_number"):
                page_number = request.args.get('page_number')
            if request.args.get("page_index"):
                page_index = request.args.get('page_index')
            interfacecase = InterfaceCase.query.filter_by(model_id=model_id, status=1).paginate(int(page_index),
                                                                                                int(page_number),
                                                                                                False)

            if not interfacecase:
                return reponse(code=MessageEnum.get_assert_error.value[0],
                               message=MessageEnum.get_assert_error.value[1])
            res = []
            for i in interfacecase.items:
                cr = User.query.filter_by(user_id=i.creater).first().username
                # logger.info(type(cr))
                pn = Project.query.filter_by(id=i.project_id).first().project_name
                mn = Model.query.filter_by(id=i.model_id).first().model_name
                tdic = {'case_id': i.case_id, 'project_id': i.project_id, 'model_id': i.model_id, 'desc': i.desc,
                        'project_name': pn, 'creator': cr,
                        'model_name': mn}
                res.append(tdic)
            ret = {"list": res, "total": interfacecase.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.not_find_your_case.value[0],
                           message=MessageEnum.not_find_your_case.value[1])


class ExecuteCase(MethodView):

    @login_required
    def post(self):
        try:
            logger.info('当前进程号：{}'.format(os.getpid()))
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            case_id = data.get('case_id')
            env_id = data.get('env_id')
            if not case_id or not env_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            case = InterfaceCase.query.filter_by(case_id=case_id).first()
            if not case:
                return reponse(code=MessageEnum.case_edit_error.value[0],
                               message=MessageEnum.case_edit_error.value[1])

            if case.case_protocol == 2:
                return self.execute_proto_case(data, case)
            else:
                return self.execute_normal_case(data, case, env_id)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.test_error.value[0],
                           message=MessageEnum.test_error.value[1])

    def execute_proto_case(self, data, case):
        try:
            start_time = time.time()
            logger.info('开始执行proto协议用例')
            case_raw = json.loads(case.raw)
            env_id = data.get('env_id', case_raw.get('env_id'))
            result_queue = multiprocessing.Queue()

            process = multiprocessing.Process(
                target=self.run_proto_case,
                args=(data, case_raw, env_id, result_queue)
            )

            process.start()
            process.join()

            cacheKey = result_queue.get()

            if isinstance(cacheKey, TimeOutException):
                new_case = TestcaseResult(
                    result=str(format(cacheKey)),
                    case_id=case.case_id,
                    ispass=False,
                    testevent_id=env_id,
                    spend=str("{:.2f}".format(time.time() - start_time)),
                    date=datetime.now()
                )
                db.session.add(new_case)
                db.session.commit()

                return reponse(code=MessageEnum.execute_timeout.value[0],
                               message=MessageEnum.execute_timeout.value[1], data=format(cacheKey))
            elif isinstance(cacheKey, Exception):
                new_case = TestcaseResult(
                    result=str(format(cacheKey)),
                    case_id=case.case_id,
                    ispass=False,
                    testevent_id=env_id,
                    spend=str("{:.2f}".format(time.time() - start_time)),
                    date=datetime.now()
                )
                db.session.add(new_case)
                db.session.commit()
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1], data=format(cacheKey))

            try:
                res = largeResCache.get(cacheKey)
                logger.info('从缓存中取出的结果是：{}'.format(res))
            except Exception as e:
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1], data=format(e))
            finally:
                largeResCache.delete(cacheKey)

            assert_pass = True
            caseassert = InterfaceCaseAssert.query.filter_by(case_id=case.case_id, status=1).all()
            if caseassert:
                assert_infos = []
                for i in caseassert:
                    # 分割属性名
                    levels = i.expression.split('.')
                    # 初始化当前层级的属性值为结果本身
                    current_value = res

                    # 逐级获取属性值
                    for level in levels:
                        # 如果当前层级的属性值不存在，跳出循环
                        if not current_value:
                            break
                        # 获取当前层级的属性值
                        current_value = current_value.get(level)

                    # 检查预期结果和实际值是否匹配
                    if isinstance(current_value, bool):
                        current_value = str(current_value).lower()
                    else:
                        current_value = str(current_value)
                    if i.excepted_result == current_value:
                        asres = '断言通过'
                    else:
                        asres = '断言失败'
                        assert_pass = False
                    assert_info = {'assert_res': asres, 'expression': i.expression, 'actual_result': current_value,
                                   'excepted_result': i.excepted_result, 'assert_name': i.assert_name}
                    assert_infos.append(assert_info)
                    res['assert_info'] = assert_infos

            isPass = not isinstance(res, Exception) and assert_pass
            end_time = time.time()
            spend_time = end_time - start_time

            new_case = TestcaseResult(
                result=str(res),
                case_id=case.case_id,
                ispass=isPass,
                testevent_id=env_id,
                spend=str("{:.2f}".format(spend_time)),
                date=datetime.now()
            )
            db.session.add(new_case)

            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)

        except Exception as e:
            logger.error(traceback.format_exc())
            db.session.rollback()
            return reponse(code=MessageEnum.execute_proto_error.value[0],
                           message=MessageEnum.execute_proto_error.value[1])

    def execute_normal_case(self, data, case, env_id):
        try:
            executehandler = ExecuteHandler(case.case_id, env_id)
            if case.is_relycase == 1:
                res = executehandler.exemulticase(case_id=case.case_id, env_id=env_id)[0]
            else:
                res = executehandler.exesinglecase(case_id=case.case_id, env_id=env_id)[0]
            logger.info(res)
            result_data = json.loads(res)
            if result_data['result'] == '断言通过':
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                               data=result_data)
            elif result_data['result'] == '断言失败':
                return reponse(code=MessageEnum.assert_fail.value[0], message=MessageEnum.assert_fail.value[1],
                               data=result_data)
            else:
                return reponse(code=MessageEnum.test_error.value[0], message=MessageEnum.test_error.value[1],
                               data=result_data)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.test_error.value[0],
                           message=MessageEnum.test_error.value[1])

    def run_proto_case(self, data, case_raw, env_id, result_queue):
        try:
            logger.info('当前进程号：{}'.format(os.getpid()))
            if not env_id:
                env_id = case_raw.get('env_id')

            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')

            res = exeproto(
                uid=case_raw['uid'],
                env_id=env_id,
                branch_name=case_raw['branch_name'],
                reqmessage=case_raw['req_message_name'],
                params=case_raw['proto_content'],
                source=case_raw['source']
            )

            largecachekeyExecase = case_raw['req_message_name'] + " " + str(time.time())[:6] + str(os.getpid())
            logger.info('用例管理处执行proto测试，将结果存入缓存，缓存key是：{}'.format(largecachekeyExecase))
            largeResCache.set(largecachekeyExecase, res, 60 * 60 * 24)
            result_queue.put(largecachekeyExecase)

        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(e)
        finally:
            sys.exit(0)


class AddPreCase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            pre_cases = data.get('pre_cases')
            if not pre_cases:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            for i in pre_cases:
                if not i['parent_case_id']:
                    return reponse(code=MessageEnum.must_be_every_parame.value[0],
                                   message=MessageEnum.must_be_every_parame.value[1])
                try:
                    parentcase = InterfaceCase.query.filter_by(case_id=i['parent_case_id']).first()
                    if not parentcase:
                        return reponse(code=MessageEnum.case_not_exict.value[0],
                                       message=MessageEnum.case_not_exict.value[1])
                except Exception as e:
                    logger.error(e)
                    return reponse(code=MessageEnum.case_not_exict.value[0],
                                   message=MessageEnum.case_not_exict.value[1])

                pre_case = Precase()
                pre_case.parent_case_id = i['parent_case_id']
                pre_case.extract_expression = i['extract_expression']
                pre_case.pre_case_id = i['pre_case_id']
                pre_case.order = i['order']
                pre_case.status = 1

                db.session.add(pre_case)
            try:
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            except Exception as e:
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.add_pre_case_error.value[0],
                               message=MessageEnum.add_pre_case_error.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.add_pre_case_error.value[0],
                           message=MessageEnum.add_pre_case_error.value[1])


class AddCase(MethodView):

    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if data.get('precases') == 0 or data.get('precases') is None or len(data.get('precases')) == 0:
                rely_case = 0
            else:
                rely_case = 1
            if data.get('basicinfo') and data.get('requestinfo'):
                interfacecase = InterfaceCase()
                interfacecase.project_id = data.get('basicinfo')['project_id']
                interfacecase.model_id = data.get('basicinfo')['model_id']
                interfacecase.case_protocol = data.get('requestinfo')['caseprotcol']
                interfacecase.is_relycase = rely_case
                interfacecase.rely_dbf = data.get('relydbf') if data.get('relydbf') else 0
                interfacecase.url = data.get('requestinfo')['url']
                interfacecase.method = data.get('requestinfo')['method']
                interfacecase.desc = data.get('basicinfo')['casedesc']
                headers = {}
                if data.get('requestinfo')['headers'] and data.get('requestinfo')['headers'] != '':
                    headers = json.loads(data.get('requestinfo')['headers'])
                interfacecase.headers = json.dumps(headers)
                params = {}
                if data.get('requestinfo')['params']:
                    requestparams = json.loads(data.get('requestinfo')['params'])
                    for i in requestparams:
                        params[i['name']] = i['value']
                interfacecase.params = json.dumps(params)

                interfacecase.socketreq = data.get('requestinfo')['socketreq']
                interfacecase.socketrsp = data.get('requestinfo')['socketrsp']
                interfacecase.raw = data.get('requestinfo')['raw']
                interfacecase.creater = current_user.user_id
                interfacecase.source = 0

                try:
                    db.session.add(interfacecase)
                    db.session.flush()
                    case_id = interfacecase.case_id
                    db.session.commit()
                except Exception as e:
                    logger.error(traceback.format_exc())
                    db.session.rollback()
                    return reponse(code=MessageEnum.add_case_erro.value[0],
                                   message=MessageEnum.add_case_erro.value[1])

                if data.get('asserts'):
                    for i in data.get('asserts'):
                        interfacecaseassert = InterfaceCaseAssert()
                        interfacecaseassert.assert_name = i['desc']
                        interfacecaseassert.case_id = case_id
                        interfacecaseassert.type = 0
                        interfacecaseassert.expression = i['exp']
                        interfacecaseassert.operator = i['operator']
                        interfacecaseassert.excepted_result = i['expres']
                        interfacecaseassert.order = i['sort_id']
                        # interfacecaseassert.created_time = i['created_time']
                        # interfacecaseassert.update_time = i['update_time']

                        db.session.add(interfacecaseassert)
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        db.session.rollback()
                        return reponse(code=MessageEnum.add_case_erro.value[0],
                                       message=MessageEnum.add_case_erro.value[1])
                if data.get('precases'):
                    for i in data.get('precases'):
                        pre_case = Precase()
                        pre_case.parent_case_id = case_id
                        pre_case.extract_expression = i['exp']
                        pre_case.pre_case_id = i['pre_case_id']
                        pre_case.order = i['sort_id']
                        pre_case.status = 1

                        db.session.add(pre_case)
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        db.session.rollback()
                        return reponse(code=MessageEnum.add_case_erro.value[0],
                                       message=MessageEnum.add_case_erro.value[1])
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.add_case_erro.value[0],
                           message=MessageEnum.add_case_erro.value[1])


class GetCaseByProj(MethodView):
    @login_required
    def get(self):
        try:
            project_id = request.args.get('project_id')
            if not project_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            page_index = 1
            page_number = 10
            if request.args.get("page_number"):
                page_number = request.args.get('page_number')
            if request.args.get("page_index"):
                page_index = request.args.get('page_index')
            interfacecase = InterfaceCase.query.filter_by(project_id=project_id, status=1).paginate(int(page_index),
                                                                                                    int(page_number),
                                                                                                    False)
            if not interfacecase:
                return reponse(code=MessageEnum.get_assert_error.value[0],
                               message=MessageEnum.get_assert_error.value[1])
            res = []
            for i in interfacecase.items:
                cr = User.query.filter_by(user_id=i.creater).first().username
                pn = Project.query.filter_by(id=i.project_id).first().project_name
                mn = Model.query.filter_by(id=i.model_id).first().model_name
                tdic = {'case_id': i.case_id, 'project_id': i.project_id, 'model_id': i.model_id, 'desc': i.desc,
                        'creator': cr, 'project_name': pn, 'model_name': mn}
                res.append(tdic)
            ret = {"list": res, "total": interfacecase.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_assert_error.value[0], message=MessageEnum.get_assert_error.value[1])


class Updateprecase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            # 获取旧的 pre_case_id 列表
            oldprecaseid = [i.pre_case_id for i in Precase.query.filter_by(parent_case_id=data.get('caseid')).all()]

            # 获取新数据
            newdata = data.get('precases', [])
            interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()

            # 根据新数据是否为空，更新 interfacecase 的 is_relycase 字段
            if not newdata:
                interfacecase.is_relycase = 0
            else:
                interfacecase.is_relycase = 1

            # 更新接口用例的更新时间
            interfacecase.update_time = datetime.now()

            # 提交数据库修改
            commit_or_rollback()

            # 遍历新数据
            for item in newdata:
                pre_case_id = item.get('pre_case_id')

                # 判断 pre_case_id 是否在旧数据中
                if pre_case_id in oldprecaseid:
                    logger.info(f'precaseid:{pre_case_id} in oldprecases')
                    # 如果在，更新对应的记录
                    pre_case = Precase.query.filter_by(parent_case_id=data.get('caseid'),
                                                       pre_case_id=pre_case_id).first()
                    pre_case.extract_expression = item.get('exp')
                    pre_case.order = item.get('sort_id')
                    pre_case.status = 1
                else:
                    logger.info(f'precaseid:{pre_case_id} not in oldprecases')
                    # 如果不在，创建新记录
                    pre_case = Precase()
                    pre_case.parent_case_id = data.get('caseid')
                    pre_case.extract_expression = item.get('exp')
                    pre_case.pre_case_id = pre_case_id
                    pre_case.order = item.get('sort_id')
                    pre_case.status = 1
                    oldprecaseid.append(pre_case_id)

                pre_case.update_time = datetime.now()
                db.session.add(pre_case)

            # 遍历旧的 pre_case_id 列表，检查是否在新数据中，如果不在，则置为无效
            for old_id in oldprecaseid:
                if not any(old_id == item.get('pre_case_id') for item in newdata):
                    logger.info(f'old precaseid:{old_id} not in newprecases')
                    pre_case = Precase.query.filter_by(parent_case_id=data.get('caseid'),
                                                       pre_case_id=old_id).first()
                    pre_case.status = 0
                    pre_case.update_time = datetime.now()

            # 提交数据库修改
            commit_or_rollback()

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            db.session.rollback()
            return reponse(code=MessageEnum.update_pre_case_error.value[0],
                           message=MessageEnum.update_pre_case_error.value[1])


def commit_or_rollback():
    """封装数据库提交或回滚操作"""
    try:
        db.session.commit()
    except Exception as e:
        logger.error(traceback.format_exc())
        db.session.rollback()
        return reponse(code=MessageEnum.update_pre_case_error.value[0],
                       message=MessageEnum.update_pre_case_error.value[1])


class Updatecasebase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()

            # 检查请求数据是否为空
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            # 获取基本信息
            baseinfo = data.get('basicinfo')

            # 查询接口实例
            interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()

            # 检查接口实例是否存在
            if not interfacecase:
                return reponse(code=MessageEnum.case_edit_error.value[0],
                               message=MessageEnum.case_edit_error.value[1])

            # 更新接口实例的属性
            interfacecase.project_id = baseinfo['project_id']
            interfacecase.model_id = baseinfo['model_id']
            interfacecase.desc = baseinfo['casedesc']
            interfacecase.update_time = datetime.now()
            interfacecase.creater = current_user.user_id

            # 提交事务
            db.session.commit()

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            db.session.rollback()
            return reponse(code=MessageEnum.case_edit_error.value[0],
                           message=MessageEnum.case_edit_error.value[1])


class Updatecasereq(MethodView):
    @login_required
    def post(self):
        try:
            # 获取请求数据
            data = request.get_json()

            # 如果请求数据为空，返回错误响应
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            # 获取请求信息和接口实例
            requestinfo = data.get('requestinfo')
            interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()

            # 如果接口实例不存在，返回错误响应
            if not interfacecase:
                return reponse(code=MessageEnum.case_edit_error.value[0],
                               message=MessageEnum.case_edit_error.value[1])

            # 更新接口实例的属性
            interfacecase.case_protocol = requestinfo.get('caseprotcol')
            interfacecase.url = requestinfo.get('url')
            interfacecase.method = requestinfo.get('method')

            # 更新请求头和参数
            interfacecase.headers = requestinfo.get('headers')
            interfacecase.params = self._parse_json(requestinfo.get('params'))

            interfacecase.socketreq = requestinfo.get('socketreq')
            interfacecase.socketrsp = requestinfo.get('socketrsp')
            if interfacecase.case_protocol == 2:
                raw_data = json.loads(interfacecase.raw) if interfacecase.raw else {}
                raw_data['proto_content'] = json.loads(requestinfo.get('raw'))['request_content']
                raw_data['uid'] = json.loads(requestinfo.get('raw'))['request_uid']
                raw_data['req_message_name'] = requestinfo.get('socketreq')
                interfacecase.raw = json.dumps(raw_data)
            else:
                interfacecase.raw = requestinfo.get('raw')

            interfacecase.update_time = datetime.now()
            interfacecase.creater = current_user.user_id

            # 提交事务
            db.session.commit()

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            db.session.rollback()
            return reponse(code=MessageEnum.case_edit_error.value[0],
                           message=MessageEnum.case_edit_error.value[1])

    def _parse_json(self, data):
        """
        解析 JSON 数据并返回字符串格式
        """
        if data:
            parsed_data = {}
            json_data = json.loads(data)
            for item in json_data:
                parsed_data[item['name']] = item['value']
            return json.dumps(parsed_data)
        return None


class Updatecasesql(MethodView):
    @login_required
    def post(self):

        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()
            if not data.get('relydbf') or data.get('relydbf') is None or data.get('relydbf') == 0:
                interfacecase.rely_dbf = 0
                try:
                    db.session.commit()
                except Exception as e:
                    logger.error(traceback.format_exc())
                    db.session.rollback()
                    return reponse(code=MessageEnum.case_edit_error.value[0],
                                   message=MessageEnum.case_edit_error.value[1])
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

            if not interfacecase:
                return reponse(code=MessageEnum.case_edit_error.value[0],
                               message=MessageEnum.case_edit_error.value[1])
            interfacecase.rely_dbf = data.get('relydbf')
            interfacecase.update_time = datetime.now()
            interfacecase.creater = current_user.user_id
            try:
                db.session.commit()
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.case_edit_error.value[0],
                               message=MessageEnum.case_edit_error.value[1])
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            db.session.rollback()
            return reponse(code=MessageEnum.case_edit_error.value[0],
                           message=MessageEnum.case_edit_error.value[1])


class Getprecase(MethodView):
    @login_required
    def get(self):
        try:
            case_id = request.args.get('case_id')
            if not case_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            precases = Precase.query.filter_by(parent_case_id=case_id, status=1).all()
            if not precases:
                return reponse(code=MessageEnum.get_pre_case_error.value[0],
                               message=MessageEnum.get_pre_case_error.value[1])
            res = []
            for i in precases:
                res.append(i.to_json())
            ret = {"list": res, "total": len(precases)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_pre_case_error.value[0],
                           message=MessageEnum.get_pre_case_error.value[1])


class Getcasedetail(MethodView):
    @login_required
    def get(self):
        try:
            case_id = request.args.get('case_id')
            if not case_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            interfacecase = InterfaceCase.query.get_or_404(case_id)
            creator = User.query.get(interfacecase.creater).username
            model_name = Model.query.get(interfacecase.model_id).model_name
            project_name = Project.query.get(interfacecase.project_id).project_name

            basicinfo = {
                'case_id': interfacecase.case_id,
                'project_id': interfacecase.project_id,
                'model_id': interfacecase.model_id,
                'desc': interfacecase.desc,
                'creator': creator,
                'project_name': project_name,
                'model_name': model_name
            }

            headers = interfacecase.headers if interfacecase.headers else '{}'

            params = [{'name': k, 'value': v} for k, v in json.loads(interfacecase.params).items()] \
                if interfacecase.params else []

            if interfacecase.case_protocol == 2:
                raw = {}
                request_content = json.loads(interfacecase.raw)['proto_content']
                request_uid = json.loads(interfacecase.raw)['uid']
                raw['request_content'] = request_content
                raw['request_uid'] = request_uid
                interfacecase.raw = json.dumps(raw)

            requestinfo = {
                'caseprotcol': interfacecase.case_protocol,
                'url': interfacecase.url,
                'method': interfacecase.method,
                'headers': headers,
                'params': params,
                'socketreq': interfacecase.socketreq,
                'socketrsp': interfacecase.socketrsp,
                'raw': interfacecase.raw
            }

            precasedata = [i.to_json() for i in Precase.query.filter_by(parent_case_id=case_id, status=1).all()]

            assertdata = [i.to_json() for i in InterfaceCaseAssert.query.filter_by(case_id=case_id, status=1).all()]

            ret = {
                'basicinfo': basicinfo,
                'requestinfo': requestinfo,
                'precases': precasedata,
                'asserts': assertdata,
                'relydbf': interfacecase.rely_dbf
            }

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_case_detail_error.value[0],
                           message=MessageEnum.get_case_detail_error.value[1])


class Deletecase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            case_id = data.get('case_id')
            interfacecase = InterfaceCase.query.filter_by(case_id=case_id).first()
            if not interfacecase:
                return reponse(code=MessageEnum.case_not_exict.value[0],
                               message=MessageEnum.case_not_exict.value[1])
            interfacecase.status = 0
            interfacecase.update_time = datetime.now()
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            db.session.rollback()
            return reponse(code=MessageEnum.delete_case_error.value[0],
                           message=MessageEnum.delete_case_error.value[1])


class Getcaseres(MethodView):
    @login_required
    def get(self):
        try:
            case_id = request.args.get('case_id')
            if not case_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            page_index = 1
            page_number = 10
            if request.args.get("page_number"):
                page_number = request.args.get('page_number')
            if request.args.get("page_index"):
                page_index = request.args.get('page_index')

            query = TestcaseResult.query.filter_by(case_id=case_id)
            query = query.order_by(TestcaseResult.id.desc())
            caseres = query.paginate(int(page_index), int(page_number))

            if not caseres:
                return reponse(code=MessageEnum.get_case_res_error.value[0],
                               message=MessageEnum.get_case_res_error.value[1])
            res = []
            for i in caseres.items:
                case_desc = InterfaceCase.query.filter_by(case_id=i.case_id).first().desc
                env_name = Environment.query.filter_by(id=i.testevent_id).first().name
                tdic = {'res_id': i.id, 'case_id': i.case_id, 'case_desc': case_desc,
                        'env_name': env_name, 'response': i.result, 'result': i.ispass,
                        'testtime': str(i.date),
                        'duration': i.spend}
                res.append(tdic)
            ret = {"list": res, "total": caseres.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_case_res_error.value[0],
                           message=MessageEnum.get_case_res_error.value[1])


class Allcases(MethodView):
    @login_required
    def get(self):
        try:
            interfacecase = InterfaceCase.query.filter_by(status=1).all()
            if not interfacecase:
                return reponse(code=MessageEnum.get_assert_error.value[0],
                               message=MessageEnum.get_assert_error.value[1])
            res = []
            for i in interfacecase:
                cr = User.query.filter_by(user_id=i.creater).first().username
                pn = Project.query.filter_by(id=i.project_id).first().project_name
                tdic = {'case_id': i.case_id, 'project_id': i.project_id, 'model_id': i.model_id, 'desc': i.desc,
                        'creator': cr, 'project_name': pn}
                res.append(tdic)
            ret = {"list": res, "total": len(interfacecase)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_assert_error.value[0], message=MessageEnum.get_assert_error.value[1])


class Getbranchproto(MethodView):
    @login_required
    def get(self):
        try:
            logger.info("Getbranchproto 函数 当前主进程 ID: {}".format(os.getpid()))
            source = request.args.get('source')
            branch = request.args.get('branch_name')
            if not branch or not source:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if '/' in branch:
                branch = branch.replace('/', '_')

            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process,
                args=(branch, source, result_queue)
            )

            process.start()
            process.join()

            # Retrieve results from the Queue
            proto_names = result_queue.get()

            if proto_names:
                ret = {"list": proto_names, "total": len(proto_names)}
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
            else:
                return reponse(code=MessageEnum.get_proto_error.value[0],
                               message=MessageEnum.get_proto_error.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.unexpected_error.value[0],
                           message=MessageEnum.unexpected_error.value[1])

    def run_in_new_process(self, branch, source, result_queue):
        try:
            logger.info("获取proto name，在新进程中，当前进程 ID: {}".format(os.getpid()))

            # Redirect standard input/output/error to /dev/null
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')

            # Create a ProtoDir instance within the new process
            proto_dir = ProtoDir()

            # Get branch proto names
            proto_names = proto_dir.get_branch_protoname(branches=branch, source=source)

            # Put results into the Queue
            result_queue.put(proto_names)

        except Exception as e:
            logger.error(traceback.format_exc())
            # Put None into the Queue if there's an exception
            result_queue.put(None)
        finally:
            # Explicitly exit the process to avoid Resource temporarily unavailable error
            sys.exit(0)


def import_module_and_get_descriptor_info(branch_name, module_name, source):
    try:
        logger.info("import_module_and_get_descriptor_info 函数 当前进程 ID: {}".format(os.getpid()))
        if source == 'kk' or source is None:
            path = PROJECT_ROOT + "/proto/" + branch_name
        else:
            path = PROJECT_ROOT + "/proto/pp/" + branch_name
        os.chdir(path)
        sys.path.append(path)

        # 导入模块
        importlib.import_module(module_name)

        # 获取 FileDescriptor 信息
        file_descriptor = getattr(sys.modules[module_name], "DESCRIPTOR")
        messages = [message_name for message_name in file_descriptor.message_types_by_name if
                    message_name.endswith("REQ")]

        return {"messages": messages}

    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


class GetMessageInfo(MethodView):
    @login_required
    def get(self):
        try:
            logger.info("GetMessageInfo 函数 当前主进程 ID: {}".format(os.getpid()))
            branch_name = request.args.get('branch_name')
            proto_name = request.args.get('proto_name')
            source = request.args.get('source')

            if not branch_name or not proto_name:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if '/' in branch_name:
                branch_name = branch_name.replace('/', '_')
            if source == 'kk' or source is None:
                module_name = f"proto.{branch_name}.{proto_name}"
            else:
                module_name = f"proto.pp.{branch_name}.{proto_name}"
            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process,
                args=(branch_name, module_name, source, result_queue)
            )

            process.start()
            process.join()

            # Retrieve results from the Queue
            results = result_queue.get()

            if results:
                messages = results["messages"]
                ret = {"list": messages, "total": len(messages)}
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
            else:
                return reponse(code=MessageEnum.get_proto_error.value[0],
                               message=MessageEnum.get_proto_error.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.unexpected_error.value[0],
                           message=MessageEnum.unexpected_error.value[1])

    def run_in_new_process(self, branch_name, module_name, source, result_queue):
        try:
            logger.info("获取proto message，在新进程中，当前进程 ID: {}".format(os.getpid()))
            # Redirect standard input/output/error to /dev/null
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')

            results = import_module_and_get_descriptor_info(branch_name, module_name, source)
            result_queue.put(results)
        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(None)
        finally:
            sys.exit(0)


# def get_message_attributes(branch_name, message_name, source):
#     try:
#         logger.info("get_message_attributes 函数 当前进程 ID: {}".format(os.getpid()))
#         if source == 'kk' or source is None:
#             path = PROJECT_ROOT + "/proto/" + branch_name
#         else:
#             path = PROJECT_ROOT + "/proto/pp/" + branch_name
#         os.chdir(path)
#         sys.path.append(path)  # 将模块路径添加到 sys.path 中
#
#         for file_name in os.listdir(path):
#             if file_name.endswith(".py") and file_name != "__init__.py":
#                 module_name = os.path.splitext(file_name)[0]
#                 importlib.import_module(module_name)
#
#         for module_name in sys.modules:
#             if module_name.endswith("_pb2"):
#                 module = sys.modules[module_name]
#                 if hasattr(module, message_name):
#                     message_type = getattr(module, message_name)
#                     attributes = []
#
#                     for field in message_type.DESCRIPTOR.fields:
#                         field_name = field.name
#                         field_number = field.number
#                         field_data_type = field.type  # 获取属性的数据类型
#                         field_label = field.label  # 获取属性的标签
#
#                         if field_label == 3:  # 如果字段是重复类型
#                             is_repeated = True
#                         else:
#                             is_repeated = False
#
#                         if field_data_type == 14:
#                             enum_values = []
#                             enum_descriptor = field.enum_type
#                             for enum_value in enum_descriptor.values_by_name.values():
#                                 enum_values.append({enum_value.name: enum_value.number})
#                             attributes.append(
#                                 {"name": field_name, "number": field_number, "type": DataType(field_data_type).name,
#                                  "enum_values": enum_values, "is_repeated": is_repeated})
#                         elif field_data_type == 11:
#                             sub_message_fields = []
#                             for sub_field in field.message_type.fields:
#                                 sub_message_fields.append(
#                                     {"name": sub_field.name, "type": DataType(sub_field.type).name})
#                             attributes.append(
#                                 {"name": field_name, "number": field_number, "type": DataType(field_data_type).name,
#                                  "fields": sub_message_fields, "is_repeated": is_repeated})
#                         else:
#                             attributes.append(
#                                 {"name": field_name, "number": field_number, "type": DataType(field_data_type).name,
#                                  "is_repeated": is_repeated})
#                     return {"message_name": message_name, "attributes": attributes}
#         # 如果未找到指定的消息名，返回空字典
#         return {}
#
#     except Exception as e:
#         logger.error(traceback.format_exc())
#         raise e


class Getattbymessage(MethodView):
    @login_required
    def get(self):
        try:
            logger.info("获取message里的属性 当前主进程 ID: {}".format(os.getpid()))
            branch_name = request.args.get('branch_name')
            message_name = request.args.get('message_name')
            source = request.args.get('source')

            if not branch_name or not message_name:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if '/' in branch_name:
                branch_name = branch_name.replace('/', '_')

            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process,
                args=(branch_name, message_name, source, result_queue)
            )

            process.start()
            process.join()

            # Retrieve results from the Queue
            attributes_info = result_queue.get()
            logger.info("获取message里的属性结果: {}".format(attributes_info))

            if attributes_info:
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                               data=attributes_info)
            else:
                return reponse(code=MessageEnum.get_attributes_error.value[0],
                               message=MessageEnum.get_attributes_error.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_attributes_error.value[0],
                           message=MessageEnum.get_attributes_error.value[1])

    def run_in_new_process(self, branch_name, message_name, source, result_queue):
        try:
            logger.info("获取attributes info，在新进程中，当前进程 ID: {}".format(os.getpid()))
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            attributes_info = get_message_attributes(branch_name, message_name, source)

            # Put results into the Queue
            result_queue.put(attributes_info)
        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(None)
        finally:
            sys.exit(0)


def get_field_attributes(field):
    field_data_type = field.type
    field_name = field.name
    field_number = field.number
    field_label = field.label

    if field_label == 3:  # 如果字段是重复类型
        is_repeated = True
    else:
        is_repeated = False

    if field_data_type == 14:  # 枚举类型
        enum_values = []
        enum_descriptor = field.enum_type
        for enum_value in enum_descriptor.values_by_name.values():
            enum_values.append({enum_value.name: enum_value.number})
        return {"name": field_name, "number": field_number, "type": DataType(field_data_type).name,
                "enum_values": enum_values, "is_repeated": is_repeated}

    elif field_data_type == 11:  # 子消息类型
        sub_message_fields = []
        for sub_field in field.message_type.fields:
            sub_message_fields.append(get_field_attributes(sub_field))
        return {"name": field_name, "number": field_number, "type": DataType(field_data_type).name,
                "fields": sub_message_fields, "is_repeated": is_repeated}

    else:  # 其他类型
        return {"name": field_name, "number": field_number, "type": DataType(field_data_type).name,
                "is_repeated": is_repeated}


def get_message_attributes(branch_name, message_name, source):
    try:
        logger.info("get_message_attributes 函数 当前进程 ID: {}".format(os.getpid()))
        if source == 'kk' or source is None:
            path = PROJECT_ROOT + "/proto/" + branch_name
        else:
            path = PROJECT_ROOT + "/proto/pp/" + branch_name
        os.chdir(path)
        sys.path.append(path)  # 将模块路径添加到 sys.path 中

        for file_name in os.listdir(path):
            if file_name.endswith(".py") and file_name != "__init__.py":
                module_name = os.path.splitext(file_name)[0]
                importlib.import_module(module_name)

        for module_name in sys.modules:
            if module_name.endswith("_pb2"):
                module = sys.modules[module_name]
                if hasattr(module, message_name):
                    message_type = getattr(module, message_name)
                    attributes = []

                    for field in message_type.DESCRIPTOR.fields:
                        attributes.append(get_field_attributes(field))

                    return {"message_name": message_name, "attributes": attributes}

        # 如果未找到指定的消息名，返回空字典
        return {}

    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


def exeproto(uid, env_id, branch_name, reqmessage, params, source):
    try:
        logger.info('执行请求方法exeproto的进程号：{}'.format(os.getpid()))
        if source == 'kk' or source is None:
            proto_path = PROJECT_ROOT + "/proto/" + branch_name
        else:
            proto_path = PROJECT_ROOT + "/proto/pp/" + branch_name
        env = Environment.query.filter_by(id=env_id).first()
        host = env.url
        port = env.port

        sys.path.append(proto_path)

        player = Player(uid, host, port)
        if not player.client:
            player.client = Client(host=host, port=port)
        for name in os.listdir(proto_path):
            if name == '__init__.py' or name[-3:] != '.py':
                continue
            if source == 'kk' or source is None:
                module = importlib.import_module(f"proto.{branch_name}.{name[:-3]}")
            else:
                module = importlib.import_module(f"proto.pp.{branch_name}.{name[:-3]}")
            for item in dir(module):
                player.client.pb[item] = getattr(module, item)
        if source == 'kk' or source is None:
            player = player.login_by_uid(uid)[1]
        else:
            player = player.login_by_uid_pp(uid)[1]
        client = player.client
        client.send(reqmessage, params)
        logger.info('send message:{},send content:{}', reqmessage, params)
        rspmessage = reqmessage[:-3] + "RSP"
        msg = client.recv(rspmessage)
        # logger.info('recv message:{}', msg.body)
        client.stop()
        client = None
        return msg.body
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


class Executeproto(MethodView):
    @login_required
    def post(self):
        try:
            logger.info('主进程号：{}'.format(os.getpid()))
            data = request.get_json()
            if not data.get('req_message_name') or not data.get('env_id') or not data.get(
                    'uid') or not data.get('branch_name') or not data.get('source'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            branch_name = data.get('branch_name')
            source = data.get('source')
            if '/' in branch_name:
                branch_name = branch_name.replace('/', '_')
            if not data.get('proto_content') or data.get('proto_content') is None:
                params = {}
            else:
                params = data.get('proto_content')

            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process,
                args=(data, branch_name, params, source, result_queue)
            )

            process.start()
            process.join()

            cache = result_queue.get()

            if isinstance(cache, Exception):
                # If res is an exception, handle it accordingly
                if isinstance(cache, TimeOutException):
                    rstr = '执行超时了，请确认目标服务器的处理情况'
                    return reponse(code=MessageEnum.execute_timeout.value[0],
                                   message=MessageEnum.execute_timeout.value[1], data=rstr)
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1], data=format(cache))

            try:
                res = largeResCache.get(cache)
                logger.info('从缓存中取出的结果是：{}'.format(res))
            except Exception as e:
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1], data=format(e))
            finally:
                largeResCache.delete(cache)

            assert_info = data.get('assert_info')
            temp = res
            if not assert_info:
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)
            else:
                expected = assert_info.get('excepted_result')
                expression = assert_info.get('expression')

                if '.' in expression:
                    for i in expression.split('.'):
                        temp = temp[i]
                else:
                    temp = temp[expression]
                assertres = {'excepted_result': expected, 'actual_result': temp}
                ret = {'assert_info': assertres, 'response': res}
                if isinstance(temp, bool):
                    temp = str(temp).lower()
                else:
                    temp = str(temp)
                if temp == expected:
                    return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
                else:
                    return reponse(code=MessageEnum.assert_error.value[0], message=MessageEnum.assert_error.value[1],
                                   data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.execute_proto_error.value[0],
                           message=MessageEnum.execute_proto_error.value[1], data=format(e))

    def run_in_new_process(self, data, branch_name, params, source, result_queue):
        try:
            logger.info('当前进程号：{}'.format(os.getpid()))
            res = exeproto(uid=data.get('uid'), env_id=data.get('env_id'), branch_name=branch_name,
                           reqmessage=data.get('req_message_name'), params=params, source=source)

            largecachekey = data.get('req_message_name') + " " + str(time.time())[:6] + str(os.getpid())
            logger.info('将结果存入缓存，缓存key是：{}'.format(largecachekey))
            largeResCache.set(largecachekey, res, 60 * 60 * 24)
            result_queue.put(largecachekey)
        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(e)
        finally:
            sys.exit(0)


class Onesaveproto(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not all(data.get(field) for field in ['req_message_name', 'env_id', 'uid', 'case_desc',
                                                     'project_id', 'model_id']):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            interfacecase = InterfaceCase(
                project_id=data['project_id'],
                model_id=data['model_id'],
                desc=data['case_desc'],
                case_protocol=2,
                is_relycase=0,
                rely_dbf=0,
                socketreq=data['req_message_name'],
                raw=json.dumps(data),
                creater=current_user.user_id,
                source=1
            )

            try:
                db.session.add(interfacecase)
                db.session.flush()
                case_id = interfacecase.case_id

                assert_info = data.get('assert_info', {})
                if assert_info:
                    common_assert_info = {
                        'case_id': case_id,
                        'status': 1,
                        'created_time': datetime.now(),
                        'update_time': datetime.now(),
                        'operator': 0,
                        'assert_name': data['case_desc'] + '断言',
                        'order': 1
                    }
                    interfacecaseassert = InterfaceCaseAssert(**{**common_assert_info, **assert_info})
                    db.session.add(interfacecaseassert)

                db.session.commit()
                ret = {"case_id": case_id}
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                               data=ret)
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.add_case_erro.value[0],
                               message=MessageEnum.add_case_erro.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.add_case_erro.value[0],
                           message=MessageEnum.add_case_erro.value[1])


class Getbranches(MethodView):
    @login_required
    def get(self):
        source = request.args.get('source')
        git_repo = 'http://git.kkpoker.co/server/doc.git'
        svn_repo = 'svn://devsvn.pppoker.net/PPPoker/proto/'
        try:
            list = []
            if source == 'kk' or source is None:
                brancheslist = GenerateProto.get_recently_active_branches_cached(git_repo)
            elif source == 'pp':
                brancheslist = GenerateProto.get_recently_active_branches_pp()
            for i in brancheslist:
                list.append(i[0])
            ret = {"list": list, "total": len(list)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_branch_error.value[0], message=MessageEnum.get_branch_error.value[1])


class Forceupdatebranch(MethodView):
    @login_required
    def get(self):
        try:
            branch_name = request.args.get('branch_name')
            source = request.args.get('source')

            if not branch_name:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process,
                args=(branch_name, source, result_queue)
            )

            process.start()
            process.join()

            # Retrieve results from the Queue
            proto_names = result_queue.get()

            if proto_names:
                ret = {"list": proto_names, "total": len(proto_names)}
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
            else:
                return reponse(code=MessageEnum.force_update_branch_error.value[0],
                               message=MessageEnum.force_update_branch_error.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.force_update_branch_error.value[0],
                           message=MessageEnum.force_update_branch_error.value[1])

    def run_in_new_process(self, branch_name, source, result_queue):
        try:
            logger.info("在新进程中执行下载和编译 proto，当前进程 ID: {}".format(os.getpid()))
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            if source == 'kk' or source is None:
                GenerateProto.download_and_compile_protos(branch_name)
            elif source == 'pp':
                GenerateProto.download_and_compile_protos_pp(branch_name)

            proto_names = []
            script_directory = os.path.dirname(os.path.abspath(__file__))
            project_root = os.path.abspath(os.path.join(script_directory, '..', '..'))
            proto_root = os.path.join(project_root, 'proto')
            if source == 'kk' or source is None:
                proto_dir = os.path.join(proto_root, branch_name)
            else:
                proto_dir = os.path.join(proto_root, 'pp', branch_name)
            for file in os.listdir(proto_dir):
                if re.match(r".*_pb2.py", file):
                    proto_name = file.split(".")[0]
                    proto_names.append(proto_name)

            # Put results into the Queue
            result_queue.put(proto_names)

        except Exception as e:
            logger.error(traceback.format_exc())
            # Put None into the Queue if there's an exception
            result_queue.put(None)
        finally:
            sys.exit(0)


class ExecuteprotoMult(MethodView):
    @login_required
    def post(self):
        try:
            logger.info('主进程号：{}'.format(os.getpid()))
            data = request.get_json()
            if not data.get('env_id') or not data.get(
                    'uid') or not data.get('branch_name') or not data.get('source') or not data.get('parainfos'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            branch_name = data.get('branch_name')
            source = data.get('source')
            parainfos = data.get('parainfos')
            if '/' in branch_name:
                branch_name = branch_name.replace('/', '_')

            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process_mult,
                args=(data, branch_name, source, parainfos, result_queue)
            )

            process.start()
            process.join()

            # Retrieve results from the Queue
            res = result_queue.get()

            if res:
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)
            else:
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.execute_proto_error.value[0],
                           message=MessageEnum.execute_proto_error.value[1])

    def run_in_new_process_mult(self, data, branch_name, source, parainfos, result_queue):
        try:
            logger.info('当前进程号：{}'.format(os.getpid()))
            # Redirect standard input/output/error to /dev/null
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            res = exeprotomult(uid=data.get('uid'), env_id=data.get('env_id'), branch_name=branch_name,
                               source=source, parainfos=parainfos)

            # Put results into the Queue
            result_queue.put(res)

        except Exception as e:
            logger.error(traceback.format_exc())
            # Put None into the Queue if there's an exception
            result_queue.put(None)
        finally:
            sys.exit(0)


def exeprotomult(uid, env_id, branch_name, source, parainfos):
    try:
        logger.info('执行请求方法exeproto的进程号：{}'.format(os.getpid()))
        if source == 'kk' or source is None:
            proto_path = PROJECT_ROOT + "/proto/" + branch_name
        else:
            proto_path = PROJECT_ROOT + "/proto/pp/" + branch_name
        env = Environment.query.filter_by(id=env_id).first()
        host = env.url
        port = env.port
        reslut = []
        sys.path.append(proto_path)

        player = Player(uid, host, port)
        if not player.client:
            player.client = Client(host=host, port=port)
        for name in os.listdir(proto_path):
            if name == '__init__.py' or name[-3:] != '.py':
                continue
            if source == 'kk' or source is None:
                module = importlib.import_module(f"proto.{branch_name}.{name[:-3]}")
            else:
                module = importlib.import_module(f"proto.pp.{branch_name}.{name[:-3]}")
            for item in dir(module):
                player.client.pb[item] = getattr(module, item)
        if source == 'kk' or source is None:
            player = player.login_by_uid(uid)[1]
        else:
            player = player.login_by_uid_pp(uid)[1]
        client = player.client

        parainfos = sorted(parainfos, key=lambda x: x.get('step'))

        for i in parainfos:
            params = {"uid": uid, "req": i['proto_content']}
            reqmessage = i['req_message_name']
            rspmessage = i['rsq_message_name']
            client.send(reqmessage, params)
            msg = client.recv(rspmessage)
            r = {i['step']: msg.body}
            reslut.append(r)
        client.stop()
        client = None
        return reslut
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


class Createsuite(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('suite_name') or not data.get('case_ids') or not data.get('project_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            suite = TestSuite()
            suite.name = data.get('suite_name')
            suite.caseids = json.dumps(data.get('case_ids'))
            suite.creator = current_user.user_id
            suite.project = data.get('project_id')
            suite.status = 1
            try:
                db.session.add(suite)
                db.session.commit()
                ret = {'suite_id': suite.id}
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.create_suite_error.value[0],
                               message=MessageEnum.create_suite_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.create_suite_error.value[0],
                           message=MessageEnum.create_suite_error.value[1])


class Getsuitebyid(MethodView):
    @login_required
    def get(self):
        try:
            suite_id = request.args.get('suite_id')
            if not suite_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            suite = TestSuite.query.filter_by(id=suite_id).first()
            if not suite:
                return reponse(code=MessageEnum.get_suite_error.value[0],
                               message=MessageEnum.get_suite_error.value[1])
            if suite.status == 0:
                return reponse(code=MessageEnum.suite_deleted.value[0],
                               message=MessageEnum.suite_deleted.value[1])
            projectname = suite.projects.project_name
            creatorname = suite.users.username

            suiteinfo = {
                'suite_id': suite.id,
                'name': suite.name,
                'caseids': json.loads(suite.caseids),
                'project_name': projectname,
                'creator_name': creatorname
            }
            ret = []
            ret.append(suiteinfo)

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_suite_error.value[0],
                           message=MessageEnum.get_suite_error.value[1])


class Getsuitebyname(MethodView):
    @login_required
    def get(self):
        try:
            suite_name = request.args.get('suite_name')
            page_index = request.args.get('page_index') or 1
            page_number = request.args.get('page_number') or 10
            if not suite_name:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            suites = TestSuite.query.filter(TestSuite.name.like(f'%{suite_name}%')).filter_by(status=1).paginate(
                int(page_index), int(page_number),
                False).items
            total = TestSuite.query.filter(TestSuite.name.like(f'%{suite_name}%')).filter_by(status=1).count()
            if not suites:
                return reponse(code=MessageEnum.get_suite_error.value[0],
                               message=MessageEnum.get_suite_error.value[1])
            list = []
            for i in suites:
                if i.status == 0:
                    continue
                caseinfos = []
                for j in json.loads(i.caseids):
                    t = InterfaceCase.query.filter_by(case_id=j).first()
                    caseinfo = {'case_id': t.case_id, 'desc': t.desc}
                    caseinfos.append(caseinfo)
                projectname = i.projects.project_name
                creatorname = i.users.username

                suiteinfo = {
                    'suite_id': i.id,
                    'name': i.name,
                    'caseinfos': caseinfos,
                    'project_name': projectname,
                    'creator_name': creatorname
                }
                list.append(suiteinfo)

            ret = {"list": list, "total": total}

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_suite_error.value[0],
                           message=MessageEnum.get_suite_error.value[1])


class Getsuitebyproj(MethodView):
    @login_required
    def get(self):
        try:
            project_id = request.args.get('project_id')
            page_index = int(request.args.get('page_index') or 1)
            page_number = int(request.args.get('page_number') or 10)

            if not project_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            suites_pagination = TestSuite.query.filter_by(project=project_id, status=1).paginate(page_index,
                                                                                                 page_number, False)
            suites_total = TestSuite.query.filter_by(project=project_id, status=1).count()
            suites = suites_pagination.items
            total = suites_total

            all_case_ids = []
            for suite in suites:
                all_case_ids.extend(json.loads(suite.caseids))

            interface_cases = InterfaceCase.query.filter(InterfaceCase.case_id.in_(all_case_ids)).all()
            interface_cases_dict = {case.case_id: case for case in interface_cases}

            project = Project.query.filter_by(id=project_id).first()

            list = []
            for suite in suites:
                caseinfos = []
                for case_id in json.loads(suite.caseids):
                    case = interface_cases_dict.get(case_id)
                    if case:
                        caseinfos.append({'case_id': case.case_id, 'desc': case.desc})

                suiteinfo = {
                    'suite_id': suite.id,
                    'name': suite.name,
                    'caseinfos': caseinfos,
                    'project_name': project.project_name,
                    'creator_name': suite.users.username
                }
                list.append(suiteinfo)

            ret = {"list": list, "total": total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_suite_error.value[0],
                           message=MessageEnum.get_suite_error.value[1])


class Updatesuite(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('suite_id') or not data.get('suite_name') or not data.get('case_ids') or not data.get(
                    'project_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            suite = TestSuite.query.filter_by(id=data.get('suite_id')).first()
            if not suite:
                return reponse(code=MessageEnum.suite_not_exict.value[0],
                               message=MessageEnum.suite_not_exict.value[1])
            suite.name = data.get('suite_name')
            suite.caseids = json.dumps(data.get('case_ids'))
            suite.project = data.get('project_id')
            try:
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.update_suite_error.value[0],
                               message=MessageEnum.update_suite_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.update_suite_error.value[0],
                           message=MessageEnum.update_suite_error.value[1])


class Deletesuite(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('suite_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            suite = TestSuite.query.filter_by(id=data.get('suite_id')).first()
            if not suite:
                return reponse(code=MessageEnum.suite_not_exict.value[0],
                               message=MessageEnum.suite_not_exict.value[1])
            suite.status = 0
            try:
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.delete_suite_error.value[0],
                               message=MessageEnum.delete_suite_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.delete_suite_error.value[0],
                           message=MessageEnum.delete_suite_error.value[1])


class Exemult(MethodView):

    @login_required
    def post(self):
        try:
            start_time = time.time()
            data = request.get_json()
            if not data.get('suite_id') and not data.get('env_id') and not data.get('model_id') and not data.get(
                    'project_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            caseinfos = []
            collections_name = ''
            if data.get('suite_id'):  # 执行测试套件
                suite = TestSuite.query.filter_by(id=data.get('suite_id')).first()
                collections_name = suite.name
                if not suite:
                    return reponse(code=MessageEnum.suite_not_exict.value[0],
                                   message=MessageEnum.suite_not_exict.value[1])
                caseids = json.loads(suite.caseids)

                for i in caseids:
                    i = InterfaceCase.query.filter_by(case_id=i).first()
                    if i.status == 1:
                        case_info = {'case_id': i.case_id, 'case_raw': i.raw}
                        caseinfos.append(case_info)
            elif data.get('model_id'):  # 按模块执行
                caselist = InterfaceCase.query.filter_by(model_id=data.get('model_id')).filter_by(status=1).all()
                collections_name = Model.query.filter_by(id=data.get('model_id')).first().model_name
                for i in caselist:
                    case_info = {'case_id': i.case_id, 'case_raw': i.raw}
                    caseinfos.append(case_info)
            elif data.get('project_id'):  # 按项目执行
                caselist = InterfaceCase.query.filter_by(project_id=data.get('project_id')).filter_by(status=1).all()
                for i in caselist:
                    case_info = {'case_id': i.case_id, 'case_raw': i.raw}
                    caseinfos.append(case_info)
            else:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            env = Environment.query.filter_by(id=data.get('env_id')).first()
            if env.protocol == 'http':
                flag = True
                exe_res = []
                for case in caseinfos:
                    caseinfo = InterfaceCase.query.filter_by(case_id=case['case_id']).first()
                    isPass = True
                    assertinfo = {}
                    executehandler = ExecuteHandler(case['case_id'], env.id)
                    res = executehandler.exesinglecase(case_id=case['case_id'], env_id=env.id)
                    if json.loads(res[0])['result'] != '断言通过':
                        isPass = False
                        flag = False
                    assertinfo['case_name'] = caseinfo.desc
                    assertinfo['is_pass'] = isPass
                    assertinfo['rsp'] = res[1]
                    assertinfo['exe_desc'] = res[0]
                    exe_res.append(assertinfo)
                ret = {'collections_name': collections_name, 'is_pass': flag, 'result': exe_res}
                if flag:
                    return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                                   data=ret)
                else:
                    return reponse(code=MessageEnum.assert_error.value[0], message=MessageEnum.assert_error.value[1],
                                   data=ret)

            result_queue = multiprocessing.Queue()
            process = multiprocessing.Process(
                target=self.run_in_new_process_multproto,
                args=(data, caseinfos, result_queue)
            )

            process.start()
            process.join()

            res = result_queue.get()
            end_time = time.time()
            if isinstance(res, tuple):
                case_name = InterfaceCase.query.filter_by(case_id=res[0]).first().desc
                ret = {'error_caseid': res[0], 'error_casename': case_name, 'error_info': format(res[1])}
                return reponse(code=MessageEnum.excute_proto_terminal.value[0],
                               message=MessageEnum.excute_proto_terminal.value[1], data=ret)
            elif isinstance(res, Exception):
                ret = {'error_info': format(res)}
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1], data=ret)

            try:
                flag = True
                for i in res:
                    caseid = i.get('case_id')
                    rsp = i.get('exe_rsp')
                    assertdesc = InterfaceCaseAssert.query.filter_by(case_id=caseid).first()
                    assert_info = {}
                    if assertdesc is not None:
                        temp = rsp
                        if '.' in assertdesc.expression:
                            for j in assertdesc.expression.split('.'):
                                temp = temp[j]
                        else:
                            temp = temp[assertdesc.expression]
                        if isinstance(temp, bool):
                            temp = str(temp).lower()
                        else:
                            temp = str(temp)
                        if temp == assertdesc.excepted_result:
                            isPass = True
                        else:
                            isPass = False
                            flag = False
                        assert_info = {'case_id': caseid, 'is_pass': isPass, 'except': assertdesc.excepted_result,
                                       'actual': temp, 'assert_desc': assertdesc.assert_name,
                                       'expression': assertdesc.expression}

                    i['assert_info'] = assert_info
                    testres = TestcaseResult(
                        case_id=caseid,
                        result=str(rsp),
                        ispass=flag,
                        date=datetime.now(),
                        spend=str("{:.2f}".format(end_time - start_time)),
                        testevent_id=data.get('env_id')
                    )
                    db.session.add(testres)
                db.session.commit()
                if flag:
                    return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                                   data=res)
                else:
                    return reponse(code=MessageEnum.assert_error.value[0], message=MessageEnum.assert_error.value[1],
                                   data=res)
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.unexpected_error.value[0],
                           message=MessageEnum.unexpected_error.value[1])

    def run_in_new_process_multproto(self, data, caseinfos, result_queue):
        try:
            logger.info('当前进程号：{}'.format(os.getpid()))
            # Redirect standard input/output/error to /dev/null
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            res = exemulproto(env_id=data.get('env_id'), caseinfos=caseinfos, is_skip=data.get('is_skip'))

            result_queue.put(res)

        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(e)
        finally:
            sys.exit(0)


def exemulproto(env_id, caseinfos, is_skip):
    try:
        logger.info('执行请求方法exeproto的进程号：{}'.format(os.getpid()))
        source = json.loads(caseinfos[0]['case_raw'])['source']
        branch_name = json.loads(caseinfos[0]['case_raw'])['branch_name']
        proto_path = PROJECT_ROOT + ("/proto/" if source in ('kk', None) else "/proto/pp/") + branch_name

        env = Environment.query.filter_by(id=env_id).first()
        host, port = env.url, env.port

        sys.path.append(proto_path)
        uid = json.loads(caseinfos[0]['case_raw'])['uid']
        player = Player(uid, host, port)
        player.client = client = Client(host=host, port=port) if not player.client else player.client

        for name in os.listdir(proto_path):
            if name == '__init__.py' or not name.endswith('.py'):
                continue
            module = importlib.import_module(
                f"proto.{branch_name}.{name[:-3]}" if source in ('kk', None) else f"proto.pp.{branch_name}.{name[:-3]}")
            for item in dir(module):
                player.client.pb[item] = getattr(module, item)

        if source in ('kk', None):
            player = player.login_by_uid(uid)[1]
        else:
            player = player.login_by_uid_pp(uid)[1]

        reslut = []
        for i in caseinfos:
            r = {'case_id': i['case_id']}
            params = json.loads(i['case_raw'])['proto_content']
            reqmessage = json.loads(i['case_raw'])['req_message_name']
            rspmessage = reqmessage[:-3] + "RSP"
            try:
                client.send(reqmessage, params)
                msg = client.recv(rspmessage)
                r['exe_res'] = True
                r['exe_rsp'] = msg.body
            except Exception as e:
                logger.error(f"Error processing case {i['case_id']}: {e}")
                logger.error(traceback.format_exc())
                r['exe_res'] = False
                r['exe_rep'] = f"Error: {e}"
                if str(is_skip) == False:
                    raise e
            reslut.append(r)

        client.stop()
        logger.info('reslut is {}', reslut)
        return reslut
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e
    finally:
        client.stop() if 'client' in locals() else None


class Getallbrmes(MethodView):
    @login_required
    def get(self):
        try:
            logger.info('主进程号：{}'.format(os.getpid()))
            branch_name = request.args.get('branch_name')
            source = request.args.get('source')
            if not branch_name:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if '/' in branch_name:
                branch_name = branch_name.replace('/', '_')
            if source == 'kk' or source is None:
                proto_path = PROJECT_ROOT + "/proto/" + branch_name
            else:
                proto_path = PROJECT_ROOT + "/proto/pp/" + branch_name

            result_queue = multiprocessing.Queue()
            process = multiprocessing.Process(
                target=self.run_in_new_process_getallbrmes,
                args=(proto_path, result_queue)
            )
            process.start()
            process.join()
            res = result_queue.get()
            if res:
                ret = {"list": res, "total": len(res)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_proto_error.value[0], message=MessageEnum.get_proto_error.value[1])

    def run_in_new_process_getallbrmes(self, proto_path, result_queue):
        try:
            logger.info('当前进程号，执行获取分支内所有message：{}'.format(os.getpid()))
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            res = getallbrmes(proto_path)
            result_queue.put(res)
        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(None)
        finally:
            sys.exit(0)


def getallbrmes(proto_path):
    try:
        os.chdir(proto_path)
        sys.path.append(proto_path)

        for file_name in os.listdir(proto_path):
            if file_name.endswith(".py") and file_name != "__init__.py":
                module_name = os.path.splitext(file_name)[0]
                importlib.import_module(module_name)

        messages = []
        for module_name in sys.modules:
            if module_name.endswith("_pb2"):
                module = sys.modules[module_name]
                if hasattr(module, "DESCRIPTOR"):
                    file_descriptor = getattr(module, "DESCRIPTOR")
                    for message in file_descriptor.message_types_by_name:
                        if message.endswith("REQ"):
                            messages.append(message)
        return messages
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


class Autogencase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('attributes'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if len(data.get('attributes')) <= 1:
                return reponse(code=MessageEnum.auto_less_parameter.value[0],
                               message=MessageEnum.auto_less_parameter.value[1])
            testcase_params = generate_test_cases(data.get('attributes'))
            logger.info('测试用的用例列表是： {}', testcase_params)
            ret = {'auto_cases': testcase_params}
            if testcase_params:
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                               data=ret)
            else:
                return reponse(code=MessageEnum.auto_gen_case_error.value[0],
                               message=MessageEnum.auto_gen_case_error.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.auto_gen_case_error.value[0],
                           message=MessageEnum.auto_gen_case_error.value[1])


class Saveautocases(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('env_id') or not data.get('project_id') or not data.get('model_id') or not data.get(
                    'case_desc') or not data.get('branch_name') or not data.get('req_message_name') or not data.get(
                'source') or not data.get('uid') or not data.get('auto_cases'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            interfacecases = []

            n = len(data.get('auto_cases'))

            for i in range(n):
                interfacecase = InterfaceCase()
                interfacecase.project_id = data.get('project_id')
                interfacecase.model_id = data.get('model_id')
                interfacecase.desc = data.get('case_desc') + str(i)
                interfacecase.case_protocol = 2
                interfacecase.is_relycase = 0
                interfacecase.rely_dbf = 0
                interfacecase.socketreq = data.get('req_message_name')
                interfacecase.raw = json.dumps({"proto_content": data.get('auto_cases')[i], "uid": data.get('uid'),
                                                "branch_name": data.get('branch_name'), "source": data.get('source'),
                                                "env_id": data.get('env_id'), "project_id": data.get('project_id'),
                                                "model_id": data.get('model_id'),
                                                "req_message_name": data.get('req_message_name')})
                interfacecase.creater = current_user.user_id
                interfacecase.source = 1
                interfacecases.append(interfacecase)

            try:
                db.session.add_all(interfacecases)
                db.session.commit()
                caseids = []
                for i in interfacecases:
                    caseids.append(i.case_id)
                ret = {'caseids': caseids, 'total': len(caseids)}
                testsuite = TestSuite()
                testsuite.name = data.get('case_desc') + 'test_suite'
                testsuite.caseids = json.dumps(caseids)
                testsuite.creator = current_user.user_id
                testsuite.project = data.get('project_id')
                testsuite.status = 1
                db.session.add(testsuite)
                db.session.commit()

                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.add_case_erro.value[0],
                               message=MessageEnum.add_case_erro.value[1])


        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.add_case_erro.value[0],
                           message=MessageEnum.add_case_erro.value[1])


class Batchdelcase(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('case_ids'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            caseids = data.get('case_ids')
            for i in caseids:
                case = InterfaceCase.query.filter_by(case_id=i).first()
                case.status = 0
            try:
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                return reponse(code=MessageEnum.delete_case_error.value[0],
                               message=MessageEnum.delete_case_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.delete_case_error.value[0],
                           message=MessageEnum.delete_case_error.value[1])


class Testreport(MethodView):

    @login_required
    def get(self):
        try:
            if not any([request.args.get('model_id'), request.args.get('project_id')]):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            start_time = request.args.get('start_time')
            end_time = request.args.get('end_time')
            model_id = request.args.get('model_id')
            project_id = request.args.get('project_id')

            gross_caselist = TestcaseResult.query.filter(
                TestcaseResult.date.between(start_time, end_time)).with_entities(
                TestcaseResult.case_id).distinct().all()
            case_list = [case.case_id for case in gross_caselist]

            logger.info('gross_caselist is {}', case_list)
            filtered_cases = []

            if model_id:
                filtered_case_ids = [
                    i for i in case_list
                    if InterfaceCase.query.filter_by(case_id=i, model_id=model_id).first()
                ]
                filtered_cases.extend(filtered_case_ids)
            else:
                filtered_case_ids = [
                    i for i in case_list
                    if InterfaceCase.query.filter_by(case_id=i, project_id=project_id).first()
                ]
                filtered_cases.extend(filtered_case_ids)

            case_list = filtered_cases

            logger.info('after deal case_list is {}', case_list)
            if not case_list:
                return reponse(code=MessageEnum.no_report_here.value[0],
                               message=MessageEnum.no_report_here.value[1])

            total = TestcaseResult.query.filter(TestcaseResult.case_id.in_(case_list)).filter(
                TestcaseResult.date.between(start_time, end_time)).count()
            passnum = TestcaseResult.query.filter(TestcaseResult.case_id.in_(case_list)).filter(
                TestcaseResult.date.between(start_time, end_time), TestcaseResult.ispass == True).count()
            failnum = TestcaseResult.query.filter(TestcaseResult.case_id.in_(case_list)).filter(
                TestcaseResult.date.between(start_time, end_time), TestcaseResult.ispass == False).count()
            passrate = round(passnum / total, 4) if total != 0 else 0
            passrate_percentage = "{:.2%}".format(passrate)
            failrate = round(failnum / total, 4) if total != 0 else 0
            failrate_percentage = "{:.2%}".format(failrate)
            ret = {'total': total, 'passnum': passnum, 'failnum': failnum, 'passrate': passrate_percentage,
                   'failrate': failrate_percentage}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_report_error.value[0],
                           message=MessageEnum.get_report_error.value[1])


class Reportlist(MethodView):

    @login_required
    def get(self):
        try:
            start_time = request.args.get('start_time')
            end_time = request.args.get('end_time')
            model_id = request.args.get('model_id')
            project_id = request.args.get('project_id')
            case_id = request.args.get('case_id')
            test_res = request.args.get('test_res')
            page_number = int(request.args.get('page_number', 10))
            page_index = int(request.args.get('page_index', 1))

            # 获取所有满足时间范围的 case_id
            gross_caselist = TestcaseResult.query.filter(
                TestcaseResult.date.between(start_time, end_time)
            ).with_entities(TestcaseResult.case_id).distinct().all()
            case_list = [case.case_id for case in gross_caselist]

            if model_id:
                filtered_case_ids = InterfaceCase.query.filter(
                    InterfaceCase.case_id.in_(case_list),
                    InterfaceCase.model_id == model_id
                ).with_entities(InterfaceCase.case_id).all()
            else:
                filtered_case_ids = InterfaceCase.query.filter(
                    InterfaceCase.case_id.in_(case_list),
                    InterfaceCase.project_id == project_id
                ).with_entities(InterfaceCase.case_id).all()

            case_list = [case.case_id for case in filtered_case_ids]

            if not case_list:
                return reponse(code=MessageEnum.no_report_here.value[0],
                               message=MessageEnum.no_report_here.value[1])

            # 根据 case_list 和时间范围过滤 TestcaseResult
            query = TestcaseResult.query.filter(
                TestcaseResult.case_id.in_(case_list),
                TestcaseResult.date.between(start_time, end_time)
            )

            stats = {}
            if case_id and test_res:
                query = query.filter(TestcaseResult.case_id == case_id)
                query = query.filter(TestcaseResult.ispass == (test_res.lower() == 'true'))
            elif case_id:
                query = query.filter(TestcaseResult.case_id == case_id)
                total_count = query.count()
                pass_count = query.filter(TestcaseResult.ispass == True).count()
                fail_count = query.filter(TestcaseResult.ispass == False).count()
                stats = {
                    'total_count': total_count,
                    'pass_count': pass_count,
                    'fail_count': fail_count
                }
            else:
                query = query.filter(TestcaseResult.ispass == (test_res.lower() == 'true'))

            # 分页查询
            total = query.count()
            total_res = query.offset((page_index - 1) * page_number).limit(page_number).all()

            # 获取所有必要的 InterfaceCase 数据
            case_ids = [res.case_id for res in total_res]
            cases = InterfaceCase.query.filter(InterfaceCase.case_id.in_(case_ids)).all()
            case_map = {case.case_id: case for case in cases}

            # 构建返回结果
            ret = [
                {
                    'case_id': res.case_id,
                    'case_desc': case_map[res.case_id].desc,
                    'is_pass': res.ispass,
                    'spend': res.spend,
                    'detail': res.result,
                    'exe_time': str(res.date)
                }
                for res in total_res
            ]

            response = {
                'total': total,
                'page_number': page_number,
                'page_index': page_index,
                'reslist': ret
            }

            if stats:
                response.update({'stats': stats})

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=response)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_report_error.value[0],
                           message=MessageEnum.get_report_error.value[1])
