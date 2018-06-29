'''
    Create by MccRee
'''
from flask import render_template, request, redirect, url_for, flash

from app.models.base import db
from app.forms.auth import RegisterForm, LoginForm, EmailForm, ResetPasswordForm
from app.models.user import User
from .blueprint import web
from flask_login import login_user, logout_user
from app.libs.email import send_email


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


@web.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('web.index'))

#这里忘记密码发邮件
@web.route('/reset/password', methods=['GET', 'POST'])
def forget_password_request():
    form = EmailForm(request.form)
    if request.method == 'POST':
        if form.validate():
            account_email = form.email.data
            # 这里如果使用first_or_404, 如果email不存在,那就抛404异常,后续代码不会走
            user = User.query.filter_by(email=account_email).first_or_404()
            # 尝试把发邮件放入异步线程中执行
            send_email(form.email.data,'重置你的密码','email/reset_password.html', user=user, token=user.generate_token())
            flash('一封邮件已经发送到邮箱' + account_email + '请及时查看')
    return render_template('auth/forget_password_request.html', form=form)


#点了邮件中的地址就走这个路由
@web.route('/reset/password/<token>', methods=['GET', 'POST'])
def forget_password(token):
    form = ResetPasswordForm(request.form)
    if request.method == 'POST' and form.validate():
        success = User.reset_password(token, form.password1.data)
        if success:
            flash('你的密码已经更新')
            return redirect(url_for('web.login'))
        else:
            flash('密码重置失败')
    return render_template('auth/forget_password.html',form=form)
