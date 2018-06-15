'''
    Create by MccRee
'''

# 必须继承自db.Model
from flask import current_app
from sqlalchemy.orm import relationship

from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger, desc, func
from collections import namedtuple

from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    # 这里的user.id只指上一行的user
    uid = Column(Integer, ForeignKey('user.id'))
    # 这里通过isbn编号来关联书籍
    isbn = Column(String(15), nullable=False)
    # launched表示是否赠送出去
    launched = Column(Boolean, default=False)

    @classmethod
    def get_user_gifts(cls, uid):
        gifts = Gift.query.filter_by(uid=uid, launched=False).order_by(desc(Gift.create_time)).all()
        return gifts

    @classmethod
    def get_wish_counts(cls, isbn_list):
        # 根据传入的一组isbn, 到Wish表中检索对应的礼物书籍,并且统计出每一个礼物的Wish心愿数量
        # 这里要查询模型并统计数量 db.session
        # filter()是传入条件表达式
        # mysql in 查询 xxx结果的isbn 在isbn_list中
        # func.count()用于统计
        count_list = db.session.query(func.count(Wish.id), Wish.isbn).filter(Wish.launched == False,
                                                                             Wish.isbn.in_(isbn_list),
                                                                             Wish.status == 1).group_by(Wish.isbn).all()
        # 尽量返回对象或字典 这里用了个推导式
        count_list = [{'count': w[0], 'isbn': w[1]} for w in count_list]
        return count_list

    @property
    def book(self):
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(self.isbn)
        return yushu_book.first

    # 对象代表一个礼物,在对象方法中查询多个礼物是不合理的
    @classmethod
    def recent(cls):
        # filter_by 筛选 limit限制返回数 order_by排序 distinct去重 desc倒序
        # 链式调用
        # 主体 Query
        # 子函数 filter_by等
        # 所有的子涵数都会返回主体Query
        # 链式调用里有一个触发函数,比如all() first()
        recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            desc(Gift.create_time)).limit(
            current_app.config['RECENT_BOOK_COUNT']).all()
        return recent_gift
