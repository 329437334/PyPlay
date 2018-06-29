'''
    Create by MccRee
'''

#通常在app下面实例化Flask的核心对象,关于Flask核心对象的操作都放在这里
from flask import Flask


def register_blueprints(app):
    from app.api.v1.user import user
    from app.api.v1.book import book
    app.register_blueprint(user)
    app.register_blueprint(book)


def create_app():
    app = Flask(__name__)
    #装载配置文件
    app.config.from_object('app.config.secure')
    app.config.from_object('app.config.setting')
    register_blueprints(app)
    return app