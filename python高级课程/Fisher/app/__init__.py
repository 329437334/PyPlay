'''
    Create by MccRee
'''
from flask import Flask
from flask_login import LoginManager
from app.models.base import db


login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    # 载入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    #把插件db与app绑定起来
    db.init_app(app)
    db.create_all(app=app)
    #绑定插件
    login_manager.init_app(app=app)
    login_manager.login_view = 'web.login'
    login_manager.login_message = '请先登录或者注册'
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)