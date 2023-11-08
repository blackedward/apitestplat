import json
import traceback

from flask import Blueprint, request
from flask.views import MethodView
from flask_login import login_required, current_user
from sqlalchemy import distinct

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
                tdic = {'case_id': i.case_id, 'project_id': i.project_id, 'model_id': i.model_id, 'desc': i.desc,
                        'creator': cr, 'project_name': pn}
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
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            baseinfo = data.get('basicinfo')
            interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()
            if not interfacecase:
                return reponse(code=MessageEnum.case_edit_error.value[0],
                               message=MessageEnum.case_edit_error.value[1])
            interfacecase.project_id = baseinfo['project_id']
            interfacecase.model_id = baseinfo['model_id']
            interfacecase.desc = baseinfo['casedesc']
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


class Updatecasereq(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.must_be_every_parame.value[0],
                               message=MessageEnum.must_be_every_parame.value[1])
            requestinfo = data.get('requestinfo')
            interfacecase = InterfaceCase.query.filter_by(case_id=data.get('caseid')).first()
            if not interfacecase:
                return reponse(code=MessageEnum.case_edit_error.value[0],
                               message=MessageEnum.case_edit_error.value[1])
            interfacecase.case_protocol = requestinfo['caseprotcol']
            interfacecase.url = requestinfo['url']
            interfacecase.method = requestinfo['method']
            if requestinfo['headers']:
                headers = {}
                requestheaders = json.loads(requestinfo['headers'])
                for i in requestheaders:
                    headers[i['name']] = i['value']
                interfacecase.headers = json.dumps(headers)
            if requestinfo['params']:
                params = {}
                requestparams = json.loads(requestinfo['params'])
                for i in requestparams:
                    params[i['name']] = i['value']
                interfacecase.params = json.dumps(params)
            interfacecase.socketreq = requestinfo['socketreq']
            interfacecase.socketrsp = requestinfo['socketrsp']
            interfacecase.raw = requestinfo['raw']
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

            interfacecase = InterfaceCase.query.filter_by(case_id=case_id, status=1).first()
            if interfacecase:
                creator = User.query.filter_by(user_id=interfacecase.creater).first().username
                basicinfo = {'case_id': interfacecase.case_id, 'project_id': interfacecase.project_id,
                             'model_id': interfacecase.model_id, 'desc': interfacecase.desc,
                             'creator': creator}
                requestinfo = {'caseprotcol': interfacecase.case_protocol, 'url': interfacecase.url,
                               'method': interfacecase.method, 'headers': interfacecase.headers,
                               'params': interfacecase.params, 'socketreq': interfacecase.socketreq,
                               'socketrsp': interfacecase.socketrsp, 'raw': interfacecase.raw}
                relydbf = interfacecase.rely_dbf
            else:
                return reponse(code=MessageEnum.get_case_detail_error.value[0],
                               message=MessageEnum.get_case_detail_error.value[1])
            precases = Precase.query.filter_by(parent_case_id=case_id, status=1).all()
            precasedata = []
            if precases:
                for i in precases:
                    precasedata.append(i.to_json())

            asserts = InterfaceCaseAssert.query.filter_by(case_id=case_id, status=1).all()
            assertdata = []
            if asserts:
                for i in asserts:
                    assertdata.append(i.to_json())

            ret = {'basicinfo': basicinfo, 'requestinfo': requestinfo, 'precases': precasedata, 'asserts': assertdata,
                   'relydbf': relydbf}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_case_detail_error.value[0],
                           message=MessageEnum.get_case_detail_error.value[1])
