'''
    Create by MccRee
'''
from flask import Blueprint

book = Blueprint('book', __name__)

#使用蓝图分离视图函数,是存在缺陷的,蓝图的本意是用来区分模块的,而不是只用来分离视图函数

@book.route('/v1/book/get')
def get_book():
    return 'get book'

