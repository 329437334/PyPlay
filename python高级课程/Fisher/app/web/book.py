'''
    Create by MccRee
    #蓝图 blueprint
'''
from flask import jsonify, request

from app.forms.book import SearchForm
from helper import is_isbn_or_key
from yushu_book import YuShuBook
from .blueprint import web


@web.route('/book/search')
def search():
    '''
    Request类实例化后用于？接参数
    :param q:至少要有一个字符
    :param page:正整数，要有最大值限制
    :return:
    '''
    # 验证层概念,参数校验
    form = SearchForm(request.args)
    # form.validate校验参数，从验证层取数据避免没有默认值
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
        return jsonify(result)
    else:
        return jsonify(form.errors)
