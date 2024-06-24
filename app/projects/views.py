import traceback
from enum import Enum

from flask import Blueprint, typing as ft, render_template, jsonify
from flask import redirect, request, session, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user
import json
from app.models import *
from flask.views import View, MethodView

from common.exesql import ExeSql
from common.jsontools import reponse
from error_message import MessageEnum
from common.log import logger

project = Blueprint('project', __name__)


class CreateProject(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.project_cannot_empty.value[0],
                               message=MessageEnum.project_cannot_empty.value[1])
            project_name = data.get('project_name')
            if not project_name:
                return reponse(code=MessageEnum.project_cannot_empty.value[0],
                               message=MessageEnum.project_cannot_empty.value[1])
            if Project.query.filter_by(project_name=project_name).first():
                return reponse(code=MessageEnum.project_only_one.value[0],
                               message=MessageEnum.project_only_one.value[1])
            project = Project()
            project.project_name = project_name
            project.status = 1
            project.product = data.get('product')
            project.project_user_id = current_user.user_id
            db.session.add(project)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.project_add_error.value[0],
                           message=MessageEnum.project_add_error.value[1])


class DeleteProject(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.project_cannot_empty.value[0],
                               message=MessageEnum.project_cannot_empty.value[1])
            project_id = data.get('project_id')
            if not project_id:
                return reponse(code=MessageEnum.project_cannot_empty.value[0],
                               message=MessageEnum.project_cannot_empty.value[1])
            project = Project.query.filter_by(id=project_id).first()
            if not project or project.status == 0:
                return reponse(code=MessageEnum.project_search.value[0],
                               message=MessageEnum.project_search.value[1])
            if current_user.role_id == 2:
                db.session.query(Model).filter(Model.project == project_id).update({Model.status: 0})
                db.session.query(Environment).filter(Environment.project == project_id).update({Environment.status: 0})
                db.session.query(InterfaceCase).filter(InterfaceCase.project_id == project_id).update(
                    {InterfaceCase.status: 0})
                project.status = 0
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            else:
                return reponse(code=MessageEnum.permiss_is_ness.value[0],
                               message=MessageEnum.permiss_is_ness.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.cobfig_delete_error.value[0],
                           message=MessageEnum.cobfig_delete_error.value[1])


class UpdateProject(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.project_cannot_empty.value[0],
                               message=MessageEnum.project_cannot_empty.value[1])
            project_id = data.get('project_id')
            project_name = data.get('project_name')
            if not project_id or not project_name:
                return reponse(code=MessageEnum.project_cannot_empty.value[0],
                               message=MessageEnum.project_cannot_empty.value[1])
            project = Project.query.filter_by(id=project_id).first()
            if not project or project.status == 0:
                return reponse(code=MessageEnum.project_search.value[0],
                               message=MessageEnum.project_search.value[1])

            project.project_name = project_name
            try:
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.edit_fial.value[0],
                               message=MessageEnum.edit_fial.value[1])
            if not data.get('envs'):
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            else:
                newenvs = data.get('envs')
                oldnenvs = Environment.query.filter_by(project=project_id, status=1).all()
                for i in newenvs:
                    if i.get('envid'):
                        env = Environment.query.filter_by(id=i.get('envid')).first()
                        env.name = i.get('name')
                        env.url = i.get('url')
                        env.port = i.get('port')
                        env.protocol = i.get('protocol')
                        env.desc = i.get('desc')
                        env.project = project_id
                        env.make_user = current_user.user_id
                        env.status = 1
                        try:
                            db.session.commit()
                        except Exception as e:
                            db.session.rollback()
                            logger.error(traceback.format_exc())
                            return reponse(code=MessageEnum.edit_fial.value[0],
                                           message=MessageEnum.edit_fial.value[1])
                    else:
                        env = Environment()
                        env.name = i.get('name')
                        env.url = i.get('url')
                        env.port = i.get('port')
                        env.protocol = i.get('protocol')
                        env.desc = i.get('desc')
                        env.project = project_id
                        env.make_user = current_user.user_id
                        env.status = 1
                        try:
                            db.session.add(env)
                            db.session.commit()
                        except Exception as e:
                            db.session.rollback()
                            logger.error(traceback.format_exc())
                            return reponse(code=MessageEnum.edit_fial.value[0],
                                           message=MessageEnum.edit_fial.value[1])
                for j in oldnenvs:
                    logger.info(j.id)
                    logger.info(newenvs)
                    if not any(j.id == d.get('envid') for d in newenvs):
                        j.status = 0
                        try:
                            db.session.commit()
                        except Exception as e:
                            db.session.rollback()
                            logger.error(traceback.format_exc())
                            return reponse(code=MessageEnum.edit_fial.value[0],
                                           message=MessageEnum.edit_fial.value[1])
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.edit_fial.value[0],
                           message=MessageEnum.edit_fial.value[1])


class GetPrjById(MethodView):
    @login_required
    def get(self, id):
        try:
            project = Project.query.filter_by(id=id).first()
            if not project:
                return reponse(code=MessageEnum.project_search.value[0],
                               message=MessageEnum.project_search.value[1])
            rsdatat = {}
            rsdatat['project_id'] = project.id
            rsdatat['project_name'] = project.project_name
            rsdatat['product'] = project.product
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=rsdatat)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.project_search.value[0],
                           message=MessageEnum.project_search.value[1])


class GetPrjByName(MethodView):
    @login_required
    def get(self, name):
        try:
            project = Project.query.filter_by(project_name=name).first()
            if not project:
                return reponse(code=MessageEnum.project_search.value[0],
                               message=MessageEnum.project_search.value[1])
            rsdatat = {}
            rsdatat['project_id'] = project.id
            rsdatat['project_name'] = project.project_name
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=rsdatat)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.project_search.value[0],
                           message=MessageEnum.project_search.value[1])


class GetAllPrj(MethodView):
    @login_required
    def get(self):
        try:
            page_index = 1
            page_number = 10
            if request.args.get("page_number"):
                page_number = request.args.get('page_number')
            if request.args.get("page_index"):
                page_index = request.args.get('page_index')
            if current_user.role_id == 2:
                project = Project.query.filter_by(status=1).paginate(int(page_index), int(page_number), False)
            else:
                user = User.query.filter_by(user_id=current_user.user_id).first()
                project = Project.query.filter_by(status=1, product=user.pdline).paginate(int(page_index),
                                                                                          int(page_number),
                                                                                          False)
            if not project:
                return reponse(code=MessageEnum.project_search.value[0],
                               message=MessageEnum.project_search.value[1])
            rdata = []
            for i in project.items:
                rdata.append(i.to_json())

            ret = {"list": rdata, "total": project.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.project_search.value[0],
                           message=MessageEnum.project_search.value[1])


class CreateDb(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.db_para_error.value[0],
                               message=MessageEnum.db_para_error.value[1])
            try:
                namex = data.get('db_name')
                dbconf = Dbconf.query.filter_by(db_name=namex).first()
                if dbconf.db_name == namex:
                    return reponse(code=MessageEnum.db_name_rep.value[0],
                                   message=MessageEnum.db_name_rep.value[1])
            except Exception as e:
                pass
            dbconf = Dbconf()
            dbconf.db_name = data.get('db_name')
            dbconf.type = data.get('type')
            dbconf.desc = data.get('desc')
            dbconf.url = data.get('url')
            dbconf.username = data.get('username')
            dbconf.password = data.get('password')
            dbconf.status = 1
            dbconf.test_url = data.get('test_url')
            dbconf.test_username = data.get('test_username')
            dbconf.test_password = data.get('test_password')
            dbconf.dev_url = data.get('dev_url')
            dbconf.dev_username = data.get('dev_username')
            dbconf.dev_password = data.get('dev_password')
            dbconf.stg_url = data.get('stg_url')
            dbconf.stg_username = data.get('stg_username')
            dbconf.stg_password = data.get('stg_password')
            dbconf.prod_url = data.get('prod_url')
            dbconf.prod_username = data.get('prod_username')
            dbconf.prod_password = data.get('prod_password')

            db.session.add(dbconf)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.db_cr_error.value[0],
                           message=MessageEnum.db_cr_error.value[1])


class DBType(Enum):
    MYSQL = 0
    ORACLE = 1
    SQLSERVER = 2


class GetDbById(MethodView):
    @login_required
    def get(self, id):
        try:
            dbconf = Dbconf.query.filter_by(id=id).first()
            if not dbconf:
                return reponse(code=MessageEnum.db_search_error.value[0],
                               message=MessageEnum.db_search_error.value[1])
            rsdatat = {}
            rsdatat['id'] = dbconf.id
            rsdatat['db_name'] = dbconf.db_name
            rsdatat['type'] = dbconf.type
            rsdatat['desc'] = dbconf.desc
            rsdatat['url'] = dbconf.url
            rsdatat['username'] = dbconf.username
            rsdatat['password'] = dbconf.password
            rsdatat['status'] = dbconf.status
            rsdatat['test_url'] = dbconf.test_url
            rsdatat['test_username'] = dbconf.test_username
            rsdatat['test_password'] = dbconf.test_password
            rsdatat['dev_url'] = dbconf.dev_url
            rsdatat['dev_username'] = dbconf.dev_username
            rsdatat['dev_password'] = dbconf.dev_password
            rsdatat['stg_url'] = dbconf.stg_url
            rsdatat['stg_username'] = dbconf.stg_username
            rsdatat['stg_password'] = dbconf.stg_password
            rsdatat['prod_url'] = dbconf.prod_url
            rsdatat['prod_username'] = dbconf.prod_username
            rsdatat['prod_password'] = dbconf.prod_password
            rsdatat['prod_url'] = dbconf.prod_url
            rsdatat['prod_username'] = dbconf.prod_username
            rsdatat['prod_password'] = dbconf.prod_password
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=rsdatat)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.db_search_error.value[0],
                           message=MessageEnum.db_search_error.value[1])


class GetAllDb(MethodView):
    @login_required
    def get(self):
        try:
            page_index = 1
            page_number = 10
            if request.args.get("page_index"):
                page_index = request.args.get("page_index")
            if request.args.get("page_number"):
                page_number = request.args.get("page_number")

            dbconf = Dbconf.query.filter_by(status=1).paginate(int(page_index), int(page_number), False)
            if not dbconf:
                return reponse(code=MessageEnum.db_search_error.value[0],
                               message=MessageEnum.db_search_error.value[1])
            rdata = []
            for i in dbconf.items:
                rdata.append(i.to_json())
            ret = {"list": rdata, "total": dbconf.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.db_search_error.value[0],
                           message=MessageEnum.db_search_error.value[1])


class ModifyDb(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.db_para_error.value[0],
                               message=MessageEnum.db_para_error.value[1])
            dbconf = Dbconf.query.filter_by(id=data.get('id')).first()
            if not dbconf:
                return reponse(code=MessageEnum.db_search_error.value[0],
                               message=MessageEnum.db_search_error.value[1])
            dbconf.db_name = data.get('db_name')
            dbconf.type = data.get('type')
            dbconf.desc = data.get('desc')
            dbconf.url = data.get('url')
            dbconf.username = data.get('username')
            dbconf.password = data.get('password')
            dbconf.status = data.get('status')
            dbconf.test_url = data.get('test_url')
            dbconf.test_username = data.get('test_username')
            dbconf.test_password = data.get('test_password')
            dbconf.dev_url = data.get('dev_url')
            dbconf.dev_username = data.get('dev_username')
            dbconf.dev_password = data.get('dev_password')
            dbconf.stg_url = data.get('stg_url')
            dbconf.stg_username = data.get('stg_username')
            dbconf.stg_password = data.get('stg_password')
            dbconf.prod_url = data.get('prod_url')
            dbconf.prod_username = data.get('prod_username')
            dbconf.prod_password = data.get('prod_password')

            db.session.add(dbconf)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.db_edit_error.value[0],
                           message=MessageEnum.db_edit_error.value[1])


class CreateDbfac(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data or not data.get('dbfac_name'):
                return reponse(code=MessageEnum.dbfac_para_error.value[0],
                               message=MessageEnum.dbfac_para_error.value[1])
            try:
                if data.get('dbfac_name') == DataFactory.query.filter_by(
                        dbfac_name=data.get('dbfac_name')).first().dbfac_name:
                    return reponse(code=MessageEnum.dbfac_name_rep.value[0],
                                   message=MessageEnum.dbfac_name_rep.value[1])  # 名称重复
            except Exception as e:
                pass
            dbfac = DataFactory()
            dbfac.dbfac_name = data.get('dbfac_name')
            dbfac.type = data.get('type')
            dbfac.times = data.get('times')
            dbfac.failed_stop = data.get('failed_stop')
            dbfac.sql_run_dev = data.get('sql_run_dev')
            dbfac.sql_db_id = data.get('sql_db_id')
            dbfac.sql_str = data.get('sql_str')
            # dbfac.interface_suite_id = data.get('interface_suite_id')
            # dbfac.ui_suite_id = data.get('ui_suite_id')
            dbfac.execute_type = data.get('execute_type')

            db.session.add(dbfac)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.dbfac_cr_error.value[0],
                           message=MessageEnum.dbfac_cr_error.value[1])


class GetFacByid(MethodView):
    @login_required
    def get(self, id):
        try:
            dbfac = DataFactory.query.filter_by(id=id).first()
            if not dbfac:
                return reponse(code=MessageEnum.dbfac_search_error.value[0],
                               message=MessageEnum.dbfac_search_error.value[1])
            rsdatat = {}
            rsdatat['id'] = dbfac.id
            rsdatat['dbfac_name'] = dbfac.dbfac_name
            rsdatat['type'] = dbfac.type
            rsdatat['times'] = dbfac.times
            rsdatat['failed_stop'] = dbfac.failed_stop
            rsdatat['sql_run_dev'] = dbfac.sql_run_dev
            rsdatat['sql_db_id'] = dbfac.sql_db_id
            rsdatat['sql_db_name'] = dbfac.dbconf.db_name
            rsdatat['sql_str'] = dbfac.sql_str
            # rsdatat['interface_suite_id'] = dbfac.interface_suite_id
            # rsdatat['ui_suite_id'] = dbfac.ui_suite_id
            rsdatat['execute_type'] = dbfac.execute_type
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=rsdatat)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.dbfac_search_error.value[0],
                           message=MessageEnum.dbfac_search_error.value[1])


class GetAllDf(MethodView):
    @login_required
    def get(self):
        try:
            page_index = 1
            page_number = 10
            if request.args.get("page_index"):
                page_index = request.args.get("page_index")
            if request.args.get("page_number"):
                page_number = request.args.get("page_number")

            dbfac = DataFactory.query.filter_by().paginate(int(page_index), int(page_number), False)
            if not dbfac:
                return reponse(code=MessageEnum.dbfac_search_error.value[0],
                               message=MessageEnum.dbfac_search_error.value[1])
            rdata = []
            for i in dbfac.items:
                rdata.append(i.to_json())
            ret = {"list": rdata, "total": dbfac.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.dbfac_search_error.value[0],
                           message=MessageEnum.dbfac_search_error.value[1])


class ModifyDbf(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data or not data.get('dbfac_name'):
                return reponse(code=MessageEnum.dbfac_para_error.value[0],
                               message=MessageEnum.dbfac_para_error.value[1])
            dbfac = DataFactory.query.filter_by(id=data.get('id')).first()
            if not dbfac:
                return reponse(code=MessageEnum.dbfac_search_error.value[0],
                               message=MessageEnum.dbfac_search_error.value[1])
            dbfac.dbfac_name = data.get('dbfac_name')
            dbfac.type = data.get('type')
            dbfac.times = data.get('times')
            dbfac.failed_stop = data.get('failed_stop')
            dbfac.sql_run_dev = data.get('sql_run_dev')
            dbfac.sql_db_id = data.get('sql_db_id')
            dbfac.sql_str = data.get('sql_str')
            # dbfac.interface_suite_id = data.get('interface_suite_id')
            # dbfac.ui_suite_id = data.get('ui_suite_id')
            dbfac.execute_type = data.get('execute_type')

            db.session.add(dbfac)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.dbfac_edit_error.value[0],
                           message=MessageEnum.dbfac_edit_error.value[1])


class CreateEnv(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.env_para_error.value[0],
                               message=MessageEnum.env_para_error.value[1])
            env = Environment()
            env.name = data.get('name')
            env.make_user = current_user.user_id
            env.url = data.get('url')
            env.port = data.get('port')
            env.protocol = data.get('protocol')
            env.desc = data.get('desc')
            env.project = data.get('project')
            env.status = 1

            db.session.add(env)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.env_cr_error.value[0],
                           message=MessageEnum.env_cr_error.value[1])


class GetConfForP(MethodView):
    @login_required
    def get(self, id):
        try:
            prj = Project.query.filter_by(id=id).first()
            envs = prj.Interfacehuan.filter_by(status=1).all()
            rdata = []
            for i in envs:
                rdata.append(i.to_json())
            ret = {"list": rdata, "total": len(rdata)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.env_search_error.value[0],
                           message=MessageEnum.env_search_error.value[1])


class ModifyProConf(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.env_para_error.value[0],
                               message=MessageEnum.env_para_error.value[1])
            project = Project.query.filter_by(id=data.get('project_id')).first()
            if not project:
                return reponse(code=MessageEnum.project_search.value[0],
                               message=MessageEnum.project_search.value[1])
            confs = request.get_json().get('confs')
            for i in confs:
                # if (i.get('env_id') not in envs.id):
                #     return reponse(code=MessageEnum.env_search_error.value[0],
                #                    message=MessageEnum.env_search_error.value[1])
                env = Environment.query.filter_by(id=i.get('env_id')).first()
                env.id = i.get('env_id')
                env.name = i.get('name')
                env.make_user = current_user.user_id
                env.url = i.get('url')
                env.port = i.get('port')
                env.protocol = i.get('protocol')
                env.desc = i.get('desc')
                env.project = data.get('project_id')
                env.status = 1

                db.session.commit()

            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.env_edit_error.value[0],
                           message=MessageEnum.env_edit_error.value[1])


class CreateModel(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.model_para_error.value[0],
                               message=MessageEnum.model_para_error.value[1])

            model = Model()
            model.model_name = data.get('model_name')
            model.model_user_id = current_user.user_id
            model.project = data.get('project_id')
            model.status = 1

            db.session.add(model)
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.model_edit_fial.value[0],
                           message=MessageEnum.model_edit_fial.value[1])


class ModifyModel(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.edit_model_error.value[0],
                               message=MessageEnum.edit_model_error.value[1])
            model = Model.query.filter_by(id=data.get('model_id')).first()
            if not model:
                return reponse(code=MessageEnum.model_not_exict.value[0],
                               message=MessageEnum.model_not_exict.value[1])
            model.model_name = data.get('model_name')
            model.model_user_id = current_user.user_id
            model.project = data.get('project_id')
            model.status = 1

            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])

        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.edit_model_error.value[0],
                           message=MessageEnum.edit_model_error.value[1])


class GetModelById(MethodView):
    @login_required
    def get(self, id):
        try:
            model = Model.query.filter_by(id=id).first()
            if not model:
                return reponse(code=MessageEnum.model_not_exict.value[0],
                               message=MessageEnum.model_not_exict.value[1])
            rsdatat = {}
            rsdatat['id'] = model.id
            rsdatat['model_name'] = model.model_name
            rsdatat['model_user_id'] = model.model_user_id
            rsdatat['project'] = model.project
            rsdatat['status'] = model.status
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=rsdatat)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.model_not_exict.value[0],
                           message=MessageEnum.model_not_exict.value[1])


class GetAllModel(MethodView):
    @login_required
    def get(self):
        try:
            page_index = request.args.get('page_index') or 1
            page_number = request.args.get('page_number') or 10

            model = Model.query.filter_by(status=1).paginate(int(page_index), int(page_number), False)
            if not model:
                return reponse(code=MessageEnum.model_not_exict.value[0],
                               message=MessageEnum.model_not_exict.value[1])
            rdata = []
            for i in model.items:
                rdata.append(i.to_json())
            ret = {"list": rdata, "total": model.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.model_not_exict.value[0],
                           message=MessageEnum.model_not_exict.value[1])


class GetModelByPrjId(MethodView):
    @login_required
    def get(self, id):
        try:
            page_index = request.args.get('page_index') or 1
            page_number = request.args.get('page_number') or 10

            model = Model.query.filter_by(project=id, status=1).paginate(int(page_index), int(page_number), False)
            project_name = Project.query.filter_by(id=id).first().project_name

            rdata = []
            for i in model.items:
                tdic = {}
                tdic['id'] = i.id
                model_case_count = InterfaceCase.query.filter_by(model_id=i.id, status=1).count()
                tdic['model_case_count'] = model_case_count
                tdic['model_name'] = i.model_name
                tdic['project'] = project_name
                tdic['status'] = i.status
                rdata.append(tdic)
            ret = {"list": rdata, "total": model.total}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.model_not_exict.value[0],
                           message=MessageEnum.model_not_exict.value[1])


class DeleteModel(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.model_cannot_empty.value[0],
                               message=MessageEnum.model_cannot_empty.value[1])
            model_id = data.get('model_id')
            if not model_id:
                return reponse(code=MessageEnum.model_cannot_empty.value[0],
                               message=MessageEnum.model_cannot_empty.value[1])
            model = Model.query.filter_by(id=model_id).first()
            if not model or model.status == 0:
                return reponse(code=MessageEnum.model_not_exict.value[0],
                               message=MessageEnum.model_not_exict.value[1])
            db.session.query(InterfaceCase).filter(InterfaceCase.model_id == model_id).update({InterfaceCase.status: 0})
            model.status = 0
            db.session.commit()
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.model_delete_error.value[0],
                           message=MessageEnum.model_delete_error.value[1])


class ExeDbFac(MethodView):
    @login_required
    def post(self):
        data = request.get_json()
        if not data or not data.get('dbfac_id'):
            return reponse(code=MessageEnum.parames_not_null.value[0],
                           message=MessageEnum.parames_not_null.value[1])
        try:
            dbfac = DataFactory.query.filter_by(id=data.get('dbfac_id')).first()
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
            if dbfac.sql_str and dbfac.sql_str.__contains__(';'):
                toexecsqls = dbfac.sql_str.split(';')
            else:
                toexecsqls = dbfac.sql_str

            linkurl = "mysql+pymysql://" + sqlusername + ":" + sqlpassword + "@" + sqlurl
            exesql = ExeSql(linkurl)
            logger.info('待执行的SQL是{}', toexecsqls)
            if isinstance(toexecsqls, list):
                for i in toexecsqls:
                    if i:
                        exesql.exe_sql(i)
            else:
                exesql.exe_sql(toexecsqls)
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.test_sql_query_error.value[0],
                           message=MessageEnum.test_sql_query_error.value[1])


class AddProject(MethodView):
    @login_required
    def post(self):
        data = request.get_json()
        if not data or not data.get('projectname'):
            return reponse(code=MessageEnum.parames_not_null.value[0],
                           message=MessageEnum.parames_not_null.value[1])
        try:
            project = Project.query.filter_by(project_name=data.get('projectname')).first()
            if project:
                return reponse(code=MessageEnum.project_only_one.value[0],
                               message=MessageEnum.project_only_one.value[1])
            project = Project()
            project.project_name = data.get('projectname')
            project.project_user_id = current_user.user_id
            project.status = 1
            try:
                db.session.add(project)
                db.session.flush()
                project_id = project.id
                db.session.commit()
            except Exception as e:
                db.session.rollback()
                logger.error(traceback.format_exc())
                return reponse(code=MessageEnum.project_add_error.value[0],
                               message=MessageEnum.project_add_error.value[1])

            if data.get('envs'):

                for i in data.get('envs'):
                    env = Environment()
                    env.name = i.get('envname')
                    env.make_user = current_user.user_id
                    env.url = i.get('url')
                    env.port = i.get('port')
                    env.protocol = i.get('protocol')
                    env.desc = i.get('desc')
                    env.project = project_id
                    env.status = 1

                    db.session.add(env)
                try:
                    db.session.commit()
                    return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
                except Exception as e:
                    db.session.rollback()
                    logger.error(traceback.format_exc())
                    return reponse(code=MessageEnum.project_add_error.value[0],
                                   message=MessageEnum.project_add_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.project_add_error.value[0],
                           message=MessageEnum.project_add_error.value[1])


class Getallenv(MethodView):

    @login_required
    def get(self):
        try:
            envs = Environment.query.filter_by(status=1).all()
            if not envs:
                return reponse(code=MessageEnum.env_search_error.value[0],
                               message=MessageEnum.env_search_error.value[1])
            rdata = []
            for i in envs:
                rdata.append(i.to_json())
            ret = {"list": rdata, "total": len(rdata)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.env_search_error.value[0],
                           message=MessageEnum.env_search_error.value[1])


class Getplbypid(MethodView):
    @login_required
    def get(self, id):
        try:
            project = Project.query.filter_by(id=id).first()
            if not project:
                return reponse(code=MessageEnum.project_search.value[0],
                               message=MessageEnum.project_search.value[1])
            rdata = {'product': project.product}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1],
                           data=rdata)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.project_search.value[0],
                           message=MessageEnum.project_search.value[1])
