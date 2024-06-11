import importlib
import json
import multiprocessing
import os
import sys
import time
import traceback
from enum import Enum

from flask import Blueprint, typing as ft, render_template, jsonify
from flask import redirect, request, session, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
from gevent import spawn, joinall

from app.models import *
from flask.views import View, MethodView

from common import AssertClass
from common.Client import Client
from common.executehandler import ExecuteHandler
from common.jsontools import reponse
from common.player import Player
from error_message import MessageEnum
from common.log import logger
from sqlalchemy import and_

tasks = Blueprint('tasks', __name__)
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


class RunningStatus(Enum):
    CREATED = 0
    RUNNING = 1
    FINISHED = 2
    FAILED = 3


class Createtask(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('task_content'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            userinfo = User.query.filter_by(user_id=current_user.user_id).first()
            task_content = data.get('task_content')
            suite_id = task_content['suite_id']
            suite = TestSuite.query.filter_by(id=suite_id).first()
            if not suite:
                return reponse(code=MessageEnum.suite_not_exict.value[0],
                               message=MessageEnum.suite_not_exict.value[1])

            task = Task()
            task.name = suite.name + ' ' + userinfo.username + ' ' + datetime.now().strftime('%Y%m%d%H%M%S')
            task.task_content = json.dumps(task_content)
            task.creator = current_user.user_id
            task.product_line = User.query.filter_by(user_id=current_user.user_id).first().pdline
            task.running_status = RunningStatus.CREATED.value
            task.create_time = datetime.now()
            task.status = 1

            try:
                db.session.add(task)
                db.session.commit()
                ret = {'task_id': task.id}
                return reponse(code=MessageEnum.successs.value[0],
                               message=MessageEnum.successs.value[1], data=ret)

            except Exception as e:
                db.session.rollback()
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.task_create_error.value[0],
                               message=MessageEnum.task_create_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.task_create_error.value[0], message=MessageEnum.task_create_error.value[1])


class Taskfilter(MethodView):
    @login_required
    def get(self):
        try:
            # 检查必须的参数
            if not any(
                    [request.args.get('creator_id'), request.args.get('running_status'), request.args.get('start_time'),
                     request.args.get('end_time')]):
                return self.response(MessageEnum.must_be_every_parame.value[0],
                                     MessageEnum.must_be_every_parame.value[1])

            filters = []
            creator = request.args.get('creator_id')
            running_status = request.args.get('running_status')
            start_time = request.args.get('start_time')
            end_time = request.args.get('end_time')
            product_line = User.query.filter_by(user_id=current_user.user_id).first().pdline

            if creator:
                filters.append(Task.creator == creator)
            if running_status:
                filters.append(Task.running_status == running_status)
            filters.append(Task.product_line == product_line)

            if start_time:
                try:
                    start_time_dt = datetime.strptime(start_time, '%Y-%m-%d %H:%M:%S')
                    filters.append(Task.create_time >= start_time_dt)
                except ValueError:
                    return self.response(MessageEnum.invalid_datetime_format.value[0],
                                         'Invalid start_time format, expected YYYY-MM-DD HH:MM:SS')

            if end_time:
                try:
                    end_time_dt = datetime.strptime(end_time, '%Y-%m-%d %H:%M:%S')
                    filters.append(Task.create_time <= end_time_dt)
                except ValueError:
                    return self.response(MessageEnum.invalid_datetime_format.value[0],
                                         'Invalid end_time format, expected YYYY-MM-DD HH:MM:SS')

            page_index = int(request.args.get('page_index', 1))
            page_number = int(request.args.get('page_number', 10))

            try:
                tasks_query = Task.query.filter(and_(*filters))
                paginated_tasks = tasks_query.paginate(page=page_index, per_page=page_number, error_out=False)
                tasks = paginated_tasks.items

                ret = []
                for task in tasks:
                    task_data = task.to_dict()
                    task_data['creator_name'] = task.users.username
                    task_data['create_time'] = task.create_time.strftime('%Y-%m-%d %H:%M:%S')
                    task_data['end_time'] = task.end_time.strftime('%Y-%m-%d %H:%M:%S') if task.end_time else ''
                    ret.append(task_data)

                data = {
                    'tasks': ret,
                    'total': paginated_tasks.total
                }

                return self.response(MessageEnum.successs.value[0], MessageEnum.successs.value[1], data=data)

            except Exception as e:
                logger.error(f"Error fetching tasks: {str(e)}")
                return self.response(MessageEnum.task_query_error.value[0], MessageEnum.task_query_error.value[1])

        except Exception as e:
            logger.error(f"Error in request: {str(e)}")
            return self.response(MessageEnum.task_query_error.value[0], MessageEnum.task_query_error.value[1])

    def response(self, code, message, data=None):
        response = {'code': code, 'message': message}
        if data is not None:
            response['data'] = data
        return jsonify(response)


class Taskreport(MethodView):
    @login_required
    def get(self):
        try:
            task_id = request.args.get('task_id')
            page_index = int(request.args.get('page_index', 1))
            page_number = int(request.args.get('page_number', 10))

            task = Task.query.filter_by(id=task_id).first()
            if not task:
                return reponse(code=MessageEnum.task_not_exist.value[0],
                               message=MessageEnum.task_not_exist.value[1])
            if task.running_status not in [RunningStatus.FINISHED.value, RunningStatus.FAILED.value]:
                return reponse(code=MessageEnum.task_not_finished.value[0],
                               message=MessageEnum.task_not_finished.value[1])

            testres = TestcaseResult.query.filter_by(task_id=task_id).all()
            case_ids = [i.case_id for i in testres]

            cases = {case.case_id: [] for case in InterfaceCase.query.filter(InterfaceCase.case_id.in_(case_ids)).all()}
            for case in InterfaceCase.query.filter(InterfaceCase.case_id.in_(case_ids)).all():
                cases[case.case_id].append(case)

            assertinfos = {i.case_id: [] for i in InterfaceCaseAssert.query.filter(
                InterfaceCaseAssert.case_id.in_(case_ids)).all()}
            for assert_info in InterfaceCaseAssert.query.filter(InterfaceCaseAssert.case_id.in_(case_ids)).all():
                assertinfos[assert_info.case_id].append(assert_info)

            execute_list = []
            for i in testres:
                case_list = cases.get(i.case_id, [])
                for case in case_list:
                    e_info = {
                        'case_name': case.desc,
                        'is_pass': i.ispass,
                        'result': i.result,
                        'date': str(i.date),
                        'spend': i.spend
                    }
                    assert_info_list = assertinfos.get(i.case_id, [])
                    assert_info_dicts = [{
                        'expected_result': assert_info.excepted_result,
                        'expected_expression': assert_info.expression
                    } for assert_info in assert_info_list]

                    execute_list.append({**{'execute_info': e_info}, **{'assert_info': assert_info_dicts}})

            total_cases = len(execute_list)
            start = (page_index - 1) * page_number
            end = start + page_number
            paginated_execute_list = execute_list[start:end]

            execute_info = {
                'execute_list': paginated_execute_list,
                'total': total_cases
            }

            pass_cases = len([i for i in execute_list if i['execute_info']['is_pass']])
            fail_cases = total_cases - pass_cases
            pass_rate = "{:.2%}".format(pass_cases / total_cases) if total_cases > 0 else "0.00%"
            total_spend = "{:.2f}".format(sum(float(i['execute_info']['spend']) for i in execute_list))

            statistic_info = {
                'total': total_cases,
                'pass': pass_cases,
                'fail': fail_cases,
                'pass_rate': pass_rate,
                'spend': total_spend
            }

            ret = {'execute_info': execute_info, 'statistic_info': statistic_info}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.task_report_error.value[0],
                           message=MessageEnum.task_report_error.value[1])


# class BaseTaskHandler(MethodView):
#     def handle_task_execution(self, task_id):
#         try:
#             start_time = time.time()
#             task = Task.query.filter_by(id=task_id).first()
#             task_content = json.loads(task.task_content)
#             env_id = task_content['env_id']
#             suite = TestSuite.query.filter_by(id=task_content['suite_id']).first()
#             caseids = json.loads(suite.caseids)
#             caseinfos = self.get_case_infos(caseids)
#             env = Environment.query.filter_by(id=env_id).first()
#
#             if env.protocol == 'http':
#                 return self.handle_http_protocol(env, caseinfos, suite, task, start_time)
#             else:
#                 return self.handle_other_protocol(env_id, caseinfos, suite, task, start_time)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             raise e
#
#     def get_case_infos(self, caseids):
#         caseinfos = []
#         for case_id in caseids:
#             case = InterfaceCase.query.filter_by(case_id=case_id).first()
#             if case.status == 1:
#                 case_info = {'case_id': case.case_id, 'case_raw': case.raw}
#                 caseinfos.append(case_info)
#         return caseinfos
#
#     def handle_http_protocol(self, env, caseinfos, suite, task, start_time):
#         logger.info('开始处理HTTP协议测试套件')
#         caseids = [case['case_id'] for case in caseinfos]
#         logger.info('待处理的caseids是: {}', caseids)
#         flag = True
#         exe_res = []
#         for case in caseinfos:
#             executehandler = ExecuteHandler(case['case_id'], env.id)
#             res = executehandler.execute_task_http(case_id=case['case_id'], env_id=env.id, task_id=task.id)
#             if json.loads(res[0])['result'] != '断言通过':
#                 flag = False
#             ret = {'collections_name': suite.name, 'is_pass': flag, 'result': exe_res}
#             logger.info('ret is {}', ret)
#             self.update_task_status(task, flag, start_time)
#         return ret
#
#     def handle_other_protocol(self, env_id, caseinfos, suite, task, start_time):
#         result_queue = multiprocessing.Queue()
#         process = multiprocessing.Process(
#             target=self.run_in_new_process_multproto,
#             args=(env_id, caseinfos, result_queue)
#         )
#
#         process.start()
#         process.join()
#
#         res = result_queue.get()
#
#         if isinstance(res, tuple):
#             case_name = InterfaceCase.query.filter_by(case_id=res[0]).first().desc
#             return {'error_caseid': res[0], 'error_casename': case_name, 'error_info': format(res[1])}
#         elif isinstance(res, Exception):
#             return {'error_info': format(res)}
#
#         try:
#             flag = True
#             for i in res:
#                 caseid = i.get('case_id')
#                 rsp = i.get('exe_rsp')
#                 assertdesc = InterfaceCaseAssert.query.filter_by(case_id=caseid).first()
#                 assert_info = {}
#                 if assertdesc is not None:
#                     temp = rsp
#                     if '.' in assertdesc.expression:
#                         for j in assertdesc.expression.split('.'):
#                             temp = temp[j]
#                     else:
#                         temp = temp[assertdesc.expression]
#                     if isinstance(temp, bool):
#                         temp = str(temp).lower()
#                     else:
#                         temp = str(temp)
#                     if (temp == assertdesc.excepted_result) and i.get('exe_res'):
#                         isPass = True
#                     else:
#                         isPass = False
#                         flag = False
#                     assert_info = {'case_id': caseid, 'is_pass': isPass, 'except': assertdesc.excepted_result,
#                                    'actual': temp, 'assert_desc': assertdesc.assert_name,
#                                    'expression': assertdesc.expression}
#
#                 i['assert_info'] = assert_info
#                 testres = TestcaseResult(
#                     case_id=caseid,
#                     result=str(rsp),
#                     ispass=i.get('assert_info', {}).get('is_pass', True) and i.get('exe_res', False),
#                     date=datetime.now(),
#                     spend=i['exe_spend'],
#                     testevent_id=env_id,
#                     task_id=task.id
#                 )
#                 db.session.add(testres)
#             db.session.commit()
#             ret = {'collections_name': suite.name, 'is_pass': flag, 'result': res}
#             self.update_task_status(task, flag, start_time)
#             return ret
#         except Exception as e:
#             db.session.rollback()
#             logger.error(traceback.format_exc())
#             raise e
#
#     def update_task_status(self, task, flag, start_time):
#         if flag:
#             task.running_status = RunningStatus.FINISHED.value
#         else:
#             task.running_status = RunningStatus.FAILED.value
#         task.end_time = datetime.now()
#         task.spend = str("{:.2f}".format(time.time() - start_time))
#         db.session.commit()
#
#     def run_in_new_process_multproto(self, env_id, caseinfos, result_queue):
#         try:
#             logger.info('Task当前进程号：{}'.format(os.getpid()))
#             sys.stdin = open(os.devnull, 'r')
#             sys.stdout = open(os.devnull, 'w')
#             sys.stderr = open(os.devnull, 'w')
#             res = self.exemulproto(env_id, caseinfos)
#
#             result_queue.put(res)
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             result_queue.put(e)
#         finally:
#             sys.exit(0)
#
#     def exemulproto(self, env_id, caseinfos):
#         try:
#             logger.info('Task执行请求方法exeproto的进程号：{}'.format(os.getpid()))
#             source = json.loads(caseinfos[0]['case_raw'])['source']
#             branch_name = json.loads(caseinfos[0]['case_raw'])['branch_name']
#             proto_path = PROJECT_ROOT + ("/proto/" if source in ('kk', None) else "/proto/pp/") + branch_name
#             logger.info(f"proto_path: {proto_path}")
#
#             env = Environment.query.filter_by(id=env_id).first()
#             host, port = env.url, env.port
#
#             sys.path.append(proto_path)
#             uid = json.loads(caseinfos[0]['case_raw'])['uid']
#             player = Player(uid, host, port)
#             player.client = client = Client(host=host, port=port) if not player.client else player.client
#
#             for name in os.listdir(proto_path):
#                 if name == '__init__.py' or not name.endswith('.py'):
#                     continue
#                 module = importlib.import_module(
#                     f"proto.{branch_name}.{name[:-3]}" if source in (
#                         'kk', None) else f"proto.pp.{branch_name}.{name[:-3]}")
#                 for item in dir(module):
#                     player.client.pb[item] = getattr(module, item)
#
#             if source in ('kk', None):
#                 player = player.login_by_uid(uid)[1]
#             else:
#                 player = player.login_by_uid_pp(uid)[1]
#
#             reslut = []
#             for i in caseinfos:
#                 r = {'case_id': i['case_id']}
#                 params = json.loads(i['case_raw'])['proto_content']
#                 reqmessage = json.loads(i['case_raw'])['req_message_name']
#                 rspmessage = reqmessage[:-3] + "RSP"
#                 start_time = time.time()
#                 try:
#                     client.send(reqmessage, params)
#                     msg = client.recv(rspmessage)
#                     r['exe_res'] = True
#                     r['exe_rsp'] = msg.body
#                 except Exception as e:
#                     logger.error(f"Error processing case {i['case_id']}: {e}")
#                     logger.error(traceback.format_exc())
#                     r['exe_res'] = False
#                     r['exe_rsp'] = str(e)
#                 finally:
#                     end_time = time.time()
#                     r['exe_spend'] = str("{:.2f}".format(end_time - start_time))
#                     reslut.append(r)
#
#             logger.info('reslut is {}', reslut)
#             return reslut
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             raise e
#         finally:
#             client.stop() if 'client' in locals() else None


# class Executetask(BaseTaskHandler):
#     @login_required
#     def post(self):
#         try:
#             data = request.get_json()
#             if not data.get('task_id'):
#                 return reponse(code=MessageEnum.must_be_every_parame.value[0],
#                                message=MessageEnum.must_be_every_parame.value[1])
#
#             task_id = data.get('task_id')
#             task = Task.query.filter_by(id=task_id).first()
#             if not task:
#                 return reponse(code=MessageEnum.task_not_exist.value[0],
#                                message=MessageEnum.task_not_exist.value[1])
#
#             if task.running_status == RunningStatus.RUNNING.value:
#                 return reponse(code=MessageEnum.task_is_running.value[0],
#                                message=MessageEnum.task_is_running.value[1])
#
#             task.running_status = RunningStatus.RUNNING.value
#             db.session.commit()
#
#             spawn(self.dealtask, task_id)
#
#             return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
#
#         except Exception as e:
#             logger.error(traceback.format_exc())
#             return reponse(code=MessageEnum.task_execute_error.value[0],
#                            message=MessageEnum.task_execute_error.value[1])
#
#     def dealtask(self, task_id):
#         self.handle_task_execution(task_id)
class BaseTaskHandler(MethodView):
    def handle_task_execution(self, task_id):
        try:
            start_time = time.time()
            task = Task.query.filter_by(id=task_id).first()
            task_content = json.loads(task.task_content)
            env_id = task_content['env_id']
            suite = TestSuite.query.filter_by(id=task_content['suite_id']).first()
            caseids = json.loads(suite.caseids)
            caseinfos = self.get_case_infos(caseids)
            env = Environment.query.filter_by(id=env_id).first()

            if env.protocol == 'http':
                result = self.handle_http_protocol(env, caseinfos, suite, task, start_time)
            else:
                result = self.handle_other_protocol(env_id, caseinfos, suite, task, start_time)

            self.update_task_status(task, result['is_pass'], start_time)
        except Exception as e:
            logger.error(traceback.format_exc())
            self.update_task_status(task, False, start_time)

    def start_new_process(self, task_id):
        process = multiprocessing.Process(target=self.dealtask, args=(task_id,))
        process.start()

    def dealtask(self, task_id):
        try:
            self.handle_task_execution(task_id)
        except Exception as e:
            logger.error(f"Error executing task {task_id}: {e}")

    def get_case_infos(self, caseids):
        caseinfos = []
        for case_id in caseids:
            case = InterfaceCase.query.filter_by(case_id=case_id).first()
            if case.status == 1:
                case_info = {'case_id': case.case_id, 'case_raw': case.raw}
                caseinfos.append(case_info)
        return caseinfos

    def handle_http_protocol(self, env, caseinfos, suite, task, start_time):
        logger.info('开始处理HTTP协议测试套件')
        caseids = [case['case_id'] for case in caseinfos]
        logger.info('待处理的caseids是: {}'.format(caseids))
        flag = True
        exe_res = []
        for case in caseinfos:
            executehandler = ExecuteHandler(case['case_id'], env.id)
            res = executehandler.execute_task_http(case_id=case['case_id'], env_id=env.id, task_id=task.id)
            if json.loads(res[0])['result'] != '断言通过':
                flag = False
            exe_res.append(res)
        ret = {'collections_name': suite.name, 'is_pass': flag, 'result': exe_res}
        logger.info('ret is {}'.format(ret))
        return ret

    def handle_other_protocol(self, env_id, caseinfos, suite, task, start_time):
        logger.info('开始处理proto协议测试套件')
        caseids = [case['case_id'] for case in caseinfos]
        logger.info('待处理的proto caseids是: {}'.format(caseids))
        result_queue = multiprocessing.Queue()
        process = multiprocessing.Process(
            target=self.run_in_new_process_multproto,
            args=(env_id, caseinfos, result_queue)
        )

        process.start()
        process.join()

        res = result_queue.get()

        if isinstance(res, tuple):
            case_name = InterfaceCase.query.filter_by(case_id=res[0]).first().desc
            return {'error_caseid': res[0], 'error_casename': case_name, 'error_info': format(res[1])}
        elif isinstance(res, Exception):
            return {'error_info': format(res)}

        try:
            flag = True
            for i in res:
                caseid = i.get('case_id')
                rsp = i.get('exe_rsp')
                assertdesc = InterfaceCaseAssert.query.filter_by(case_id=caseid).first()
                assert_info = {}

                if assertdesc is not None:
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
                    keys = assertdesc.expression.split('.')
                    current = rsp
                    if not isinstance(current, str):
                        for key in keys:
                            if isinstance(current, list):
                                current = current[int(key)]
                            else:
                                current = current[key]
                        assert_res = AssertClass.assert_value(rsp, assertdesc.expression, assertdesc.excepted_result,
                                                              assert_operators.get(assertdesc.operator))
                        if assert_res and i.get('exe_res'):
                            isPass = True
                        else:
                            isPass = False
                            flag = False
                        assert_info = {'case_id': caseid, 'is_pass': isPass, 'except': assertdesc.excepted_result,
                                       'actual': current, 'assert_desc': assertdesc.assert_name,
                                       'expression': assertdesc.expression}

                i['assert_info'] = assert_info
                testres = TestcaseResult(
                    case_id=caseid,
                    result=str(rsp),
                    ispass=i.get('assert_info', {}).get('is_pass', True) and i.get('exe_res', False),
                    date=datetime.now(),
                    spend=i['exe_spend'],
                    testevent_id=env_id,
                    task_id=task.id
                )
                db.session.add(testres)
            db.session.commit()
            ret = {'collections_name': suite.name, 'is_pass': flag, 'result': res}
            return ret
        except Exception as e:
            db.session.rollback()
            logger.error(traceback.format_exc())
            raise e

    def update_task_status(self, task, flag, start_time):
        task.running_status = RunningStatus.FINISHED.value if flag else RunningStatus.FAILED.value
        task.end_time = datetime.now()
        task.spend = str("{:.2f}".format(time.time() - start_time))
        db.session.commit()

    def run_in_new_process_multproto(self, env_id, caseinfos, result_queue):
        try:
            logger.info('Task当前进程号：{}'.format(os.getpid()))
            sys.stdin = open(os.devnull, 'r')
            sys.stdout = open(os.devnull, 'w')
            sys.stderr = open(os.devnull, 'w')
            res = self.exemulproto(env_id, caseinfos)

            result_queue.put(res)

        except Exception as e:
            logger.error(traceback.format_exc())
            result_queue.put(e)
        finally:
            sys.exit(0)

    def exemulproto(self, env_id, caseinfos):
        try:
            logger.info('Task执行请求方法exeproto的进程号：{}'.format(os.getpid()))
            source = json.loads(caseinfos[0]['case_raw'])['source']
            branch_name = json.loads(caseinfos[0]['case_raw'])['branch_name']
            proto_path = PROJECT_ROOT + ("/proto/" if source in ('kk', None) else "/proto/pp/") + branch_name
            logger.info(f"proto_path: {proto_path}")

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
                    f"proto.{branch_name}.{name[:-3]}" if source in (
                        'kk', None) else f"proto.pp.{branch_name}.{name[:-3]}")
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
                start_time = time.time()
                try:
                    client.send(reqmessage, params)
                    msg = client.recv(rspmessage)
                    r['exe_res'] = True
                    r['exe_rsp'] = msg.body
                except Exception as e:
                    logger.error(f"Error processing case {i['case_id']}: {e}")
                    logger.error(traceback.format_exc())
                    r['exe_res'] = False
                    r['exe_rsp'] = str(e)
                finally:
                    end_time = time.time()
                    r['exe_spend'] = str("{:.2f}".format(end_time - start_time))
                    reslut.append(r)

            logger.info('reslut is {}'.format(reslut))
            return reslut
        except Exception as e:
            logger.error(traceback.format_exc())
            raise e
        finally:
            client.stop() if 'client' in locals() else None


class Executetask(BaseTaskHandler):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('task_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            task_id = data.get('task_id')
            task = Task.query.filter_by(id=task_id).first()
            if not task:
                return reponse(code=MessageEnum.task_not_exist.value[0],
                               message=MessageEnum.task_not_exist.value[1])

            if task.running_status == RunningStatus.RUNNING.value:
                return reponse(code=MessageEnum.task_is_running.value[0],
                               message=MessageEnum.task_is_running.value[1])

            task.running_status = RunningStatus.RUNNING.value
            db.session.commit()

            self.start_new_process(task_id)

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.task_execute_error.value[0],
                           message=MessageEnum.task_execute_error.value[1])


class Reruntask(BaseTaskHandler):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('task_id'):
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])

            task_id = data.get('task_id')
            task = Task.query.filter_by(id=task_id).first()
            if not task:
                return reponse(code=MessageEnum.task_not_exist.value[0],
                               message=MessageEnum.task_not_exist.value[1])

            if task.running_status != RunningStatus.FAILED.value and task.running_status != RunningStatus.FINISHED.value:
                return reponse(code=MessageEnum.task_not_done.value[0],
                               message=MessageEnum.task_not_done.value[1])
            new_task = Task()
            new_task.name = task.name.rsplit(' ', 1)[0] + ' ' + 'rerun' + ' ' + datetime.now().strftime('%Y%m%d%H%M%S')
            new_task.task_content = task.task_content
            new_task.creator = current_user.user_id
            new_task.product_line = task.product_line
            new_task.running_status = RunningStatus.RUNNING.value
            new_task.create_time = datetime.now()
            new_task.status = 1
            new_task.origin_taskid = task_id

            try:
                db.session.add(new_task)
                db.session.commit()
                newtask_id = new_task.id
                ret = {'newtask_id': newtask_id}
            except Exception as e:
                db.session.rollback()
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.task_create_error.value[0],
                               message=MessageEnum.task_create_error.value[1])
            self.start_new_process(newtask_id)
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.task_execute_error.value[0],
                           message=MessageEnum.task_execute_error.value[1])


class Creatorlist(MethodView):
    @login_required
    def get(self):
        try:
            c_user = User.query.filter_by(user_id=current_user.user_id).first()
            if c_user.role_id == 2:
                tasks = Task.query.filter_by(status=1).all()
            else:
                tasks = Task.query.filter_by(product_line=c_user.pdline, status=1).all()

            creator_list = []
            creator_ids = set()

            for task in tasks:
                if task.creator not in creator_ids:
                    creator = User.query.filter_by(user_id=task.creator).first()
                    if creator:
                        c = {'creator_id': creator.user_id, 'creator_name': creator.username}
                        creator_list.append(c)
                        creator_ids.add(task.creator)

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=creator_list)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.task_query_error.value[0], message=MessageEnum.task_query_error.value[1])
