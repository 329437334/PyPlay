'''
    Create by MccRee
'''
from flask import render_template

from app.web import blueprint

from app.web import book
from app.web import auth
from app.web import drift
from app.web import gift
from app.web import main
from app.web import wish
from app.web.blueprint import web


@web.app_errorhandler(404)
def not_found(e):
    return render_template('404.html'), 404
