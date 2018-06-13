'''
    Create by MccRee
'''

# 必须继承自db.Model
from flask import current_app
from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger, desc

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

