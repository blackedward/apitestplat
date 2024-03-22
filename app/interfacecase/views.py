import importlib
import json
import multiprocessing
import os
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


# class ExecuteCase(MethodView):
#
#     @login_required
#     def post(self):
#         try:
#             logger.info('当前进程号：{}'.format(os.getpid()))
#             data = request.get_json()
#             if not data:
#                 return reponse(code=MessageEnum.must_be_every_parame.value[0],
#                                message=MessageEnum.must_be_every_parame.value[1])
#             case_id = data.get('case_id')
#             env_id = data.get('env_id')
#             if not case_id or not env_id:
#                 return reponse(code=MessageEnum.must_be_every_parame.value[0],
#                                message=MessageEnum.must_be_every_parame.value[1])
#
#             case = InterfaceCase.query.filter_by(case_id=case_id).first()
#             if not case:
#                 return reponse(code=MessageEnum.case_edit_error.value[0],
#                                message=MessageEnum.case_edit_error.value[1])
#
#             if case.case_protocol == 2:
#                 return self.execute_proto_case(data, case)
#             else:
#                 return self.execute_normal_case(data, case, env_id)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             return reponse(code=MessageEnum.test_error.value[0],
#                            message=MessageEnum.test_error.value[1])
#
#     def execute_proto_case(self, data, case):
#         try:
#             start_time = time.time()
#             logger.info('开始执行proto协议用例')
#             case_raw = json.loads(case.raw)
#             env_id = data.get('env_id', case_raw.get('env_id'))
#             result_queue = multiprocessing.Queue()
#
#             process = multiprocessing.Process(
#                 target=self.run_proto_case,
#                 args=(data, case_raw, env_id, result_queue)
#             )
#
#             process.start()
#             process.join()
#
#             res = result_queue.get()
#             isPass = isinstance(res, Exception)
#
#             end_time = time.time()
#             spend_time = end_time - start_time
#
#             new_case = TestcaseResult(
#                 result=str(res),
#                 case_id=case.case_id,
#                 ispass=isPass,
#                 testevent_id=env_id,
#                 spend=str("{:.2f}".format(spend_time)),
#                 date=datetime.now()
#             )
#             db.session.add(new_case)
#
#             db.session.commit()
#             return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             db.session.rollback()
#             return reponse(code=MessageEnum.execute_proto_error.value[0],
#                            message=MessageEnum.execute_proto_error.value[1])
#
#     def execute_normal_case(self, data, case, env_id):
#         try:
#             executehandler = ExecuteHandler(case.case_id, env_id)
#             res = executehandler.exemulticase(case_id=case.case_id, env_id=env_id)[0]
#             logger.info(res)
#             result_data = json.loads(res)
#             if result_data['result'] == '断言通过':
#                 return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
#                                data=result_data)
#             elif result_data['result'] == '断言失败':
#                 return reponse(code=MessageEnum.assert_fail.value[0], message=MessageEnum.assert_fail.value[1],
#                                data=result_data)
#             else:
#                 return reponse(code=MessageEnum.test_error.value[0], message=MessageEnum.test_error.value[1],
#                                data=result_data)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             return reponse(code=MessageEnum.test_error.value[0],
#                            message=MessageEnum.test_error.value[1])
#
#     def run_proto_case(self, data, case_raw, env_id, result_queue):
#         try:
#             logger.info('当前进程号：{}'.format(os.getpid()))
#             if not env_id:
#                 env_id = case_raw.get('env_id')
#
#             sys.stdin = open(os.devnull, 'r')
#             sys.stdout = open(os.devnull, 'w')
#             sys.stderr = open(os.devnull, 'w')
#
#             res = exeproto(
#                 uid=case_raw['uid'],
#                 env_id=env_id,
#                 branch_name=case_raw['branch_name'],
#                 reqmessage=case_raw['req_message_name'],
#                 params=case_raw['proto_content'],
#                 source=case_raw['source']
#             )
#
#             result_queue.put(res)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             result_queue.put(e)
#         finally:
#             sys.exit(0)


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
            if not case_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if not env_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            case = InterfaceCase.query.filter_by(case_id=case_id).first()
            if case.case_protocol == 2:
                start_time = time.time()
                logger.info('开始执行proto协议用例')
                case_raw = json.loads(case.raw)
                # 使用 multiprocessing Queue 来通信结果
                result_queue = multiprocessing.Queue()

                # 使用 multiprocessing 在新进程中运行函数
                process = multiprocessing.Process(
                    target=self.run_proto_case,
                    args=(data, case_raw, case_raw['branch_name'], case_raw['proto_content'], case_raw['source'],
                          result_queue)
                )

                process.start()
                process.join()

                # 从队列中获取结果
                res = result_queue.get()
                if isinstance(res, Exception):
                    isPass = False
                else:
                    isPass = True
                end_time = time.time()
                spend_time = end_time - start_time

                new_case = TestcaseResult(result=str(res),
                                          case_id=case_id,
                                          ispass=isPass, testevent_id=env_id, spend=str(int(spend_time)),
                                          date=datetime.now())
                db.session.add(new_case)
                try:
                    db.session.commit()
                    return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)
                except Exception as e:
                    db.session.rollback()
                    logger.info('用例：%s保存测试结果失败!原因：%s' % (case_id, e))
                    return reponse(code=MessageEnum.execute_proto_error.value[0],
                                   message=MessageEnum.execute_proto_error.value[1])

            executehandler = ExecuteHandler(case_id, env_id)
            if case.is_relycase == 1:
                res = executehandler.exemulticase(case_id=case_id, env_id=env_id)[0]
            else:
                res = executehandler.exesinglecase(case_id=case_id, env_id=env_id)[0]
            logger.info(res)
            if eval(res)['result'] == '断言通过':
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                               data=json.loads(res))
            elif eval(res)['result'] == '断言失败':
                return reponse(code=MessageEnum.assert_fail.value[0], message=MessageEnum.assert_fail.value[1],
                               data=json.loads(res))
            else:
                return reponse(code=MessageEnum.test_error.value[0], message=MessageEnum.test_error.value[1],
                               data=json.loads(res))

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.test_error.value[0],
                           message=MessageEnum.test_error.value[1])

    def run_proto_case(self, data, case_raw, branch_name, params, source, result_queue):
        try:
            logger.info('当前进程号：{}'.format(os.getpid()))
            if not data.get('env_id'):
                envid = case_raw['env_id']
            else:
                envid = data.get('env_id')
            # 重定向标准输入/输出/错误到 /dev/null
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            res = exeproto(uid=case_raw['uid'], env_id=envid, branch_name=branch_name,
                           reqmessage=case_raw['req_message_name'], params=params, source=source)

            # 将结果放入队列
            result_queue.put(res)

        except Exception as e:
            logger.error(traceback.format_exc())
            # 如果发生异常，则将 None 放入队列
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
                if data.get('requestinfo')['headers']:
                    requestheaders = json.loads(data.get('requestinfo')['headers'])
                    for i in requestheaders:
                        headers[i['name']] = i['value']
                interfacecase.headers = json.dumps(headers)
                params = {}
                if data.get('requestinfo')['params']:
                    requestparams = json.loads(data.get('requestinfo')['params'])
                    for i in requestparams:
                        params[i['name']] = i['value']
                interfacecase.params = json.dumps(params)
                # interfacecase.form_data_encoded = data.get('requestinfo')['form_data_encoded']
                # interfacecase.form_data = data.get('requestinfo')['form_data']
                interfacecase.socketreq = data.get('requestinfo')['socketreq']
                interfacecase.socketrsp = data.get('requestinfo')['socketrsp']
                interfacecase.raw = data.get('requestinfo')['raw']
                # interfacecase.raw_type = data.get('requestinfo')['raw_type']
                # interfacecase.body_type = data.get('requestinfo')['body_type']
                interfacecase.creater = current_user.user_id
                # interfacecase.created_time = data.get('basicinfo')['created_time'] if data.get('basicinfo')[
                #     'created_time'] else datetime.datetime.now()
                # interfacecase.update_time = data.get('basicinfo')['update_time'] if data.get('basicinfo')[
                #     'update_time'] else datetime.datetime.now()
                interfacecase.source = 0
                # interfacecase.import_no = data.get('basicinfo')['import_no']

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

            olddata = Precase.query.filter_by(parent_case_id=data.get('caseid')).all()
            oldprecaseid = []
            if olddata:
                for i in olddata:
                    oldprecaseid.append(i.pre_case_id)
            newdata = data.get('precases')
            if not newdata or len(newdata) == 0:
                interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()
                interfacecase.is_relycase = 0
                interfacecase.update_time = datetime.now()
                try:
                    db.session.commit()
                except Exception as e:
                    logger.error(traceback.format_exc())
                    db.session.rollback()
                    return reponse(code=MessageEnum.update_pre_case_error.value[0],
                                   message=MessageEnum.update_pre_case_error.value[1])

                for j in oldprecaseid:
                    logger.info('old precaseid:{} not in newprecases', j)
                    pre_case = Precase.query.filter_by(parent_case_id=data.get('caseid'),
                                                       pre_case_id=j).first()
                    pre_case.status = 0
                    pre_case.update_time = datetime.now()
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        db.session.rollback()
                        return reponse(code=MessageEnum.update_pre_case_error.value[0],
                                       message=MessageEnum.update_pre_case_error.value[1])
                return reponse(code=MessageEnum.successs.value[0],
                               message=MessageEnum.successs.value[1])
            for i in newdata:
                interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()
                interfacecase.is_relycase = 1
                interfacecase.update_time = datetime.now()
                try:
                    db.session.commit()
                except Exception as e:
                    logger.error(traceback.format_exc())
                    db.session.rollback()
                    return reponse(code=MessageEnum.update_pre_case_error.value[0],
                                   message=MessageEnum.update_pre_case_error.value[1])
                if i.get('pre_case_id') in oldprecaseid:
                    logger.info('precaseid:{} in oldprecases', i.get('pre_case_id'))
                    pre_case = Precase.query.filter_by(parent_case_id=data.get('caseid'),
                                                       pre_case_id=i.get('pre_case_id')).first()
                    pre_case.extract_expression = i.get('exp')
                    pre_case.order = i.get('sort_id')
                    pre_case.status = 1
                    pre_case.update_time = datetime.now()
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        db.session.rollback()
                        return reponse(code=MessageEnum.update_pre_case_error.value[0],
                                       message=MessageEnum.update_pre_case_error.value[1])
                else:
                    logger.info('precaseid:{} not in oldprecases', i.get('pre_case_id'))
                    pre_case = Precase()
                    pre_case.parent_case_id = data.get('caseid')
                    pre_case.extract_expression = i.get('exp')
                    pre_case.pre_case_id = i.get('pre_case_id')
                    pre_case.order = i.get('sort_id')
                    pre_case.status = 1
                    pre_case.update_time = datetime.now()
                    try:
                        db.session.add(pre_case)
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        db.session.rollback()
                        return reponse(code=MessageEnum.update_pre_case_error.value[0],
                                       message=MessageEnum.update_pre_case_error.value[1])
            for j in oldprecaseid:
                if not any(j == d.get('pre_case_id') for d in data.get('precases')):
                    logger.info('old precaseid:{} not in newprecases', j)
                    pre_case = Precase.query.filter_by(parent_case_id=data.get('caseid'),
                                                       pre_case_id=j).first()
                    pre_case.status = 0
                    pre_case.update_time = datetime.now()
                    try:
                        db.session.commit()
                    except Exception as e:
                        logger.error(traceback.format_exc())
                        db.session.rollback()
                        return reponse(code=MessageEnum.update_pre_case_error.value[0],
                                       message=MessageEnum.update_pre_case_error.value[1])
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
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
            interfacecase.headers = self._parse_json(requestinfo.get('headers'))
            interfacecase.params = self._parse_json(requestinfo.get('params'))

            interfacecase.socketreq = requestinfo.get('socketreq')
            interfacecase.socketrsp = requestinfo.get('socketrsp')
            if interfacecase.case_protocol == 2:
                raw_data = json.loads(interfacecase.raw) if interfacecase.raw else {}
                raw_data['proto_content'] = requestinfo.get('raw')
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

            headers = [{'name': k, 'value': v} for k, v in json.loads(interfacecase.headers).items()] \
                if interfacecase.headers else []

            params = [{'name': k, 'value': v} for k, v in json.loads(interfacecase.params).items()] \
                if interfacecase.params else []

            if interfacecase.case_protocol == 2:
                raw = json.loads(interfacecase.raw)['proto_content']
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
        logger.info(file_descriptor)
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
            proto_name = request.args.get('proto_name')
            message_name = request.args.get('message_name')
            source = request.args.get('source')

            if not branch_name or not proto_name or not message_name:
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
        logger.info('recv message:{}', msg.body)
        client.stop()
        client = None
        return msg.body
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


# class Executeproto(MethodView):
#     @login_required
#     def post(self):
#         try:
#             logger.info('主进程号：{}'.format(os.getpid()))
#             data = request.get_json()
#             if not data.get('proto_name') or not data.get('req_message_name') or not data.get('env_id') or not data.get(
#                     'uid') or not data.get('branch_name') or not data.get('source'):
#                 return reponse(code=MessageEnum.must_be_every_parame.value[0],
#                                message=MessageEnum.must_be_every_parame.value[1])
#             branch_name = data.get('branch_name')
#             source = data.get('source')
#             if '/' in branch_name:
#                 branch_name = branch_name.replace('/', '_')
#             if not data.get('proto_content') or data.get('proto_content') is None:
#                 params = {}
#             else:
#                 params = data.get('proto_content')
#
#             # Use multiprocessing Queue to communicate results
#             result_queue = multiprocessing.Queue()
#
#             # Use multiprocessing to run the function in a new process
#             process = multiprocessing.Process(
#                 target=self.run_in_new_process,
#                 args=(data, branch_name, params, source, result_queue)
#             )
#
#             process.start()
#             process.join()
#
#             # Retrieve results from the Queue
#
#             res = result_queue.get()
#             if isinstance(res, Exception):
#                 # If res is an exception, handle it accordingly
#                 if isinstance(res, TimeOutException):
#                     rstr = '执行超时了，请确认目标服务器的处理情况'
#                     return reponse(code=MessageEnum.execute_timeout.value[0],
#                                    message=MessageEnum.execute_timeout.value[1], data=rstr)
#                 return reponse(code=MessageEnum.execute_proto_error.value[0],
#                                message=MessageEnum.execute_proto_error.value[1], data=format(res))
#
#             assert_info = data.get('assert_info')
#             temp = res
#             if not assert_info:
#                 return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)
#             else:
#                 expected = assert_info.get('excepted_result')
#                 expression = assert_info.get('expression')
#
#                 if '.' in expression:
#                     for i in expression.split('.'):
#                         temp = temp[i]
#                 else:
#                     temp = temp[expression]
#                 if temp == expected:
#                     assertres = {'excepted_result': expected, 'actual_result': temp}
#                     ret = {'assertres': assertres, 'response': res}
#                     return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
#                 else:
#                     actual = {'excepted_result': expected, 'actual_result': temp}
#                     return reponse(code=MessageEnum.assert_error.value[0], message=MessageEnum.assert_error.value[1],
#                                    data=actual)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             return reponse(code=MessageEnum.execute_proto_error.value[0],
#                            message=MessageEnum.execute_proto_error.value[1], data=format(e))
#
#     def run_in_new_process(self, data, branch_name, params, source, result_queue):
#         try:
#             logger.info('当前进程号：{}'.format(os.getpid()))
#             # Redirect standard input/output/error to /dev/null
#             sys.stdin = open(os.devnull, 'r')
#             sys.stdout = open(os.devnull, 'w')
#             sys.stderr = open(os.devnull, 'w')
#             res = exeproto(uid=data.get('uid'), env_id=data.get('env_id'), branch_name=branch_name,
#                            reqmessage=data.get('req_message_name'), params=params, source=source)
#
#             result_queue.put(res)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             result_queue.put(e)
#         finally:
#             sys.exit(0)
class Executeproto(MethodView):
    @login_required
    def post(self):
        try:
            logger.info('主进程号：{}'.format(os.getpid()))
            data = request.get_json()
            required_params = ['proto_name', 'req_message_name', 'env_id', 'uid', 'branch_name', 'source']
            if not all(data.get(param) for param in required_params):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            branch_name = data.get('branch_name').replace('/', '_')
            params = data.get('proto_content', {})

            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process,
                args=(data, branch_name, params, result_queue)
            )

            process.start()
            process.join()

            # Retrieve results from the Queue
            res = result_queue.get()
            if isinstance(res, Exception):
                if isinstance(res, TimeOutException):
                    rstr = '执行超时了，请确认目标服务器的处理情况'
                    return reponse(code=MessageEnum.execute_timeout.value[0],
                                   message=MessageEnum.execute_timeout.value[1], data=rstr)
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1], data=format(res))

            assert_info = data.get('assert_info')
            if assert_info:
                expected = assert_info.get('excepted_result')
                expression = assert_info.get('expression')

                temp = res
                if '.' in expression:
                    for i in expression.split('.'):
                        temp = temp.get(i)
                else:
                    temp = temp.get(expression)

                if temp == expected:
                    assertres = {'excepted_result': expected, 'actual_result': temp}
                    ret = {'assertres': assertres, 'response': res}
                    return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
                else:
                    actual = {'excepted_result': expected, 'actual_result': temp}
                    return reponse(code=MessageEnum.assert_error.value[0], message=MessageEnum.assert_error.value[1],
                                   data=actual)
            else:
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.execute_proto_error.value[0],
                           message=MessageEnum.execute_proto_error.value[1], data=format(e))

    def run_in_new_process(self, data, branch_name, params, result_queue):
        try:
            logger.info('当前进程号：{}'.format(os.getpid()))
            # Redirect standard input/output/error to /dev/null
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            res = exeproto(uid=data.get('uid'), env_id=data.get('env_id'), branch_name=branch_name,
                           reqmessage=data.get('req_message_name'), params=params, source=data.get('source'))

            result_queue.put(res)

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
            if not data.get('proto_name') or not data.get(
                    'req_message_name') or not data.get('env_id') or not data.get('uid') or not data.get(
                'case_desc') or not data.get('project_id') or not data.get('model_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            if not data["proto_content"]:
                data["proto_content"] = {}

            interfacecase = InterfaceCase()
            interfacecase.project_id = data.get('project_id')
            interfacecase.model_id = data.get('model_id')
            interfacecase.desc = data.get('case_desc')
            interfacecase.case_protocol = 2
            interfacecase.is_relycase = 0
            interfacecase.rely_dbf = 0
            interfacecase.socketreq = data.get('req_message_name')
            interfacecase.raw = json.dumps(data)
            interfacecase.creater = current_user.user_id
            interfacecase.source = 1

            try:
                db.session.add(interfacecase)
                db.session.flush()
                case_id = interfacecase.case_id
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                               data=case_id)
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


class Getsuitebyproj(MethodView):
    @login_required
    def get(self):
        try:
            project_id = request.args.get('project_id')
            if not project_id:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            suites = TestSuite.query.filter_by(project=project_id, status=1).all()
            if not suites:
                return reponse(code=MessageEnum.get_suite_error.value[0],
                               message=MessageEnum.get_suite_error.value[1])
            project = Project.query.filter_by(id=project_id).first()
            ret = []
            for i in suites:
                projectname = project.project_name

                creatorname = User.query.filter_by(user_id=i.creator).first().username
                ret.append({
                    'suite_id': i.id,
                    'name': i.name,
                    'caseids': json.loads(i.caseids),
                    'project_name': projectname,
                    'creator_name': creatorname
                })
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


class Exemulproto(MethodView):

    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('suite_id') and not data.get('env_id') and not data.get('model_id') and not data.get(
                    'project_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            caseinfos = []
            if data.get('suite_id'):  # 执行测试套件
                suite = TestSuite.query.filter_by(id=data.get('suite_id')).first()
                if not suite:
                    return reponse(code=MessageEnum.suite_not_exict.value[0],
                                   message=MessageEnum.suite_not_exict.value[1])
                caseids = json.loads(suite.caseids)

                for i in caseids:
                    i = InterfaceCase.query.filter_by(case_id=i).first()
                    case_info = {'case_id': i.case_id, 'case_raw': i.raw}
                    caseinfos.append(case_info)
            elif data.get('model_id'):  # 按模块执行
                caselist = InterfaceCase.query.filter_by(model_id=data.get('model_id')).filter_by(status=1).all()
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

            logger.info('caseinfos is {}', caseinfos)
            # Use multiprocessing Queue to communicate results
            result_queue = multiprocessing.Queue()

            # Use multiprocessing to run the function in a new process
            process = multiprocessing.Process(
                target=self.run_in_new_process_multproto,
                args=(data, caseinfos, result_queue)
            )

            process.start()
            process.join()

            # Retrieve results from the Queue
            res = result_queue.get()

            if isinstance(res, tuple):
                ret = {'error_caseid': res[0], 'error_info': format(res[1])}
                return reponse(code=MessageEnum.excute_proto_terminal.value[0],
                               message=MessageEnum.excute_proto_terminal.value[1], data=ret)
            elif isinstance(res, Exception):
                ret = {'error_info': format(res)}
                return reponse(code=MessageEnum.execute_proto_error.value[0],
                               message=MessageEnum.execute_proto_error.value[1], data=ret)

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=res)

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
            res = exemulproto(env_id=data.get('env_id'), caseinfos=caseinfos)

            # Put results into the Queue
            result_queue.put(res)

        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(e)
        finally:
            sys.exit(0)


def exemulproto(env_id, caseinfos):
    try:
        logger.info('执行请求方法exeproto的进程号：{}'.format(os.getpid()))
        source = json.loads(caseinfos[0]['case_raw'])['source']
        branch_name = json.loads(caseinfos[0]['case_raw'])['branch_name']
        if source == 'kk' or source is None:
            proto_path = PROJECT_ROOT + "/proto/" + branch_name
        else:
            proto_path = PROJECT_ROOT + "/proto/pp/" + branch_name
        env = Environment.query.filter_by(id=env_id).first()
        host = env.url
        port = env.port

        sys.path.append(proto_path)
        uid = json.loads(caseinfos[0]['case_raw'])['uid']
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

        reslut = []
        for i in caseinfos:
            params = json.loads(i['case_raw'])['proto_content']
            reqmessage = json.loads(i['case_raw'])['req_message_name']
            rspmessage = reqmessage[:-3] + "RSP"
            try:
                client.send(reqmessage, params)
                msg = client.recv(rspmessage)
                r = {i['case_id']: msg.body}
            except Exception as e:
                logger.error(traceback.format_exc())
                return i['case_id'], e
            reslut.append(r)

        client.stop()
        logger.info('reslut is {}', reslut)
        return reslut
    except Exception as e:
        logger.error(traceback.format_exc())
        raise e


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
            logger.info('当前进程号，执行获取分之内所有message：{}'.format(os.getpid()))
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
                interfacecase.desc = data.get('case_desc') + str(i) + ' ' + str(int(time.time()))
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
                testsuite.name = data.get('case_desc') + 'test_suite' + ' ' + str(int(time.time()))
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
