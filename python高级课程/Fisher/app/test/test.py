'''
    Create by MccRee
'''

from flask import Flask, current_app, request, Request

app = Flask(__name__)

# 应用上下文 对象 Flask
# 请求上下文 对象 Request
# Flask AppContext
# Request RequestContext
# 离线应用,单元测,没有请求时要用Flask应用就需要自己push上下文
# ctx = app.app_context()
# ctx.push()
# a = current_app
# d = current_app.config['DEBUG']
# ctx.pop()

# 用with语句改写成上下文管理器
with app.app_context():
    a = current_app
    d = current_app.config['DEBUG']



# 1.对一个实现了上下文协议的对象使用with语句
# 2.对于实现了上下文协议的对象称为上下文管理器
# 3.__enter__ __exit__实现这两个方法
# 4.上下文表达式必须返回一个上下文管理器

# 文件读写, 数据库操作 都可以用with语句来写
# try:
#     f = open(r'/user/home/t.txt')
#     f.read()
# finally:
#     f.close()

# with open(r'') as f:
#     f.read()

class MyResource:

    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        # 处理异常也在exit中
        print('close resource connection')
        if exc_tb:
            print('process exception')
            return True
        else:
            print('no exception')
            return False
        # 返回False则外部还会继续抛出异常 返回True则不会


    def query(self):
        print('query data')

try:
    with MyResource() as resource:
        resource.query()
except Exception as ex:
    pass

