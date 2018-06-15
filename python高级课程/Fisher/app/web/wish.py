'''
    Create by MccRee
'''
from flask import flash, redirect, url_for, render_template
from flask_login import login_required, current_user

from app import db
from app.models.wish import Wish
from app.view_models.wish import MyWishes
from .blueprint import web

@web.route('/wish')
def my_wish():
    uid = current_user.id
    wished_of_mine = Wish.get_user_wishes(uid)
    isbn_list = [wish.isbn for wish in wished_of_mine]
    gift_count_list = Wish.get_gifts_counts(isbn_list)
    view_model = MyWishes(wished_of_mine, gift_count_list)
    return render_template('my_wish.html',wishes=view_model.gifts)


@web.route('/save/wish/<isbn>')
@login_required
def save_to_wish(isbn):
    if current_user.can_save_to_list(isbn):
        # 既不在赠送清单，也不在心愿清单才能添加
        with db.auto_commit():
            wish = Wish()
            wish.uid = current_user.id
            wish.isbn = isbn
            db.session.add(wish)
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))