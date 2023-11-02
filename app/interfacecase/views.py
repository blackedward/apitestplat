import json
import traceback

from flask import Blueprint, request
from flask.views import MethodView
from flask_login import login_required, current_user

from app.models import *
from common.jsontools import reponse
from error_message import MessageEnum
from common.log import logger
from common.executehandler import ExecuteHandler

interfacecase = Blueprint('interfacecase', __name__)


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

            interfacecaseassert = InterfaceCaseAssert.query.filter_by(case_id=case_id).all()
            if not interfacecaseassert:
                return reponse(code=MessageEnum.get_assert_error.value[0],
                               message=MessageEnum.get_assert_error.value[1])
            res = []
            for i in interfacecaseassert:
                res.append(i.to_json())
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=res)

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

            interfacecaseassert = InterfaceCaseAssert.query.filter_by(assert_id=data.get('assert_id')).first()
            if not interfacecaseassert:
                return reponse(code=MessageEnum.edit_assert_error.value[0],
                               message=MessageEnum.edit_assert_error.value[1])

            interfacecaseassert.assert_name = data.get('assert_name')
            interfacecaseassert.case_id = data.get('case_id')
            interfacecaseassert.type = data.get('type')
            interfacecaseassert.expression = data.get('expression')
            interfacecaseassert.operator = data.get('operator')
            interfacecaseassert.excepted_result = data.get('excepted_result')
            interfacecaseassert.order = data.get('order')
            interfacecaseassert.created_time = data.get('created_time')
            interfacecaseassert.update_time = data.get('update_time')
            try:
                db.session.add(interfacecaseassert)
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            except Exception as e:
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.edit_assert_error.value[0],
                               message=MessageEnum.edit_assert_error.value[1])

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
                res.append(i.to_json())
            ret = {"content": res, "total": interfacecase.per_page}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_assert_error.value[0], message=MessageEnum.get_assert_error.value[1])


class ExecuteCase(MethodView):
    @login_required
    def post(self):
        try:
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

            if data.get('basicinfo') and data.get('requestinfo'):
                interfacecase = InterfaceCase()
                interfacecase.project_id = data.get('basicinfo')['project_id']
                interfacecase.model_id = data.get('basicinfo')['model_id']
                interfacecase.case_protocol = data.get('requestinfo')['caseprotcol']
                interfacecase.is_relycase = data.get('basicinfo')['is_relycase']
                interfacecase.rely_dbf = data.get('basicinfo')['rely_dbf']
                interfacecase.url = data.get('requestinfo')['url']
                interfacecase.method = data.get('requestinfo')['method']
                interfacecase.desc = data.get('basicinfo')['casedesc']
                interfacecase.headers = data.get('requestinfo')['headers']
                interfacecase.params = data.get('requestinfo')['params']
                # interfacecase.form_data_encoded = data.get('requestinfo')['form_data_encoded']
                # interfacecase.form_data = data.get('requestinfo')['form_data']
                interfacecase.socketreq = data.get('requestinfo')['socketreq']
                interfacecase.socketrsp = data.get('requestinfo')['socketrsp']
                interfacecase.raw = data.get('requestinfo')['raw']
                # interfacecase.raw_type = data.get('requestinfo')['raw_type']
                # interfacecase.body_type = data.get('requestinfo')['body_type']
                interfacecase.creater = current_user.user_id
                interfacecase.created_time = data.get('basicinfo')['created_time']
                interfacecase.update_time = data.get('basicinfo')['update_time']
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
                res.append(i.to_json())
            ret = {"content": res, "total": interfacecase.per_page}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_assert_error.value[0], message=MessageEnum.get_assert_error.value[1])
