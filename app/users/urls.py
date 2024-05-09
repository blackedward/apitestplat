from app.users.views import *


user.add_url_rule("/register", view_func=CreateUserView.as_view('register'))
user.add_url_rule("/login", view_func=LoginView.as_view('login'))
user.add_url_rule("/logout", view_func=LogoutView.as_view('logout'))
user.add_url_rule('/freezeuser', view_func=FreezeUserView.as_view('freezeuser'))
user.add_url_rule('/unfreezeuser', view_func=UnFreezeUserView.as_view('unfreezeuser'))
user.add_url_rule('/setadmin', view_func=SetAdminView.as_view('setadmin'))
user.add_url_rule('/list', view_func=UserList.as_view('list'))
user.add_url_rule('/currentuser', view_func=Currentuser.as_view('currentuser'))
user.add_url_rule("/resetpsw", view_func=Resetpsw.as_view('resetpsw'))

