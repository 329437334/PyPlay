'''
    Create by MccRee
'''
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
    gift = Gift()
    gift.isbn = isbn
    # 这里的current_user就是自定义的user对象
    gift.uid = current_user.id
    db.session.add(gift)
    db.session.commit()


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
