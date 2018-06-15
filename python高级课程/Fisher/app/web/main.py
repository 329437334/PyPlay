'''
    Create by MccRee
'''
from flask import render_template

from app.models.gift import Gift
from app.view_models.book import BookViewModel
from .blueprint import web


@web.route('/')
def index():
    # recent_gifts = Gift.recent()
    # books = [BookViewModel(gift.book) for gift in recent_gifts]
    return render_template('index.html')


@web.route('/personal')
def personal_center():
    pass