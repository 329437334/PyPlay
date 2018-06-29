'''
    Create by MccRee
'''
from flask import Blueprint

#使用蓝图
from app.libs.redprint import Redprint

api = Redprint('user')

@api.route('/get')
def get_user():
    return 'I am qy'

