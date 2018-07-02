'''
    Create by MccRee
'''
from flask import Blueprint

# 使用蓝图
from app.libs.redprint import Redprint

api = Redprint('user')


@api.route('', methods=['GET'])
def get_user():
    # REST 接口粒度比较粗
    # HTTP请求数量大幅增加
    # REST最适合做开放性API不掺杂业务逻辑
    # 遵守REST规范, 根据业务灵活变通
    return 'I am qy'


@api.route('', methods=['PUT'])
def update_user():
    return 'update qy'


@api.route('', methods=['DELETE'])
def delete_user():
    return 'delete qy'


@api.route('', methods=['POST'])
def create_user():
    # 提供给第三方的API
    # 客户端 client 种类非常多
    pass

