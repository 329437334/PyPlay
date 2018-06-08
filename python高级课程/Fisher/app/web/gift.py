'''
    Create by MccRee
'''
from flask import current_app, flash

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
    if current_user.can_save_to_list():
        try:
            gift = Gift()
            gift.isbn = isbn
            # 这里的current_user就是自定义的user对象
            gift.uid = current_user.id
            # 上面操作gift表-------下面操作user表------数据库中使用事务来确保一致性#
            current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
            db.session.add(gift)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e
    else:
        flash('这本书已添加至您的赠送清单或已存在于您的心愿单,请不要重复添加')


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
