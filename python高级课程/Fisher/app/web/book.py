'''
    Create by MccRee
    #蓝图 blueprint
'''
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from .blueprint import web
import json

@web.route('/test')
def test1():
    from flask import request
    from app.test.none_local import n
    print(n.v)
    n.v = 2
    print('----------')
    print(getattr(request, 'v', None))
    setattr(request, 'v', 2)
    print(request.v)
    print('----------')
    return ''


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
    books = BookCollection()

    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        yushu_book = YuShuBook()

        if isbn_or_key == 'isbn':
            yushu_book.search_by_isbn(q)
        else:
            yushu_book.search_by_keyword(q, page)

        books.fill(yushu_book, q)
        # return jsonify(books)
        return json.dumps(books, default=lambda o:o.__dict__)

    else:
        return jsonify(form.errors)
