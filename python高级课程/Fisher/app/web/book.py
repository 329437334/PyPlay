'''
    Create by MccRee
    #蓝图 blueprint
'''
from flask import jsonify, request

from helper import is_isbn_or_key
from yushu_book import YuShuBook
from .blueprint import web


@web.route('/book/search')
def search():
    '''
    Request类实例化后用于？接参数
    :param q:
    :param page:
    :return:
    '''
    q = request.args['q']
    page = request.args['page']
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)
    return jsonify(result)


