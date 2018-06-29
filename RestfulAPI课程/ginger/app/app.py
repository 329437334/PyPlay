'''
    Create by MccRee
'''

#通常在app下面实例化Flask的核心对象
from flask import Flask


def create_app():
    app = Flask(__name__)
    #装载配置文件
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    return app