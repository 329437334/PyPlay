'''
    Create by MccRee
'''
from flask import Blueprint

#使用蓝图
user = Blueprint('user', __name__)



@user.route('/v1/user/get')
def get_user():
    return 'I am qy'

