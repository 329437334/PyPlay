'''
    Create by MccRee
'''


from sqlalchemy.orm import relationship
from app.models.base import Base, db
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger, desc, func

from app.spider.yushu_book import YuShuBook


class Wish(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    # 这里的user.id只指上一行的user
    uid = Column(Integer, ForeignKey('user.id'))
    # 这里通过isbn编号来关联书籍
    isbn = Column(String(15), nullable=False)
    launched = Column(Boolean, default=False)


    @classmethod
    def get_user_wishes(cls, uid):
        wishes = Wish.query.filter_by(uid=uid, launched=False).order_by(desc(Wish.create_time)).all()
        return wishes

    @classmethod
    def get_gifts_counts(cls, isbn_list):
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