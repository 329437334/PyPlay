'''
    Create by mccree
'''
from flask import Flask

app = Flask(__name__)


@app.route('/hello/')
def hello():
    #基于函数的视图
    #基于类的视图(即插视图)
    return 'hello Qiyue'


app.run()
