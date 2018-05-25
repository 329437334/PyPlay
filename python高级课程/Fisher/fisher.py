'''
    Create by mccree
'''
from flask import Flask, make_response
from helper import is_isbn_or_key

app = Flask(__name__)
# 载入配置文件
app.config.from_object('config')
print(app.config['DEBUG'])


# 基于函数的视图,推荐


@app.route('/123')
def hello():
    '''
        视图函数的return与普通函数不同,
        还会返回 status code
        content-type http headers,默认content-type = text/html
        以上会封装成一个Response对象
        return '<html></html>'
    '''
    headers = {
        'content-type': 'text/plain',
        # 'content-type':'application/json',
        # 'location':'http://www.baidu.com'
    }
    # response = make_response('<html>啦啦啦啦</html>', 301)
    # response.headers = headers
    # return response
    return '<html></html>', 301, headers


@app.route('/book/search/<q>/<page>')
def search(q, page):
    isbn_or_key = is_isbn_or_key(q)
    pass


# 另一种路由注册办法,基于类的视图(即插视图)


if __name__ == '__main__':
    # 生成环境一般会使用 nginx+uwsgi 由uwsgi来加载fisher.py,所以app.run不会被执行
    app.run(host='0.0.0.0', debug=app.config['DEBUG'], port=81)
