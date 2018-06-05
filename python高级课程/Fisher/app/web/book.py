'''
    Create by MccRee
    #蓝图 blueprint
'''
from flask import jsonify, request, render_template, flash

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel, BookCollection
from .blueprint import web
import json


@web.route('/test')
def test():
    r = {
        'name': '',
        'age': 18
    }
    r1 = {

    }
    flash('hello qiyue', category='error')
    flash('hello jiuyue', category='warning')
    # 模板 html
    return render_template('test.html', data=r, data1=r1)


@web.route('/test1')
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
    else:
        flash('搜索的关键字不符合要求,请重新输入关键字')

    return render_template('search_result.html', books=books)


@web.route('/book/<isbn>/detail')
def book_detail(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    book = BookViewModel(yushu_book.first)
    return render_template('book_detail.html', book=book, wishes=[], gifts=[])


1