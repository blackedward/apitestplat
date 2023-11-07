import traceback

from flask import Blueprint, typing as ft, render_template
from flask import redirect, request, session, url_for, flash
from flask_login import login_user, login_required, logout_user, current_user

from app import loginManager
from app.models import *
from flask.views import View, MethodView
from common.jsontools import reponse
from error_message import MessageEnum
from common.log import logger

user = Blueprint('user', __name__)


@loginManager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


class CreateUserView(MethodView):

    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            username = data.get('username')
            password = data.get('password')
            job_number = data.get("job_number")

            job_num = User.query.filter_by(job_number=job_number).first()
            if job_num:
                flash(MessageEnum.jobnum_oblg_reg_one.value[1])
                return reponse(code=MessageEnum.jobnum_oblg_reg_one.value[0],
                               message=MessageEnum.jobnum_oblg_reg_one.value[1])
            user = User.query.filter_by(username=username).first()
            if user and user.is_enable:
                flash(MessageEnum.user_exict.value[1])
                return reponse(code=MessageEnum.user_exict.value[0],
                               message=MessageEnum.user_exict.value[1])
            new_user = User(username=username, job_number=job_number, role_id=1, real_name=username)
            new_user.set_password(password)
            db.session.add(new_user)
            try:
                db.session.commit()
                return reponse(code=MessageEnum.successs.value[0],
                               message=MessageEnum.successs.value[1])
            except Exception as e:
                logger.error(traceback.format_exc())
                db.session.rollback()
                flash(MessageEnum.user_register_error.value[1])
                return reponse(code=MessageEnum.user_register_error.value[0],
                               message=MessageEnum.user_register_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.user_register_error.value[0],
                           message=MessageEnum.user_register_error.value[1])


class LoginView(MethodView):

    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            username = data.get('username')
            password = data.get('password')
            user = User.query.filter_by(username=username).first()
            if user and user.is_enable:
                if user.check_password(password):
                    login_user(user)
                    session['username'] = username
                    return reponse(code=MessageEnum.successs.value[0], data="用户" + username + "登录成功",
                                   message=MessageEnum.successs.value[1])
                else:
                    flash(MessageEnum.login_password_error_message.value[1])
                    return reponse(code=MessageEnum.login_password_error_message.value[0],
                                   message=MessageEnum.login_password_error_message.value[1])
            else:
                flash(MessageEnum.login_user_not_exict_message.value[1])
                return reponse(code=MessageEnum.login_user_not_exict_message.value[0],
                               message=MessageEnum.login_user_not_exict_message.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.login_user_not_exict_message.value[0],
                           message=MessageEnum.login_user_not_exict_message.value[1])


class LogoutView(MethodView):
    @login_required
    def post(self):
        logout_user()
        return reponse(code=MessageEnum.successs.value[0], data="用户退出成功",
                       message=MessageEnum.successs.value[1])


class FreezeUserView(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            id = data.get('id')
            user = User.query.filter_by(user_id=id).first()
            if user and current_user.role_id == 2:
                if user.is_enable:
                    user.is_enable = False
                    db.session.commit()
                    return reponse(code=MessageEnum.successs.value[0], data="用户冻结成功",
                                   message=MessageEnum.free_is_success.value[1])
                else:
                    return reponse(code=MessageEnum.free_is_again.value[0], data="用户已经冻结，无需再次冻结",
                                   message=MessageEnum.free_is_again.value[1])
            else:
                return reponse(code=MessageEnum.free_user_error.value[0], data="冻结用户失败",
                               message=MessageEnum.free_user_error.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.free_user_error.value[0], data="冻结用户失败",
                           message=MessageEnum.free_user_error.value[1])


class UnFreezeUserView(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            id = data.get('id')
            user = User.query.filter_by(user_id=id).first()
            if user and current_user.role_id == 2:
                if not user.is_enable:
                    user.is_enable = True
                    db.session.commit()
                    return reponse(code=MessageEnum.successs.value[0], data="用户解冻成功",
                                   message=MessageEnum.user_is_un_free.value[1])
                else:
                    return reponse(code=MessageEnum.user_is_un_free.value[0], data="用户没有处于冻结状态",
                                   message=MessageEnum.user_is_un_free.value[1])
            else:
                return reponse(code=MessageEnum.user_is_unfree_success.value[0], data="解冻失败",
                               message=MessageEnum.user_is_unfree_success.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.user_is_unfree_success.value[0], data="解冻失败",
                           message=MessageEnum.user_is_unfree_success.value[1])


class SetAdminView(MethodView):
    @login_required
    def post(self):
        try:
            data = request.get_json()
            if not data:
                return reponse(code=MessageEnum.parames_not_null.value[0],
                               message=MessageEnum.parames_not_null.value[1])
            if current_user.role_id == 2:
                user_id = data.get('id')
                user = User.query.filter_by(user_id=user_id).first()
                if user:
                    user.role_id = 2
                    db.session.commit()
                    return reponse(code=MessageEnum.successs.value[0], data="设置管理员成功",
                                   message=MessageEnum.successs.value[1])
                else:
                    return reponse(code=MessageEnum.set_fail.value[0], data="设置管理员失败",
                                   message=MessageEnum.set_fail.value[1])
            else:
                return reponse(code=MessageEnum.set_fail.value[0], data="设置管理员失败",
                               message=MessageEnum.set_fail.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.set_fail.value[0], data="设置管理员失败",
                           message=MessageEnum.set_fail.value[1])


class UserList(MethodView):

    @login_required
    def get(self):
        try:
            page_index = 1
            page_number = 10
            if request.args.get("page_number"):
                page_number = request.args.get('page_number')
            if request.args.get("page_index"):
                page_index = request.args.get('page_index')

            users = User.query.paginate(int(page_index), int(page_number), False)
            if not users:
                return reponse(code=MessageEnum.login_user_not_exict_message.value[0],
                               message=MessageEnum.login_user_not_exict_message.value[1])
            data = []
            for user in users.items:
                data.append(user.to_json())

            ret = {"total": users.total, "list": data}
            return reponse(code=MessageEnum.successs.value[0], data=ret, message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.login_user_not_exict_message.value[0],
                           message=MessageEnum.login_user_not_exict_message.value[1])


class Currentuser(MethodView):

    @login_required
    def get(self):
        try:
            user = User.query.filter_by(username=current_user.username).first()
            if not user:
                return reponse(code=MessageEnum.login_user_not_exict_message.value[0],
                               message=MessageEnum.login_user_not_exict_message.value[1])
            data = user.to_json()
            ret = {}
            ret["username"] = data["username"]
            ret["real_name"] = data["real_name"]
            ret["is_enable"] = data["is_enable"]
            ret["job_number"] = data["job_number"]
            ret["is_admin"] = (data["role_id"] == 2)
            return reponse(code=MessageEnum.successs.value[0], data=ret, message=MessageEnum.successs.value[1])
        except Exception as e:
            logger.error(traceback.format_exc())
            return reponse(code=MessageEnum.login_user_not_exict_message.value[0],
                           message=MessageEnum.login_user_not_exict_message.value[1])
