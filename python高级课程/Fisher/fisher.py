'''
    Create by mccree
'''
import json

from flask import Flask, make_response
from helper import is_isbn_or_key
from yushu_book import YuShuBook

app = Flask(__name__)
# 载入配置文件
app.config.from_object('config')
print(app.config['DEBUG'])


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)

    if isbn_or_key == 'isbn':
        result = YuShuBook.search_by_isbn(q)
    else:
        result = YuShuBook.search_by_keyword(q)

    return json.dumps(result), 200, {'content-type':'application/json'}


if __name__ == '__main__':
    # 生成环境一般会使用 nginx+uwsgi 由uwsgi来加载fisher.py,所以app.run不会被执行
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=5000)
