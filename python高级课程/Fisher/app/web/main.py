'''
    Create by MccRee
'''
from app.models.gift import Gift
from .blueprint import web


@web.route('/')
def index():
    recent_gifts = Gift.recent()
    books = [BookViewModel(gift.book) for gift in recent_gifts]


@web.route('/personal')
def personal_center():
    pass