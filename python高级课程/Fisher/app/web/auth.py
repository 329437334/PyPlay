'''
    Create by MccRee
'''
from flask import render_template, request, redirect, url_for, flash

from app.models.base import db
from app.forms.auth import RegisterForm, LoginForm
from app.models.user import User
from .blueprint import web
from flask_login import login_user


# 一个视图函数中处理注册页面 和 注册事件, 通过get/post方式来区分
@web.route('/register', methods=['GET', 'POST'])
def register():
    print(request.form)
    form = RegisterForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User()
        user.set_attrs(form.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('web.login'))
    return render_template('auth/register.html', form=form)


@web.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            # 把数据库查到的user对象传给flask-login中的login_user,本质是把用户信息写入cookie, remeber为True则记住登陆,默认365天
            login_user(user, remember=True)
            # request.args用于获取url中?后面的查询参数
            next = request.args.get('next')
            if not next or not next.startswith('/'):
                # 当用在地址栏中直接输入login时,会获取不到next所以直接跳到web.index, next.startswitch是为了防止重定向攻击
                next = url_for('web.index')
            return redirect(next)
        else:
            flash('账号不存在,或者密码错误')
    return render_template('auth/login.html', form=form)


@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    pass


@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    pass
