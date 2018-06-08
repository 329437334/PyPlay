'''
    Create by MccRee
'''
from flask import current_app

from app import db
from app.models.gift import Gift
from .blueprint import web
from flask_login import login_required, current_user
@web.route('/my/gifts')
@login_required
def my_gifts():
    return 'MyGifts'

@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    '''
    赠送书籍
    '''
    gift = Gift()
    gift.isbn = isbn
    # 这里的current_user就是自定义的user对象
    gift.uid = current_user.id
    current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    db.session.add(gift)
    db.session.commit()


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
