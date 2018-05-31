'''
    Create by MccRee
    #蓝图 blueprint
'''
from flask import jsonify, request

from app.forms.book import SearchForm
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YuShuBook
from app.view_models.book import BookViewModel
from .blueprint import web

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
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YuShuBook.search_by_isbn(q)
            result = BookViewModel.package_single(result, q)
        else:
            result = YuShuBook.search_by_keyword(q, page)
            result = BookViewModel.package_collection(result, q)

        return jsonify(result)
    else:
        return jsonify(form.errors)
