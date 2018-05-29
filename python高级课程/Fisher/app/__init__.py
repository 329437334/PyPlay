'''
    Create by MccRee
'''
from flask import Flask


def create_app():
    app = Flask(__name__)
    # 载入配置文件
    app.config.from_object('app.secure')
    app.config.from_object('app.setting')
    register_blueprint(app)
    return app


def register_blueprint(app):
    from app.web.book import web
    app.register_blueprint(web)