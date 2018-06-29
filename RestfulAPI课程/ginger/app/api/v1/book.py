'''
    Create by MccRee
'''
from flask import Blueprint

from app.libs.redprint import Redprint

api = Redprint('book')

#使用蓝图分离视图函数,是存在缺陷的,蓝图的本意是用来区分模块的,而不是只用来分离视图函数
#构建自定义对象redprint

@api.route('/get')
def get_book():
    return 'get book'

@api.route('/create')
def create_book():
    return 'create book'