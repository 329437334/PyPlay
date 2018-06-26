'''
    Create by MccRee
'''
from app import mail
from flask_mail import Message


def send_email():
    # Python发电子邮件Flask插件
    msg = Message('测试邮件', sender='1656263239@qq.com', body='发封邮件测试一下', recipients=['301063915@qq.com'])
    mail.send(msg)
    pass
