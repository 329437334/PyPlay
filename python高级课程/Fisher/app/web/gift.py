'''
    Create by MccRee
'''
from flask import current_app, flash, redirect, url_for, render_template

from app import db
from app.models.gift import Gift
from app.spider.yushu_book import YuShuBook
from app.view_models.gift import MyGifts
from .blueprint import web
from flask_login import login_required, current_user


@web.route('/my/gifts')
@login_required
def my_gifts():
    '''
    思路1 循环遍历我的礼物,根据每个礼物的isbn去Wish表中查这个书籍的相关心愿并计算数量
    思路2 取出每个礼物中的isbn编号 组成一个列表
    使用in查询去Wish表中查询在isbn列表中的心愿并计算数量

    这里使用思路2
    '''
    uid = current_user.id
    gifts_of_mine = Gift.get_user_gifts(uid)
    isbn_list = [gift.isbn for gift in gifts_of_mine]
    wish_count_list = Gift.get_wish_counts(isbn_list)

    view_model = MyGifts(gifts_of_mine,wish_count_list)
    return render_template('my_gifts.html', gifts_of_mine=view_model.gifts)


@web.route('/gifts/book/<isbn>')
@login_required
def save_to_gifts(isbn):
    yushu_book = YuShuBook()
    yushu_book.search_by_isbn(isbn)
    # gifting = Gift.query.filter_by(uid=current_user.id, isbn=isbn, status=1,
    #                                launched=False).first()
    # wishing = Wish.query.filter_by(uid=current_user.id, isbn=isbn, status=1,
    #                                launched=False).first()
    if current_user.can_save_to_list(isbn):
        # 既不在赠送清单，也不在心愿清单才能添加
        with db.auto_commit():
            gift = Gift()
            gift.uid = current_user.id
            gift.isbn = isbn
            # gift.book_id = yushu_book.data.id
            db.session.add(gift)
            # current_user.beans += current_app.config['BEANS_UPLOAD_ONE_BOOK']
    else:
        flash('这本书已添加至你的赠送清单或已存在于你的心愿清单，请不要重复添加')
    return redirect(url_for('web.book_detail', isbn=isbn))


@web.route('/gifts/<gid>/redraw')
def redraw_from_gifts(gid):
    pass
