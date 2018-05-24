'''
    Create by mccree
'''
from flask import Flask


app = Flask(__name__)
#载入配置文件
app.config.from_object('config')
print(app.config['DEBUG'])

@app.route('/start')
def hello():
    #基于函数的视图,推荐
    return 'hello Qiyue'

#另一种路由注册办法,基于类的视图(即插视图)

if __name__ == '__main__':
    # 生成环境一般会使用 nginx+uwsgi 由uwsgi来加载fisher.py,所以app.run不会被执行
    app.run(host='0.0.0.0',debug=app.config['DEBUG'],port=81)
