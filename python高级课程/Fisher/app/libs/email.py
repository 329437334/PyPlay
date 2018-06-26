'''
    Create by MccRee
'''
from flask import current_app, render_template

from app import mail
from flask_mail import Message


def send_email(to, subject, template, **kwargs):
    # Python发电子邮件Flask插件
    # msg = Message('测试邮件', sender='1656263239@qq.com', body='发封邮件测试一下', recipients=['301063915@qq.com'])
    # mail.send(msg)
    msg = Message('[鱼书]'+''+subject,
                  sender=current_app.config['MAIL_USERNAME'],
                  recipients=[to])
    msg.html = render_template(template, **kwargs)
    mail.send(msg)


