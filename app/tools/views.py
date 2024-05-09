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
