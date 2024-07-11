import json
import traceback

import requests
from flask import Blueprint, typing as ft, render_template
from flask import redirect, request, session, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from app import loginManager
from app.models import *
from flask.views import View, MethodView
from common.jsontools import reponse
from error_message import MessageEnum
from common.log import logger

tools = Blueprint('tools', __name__)


class Changecard(MethodView):

    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not all([data.get('roomid'), data.get('borads'), data.get('users')]):
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            roomid = data.get('roomid')
            boards = data.get('boards')
            users = data.get('users')

            card_content = {'roomid': roomid, 'boards': boards, 'users': users}
            card_json = json.dumps(card_content)

            host = "beta10.kkpoker.co"
            post_url = 'http://' + str(host) + ':8004/after_login/after_log_username/rpc_call'

            payloaddata = {"roomid": roomid, "pb_name": "pb.iChangeCardREQ", "pb_data": "" + card_json + "",
                           "namespace": "",
                           "uid": 0, "id": 2507859, "name": ""}

            headers = {
                "Accept": "application/json, text/plain, */*",
                "Accept-Encoding": "gzip, deflate",
                "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7",
                "Connection": "keep-alive",
                "Content-Length": "621",
                "Content-Type": "application/json",
                "Host": "3.0.145.175:8080",
                "Origin": "http://3.0.145.175:8080",
                "Referer": "http://3.0.145.175:8080/",
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                              "Chrome/107.0.0.0 Safari/537.36",

            }

            msg = requests.post(post_url, headers=headers, data=json.dumps(payloaddata))
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=msg)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.test_error.value[0], message=MessageEnum.test_error.value[1])


class Addvar(MethodView):

    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not all([data.get('expression'), data.get('type'), data.get('value')]):
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            expression = data.get('expression')
            value = data.get('value')
            type = data.get('type')

            varconf = VariableConf()
            varconf.expression = expression
            varconf.value = value
            varconf.type = type
            varconf.creator = current_user.user_id
            varconf.create_time = datetime.now()
            varconf.status = 1
            try:
                db.session.add(varconf)
                db.session.commit()
                varid = varconf.id
                ret = {'varid': varid}
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
            except Exception as e:
                db.session.rollback()
                return reponse(code=MessageEnum.add_var_error.value[0], message=MessageEnum.add_var_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.add_var_error.value[0], message=MessageEnum.add_var_error.value[1])


class Delvar(MethodView):

    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data.get('id'):
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            id = data.get('id')
            try:
                varconf = VariableConf.query.filter_by(id=id).first()
                varconf.status = 0
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            except Exception as e:
                db.session.rollback()
                return reponse(code=MessageEnum.del_var_error.value[0], message=MessageEnum.del_var_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.del_var_error.value[0], message=MessageEnum.del_var_error.value[1])


class Varlist(MethodView):

    @login_required
    def get(self):
        try:
            page_index = int(request.args.get('page_index', 1))
            page_number = int(request.args.get('page_number', 10))
            varlist = VariableConf.query.filter_by(status=1).order_by(VariableConf.create_time.desc()).paginate(
                page_index, page_number, False)
            total = varlist.total
            items = varlist.items
            vars = []
            for item in items:
                vars.append({'id': item.id, 'expression': item.expression, 'value': item.value,
                             'creator': item.creator, 'create_time': str(item.create_time)})
            ret = {'total': total, 'items': vars}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_var_error.value[0], message=MessageEnum.get_var_error.value[1])


class Getvar(MethodView):

    @login_required
    def get(self):
        try:
            id = request.args.get('id')
            if not id:
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            varconf = VariableConf.query.filter_by(id=id).first()
            if varconf.status == 0:
                return reponse(code=MessageEnum.var_status_del.value[0], message=MessageEnum.var_status_del.value[1])
            ret = {'id': varconf.id, 'expression': varconf.expression, 'value': varconf.value,
                   'creator': varconf.creator, 'create_time': str(varconf.create_time)}
            return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1], data=ret)
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.get_var_error.value[0], message=MessageEnum.get_var_error.value[1])


class Updatevar(MethodView):

    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not all([data.get('id'), data.get('expression'), data.get('type'), data.get('value')]):
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            id = data.get('id')
            expression = data.get('expression')
            value = data.get('value')
            type = data.get('type')

            try:
                varconf = VariableConf.query.filter_by(id=id).first()
                varconf.expression = expression
                varconf.value = value
                varconf.type = type
                varconf.creat_time = datetime.now()
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0], message=MessageEnum.successs.value[1])
            except Exception as e:
                db.session.rollback()
                return reponse(code=MessageEnum.update_var_error.value[0],
                               message=MessageEnum.update_var_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.update_var_error.value[0], message=MessageEnum.update_var_error.value[1])
