'''
    Create by MccRee
'''
from flask import render_template, request

from app.forms.auth import RegisterForm
from app.models.user import User
from .blueprint import web

@web.route('/auth')
def index():
    pass

#一个视图函数中处理注册页面 和 注册事件, 通过get/post方式来区分
@web.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.nickname = form.nickname.data
        user.email = form.email.data
        pass
    return render_template('auth/register.html',form={'data':{}})




@web.route('/login', methods=['GET', 'POST'])
def login():
    pass

@web.route('/reset/password', methods=['GET','POST'])
def forget_password_request():
    pass

@web.route('/reset/password/<token>', methods=['GET','POST'])
def forget_password(token):
    pass