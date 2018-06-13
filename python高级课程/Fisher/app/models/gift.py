'''
    Create by MccRee
'''

# 必须继承自db.Model
from flask import current_app
from sqlalchemy.orm import relationship

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float, ForeignKey, SmallInteger


class Gift(Base):
    id = Column(Integer, primary_key=True)
    user = relationship('User')
    # 这里的user.id只指上一行的user
    uid = Column(Integer, ForeignKey('user.id'))
    # 这里通过isbn编号来关联书籍
    isbn = Column(String(15), nullable=False)
    # launched表示是否赠送出去
    launched = Column(Boolean, default=False)

    def recent(self):
        # filter_by 筛选 limit限制返回数 order_by排序 distinct去重
         recent_gift = Gift.query.filter_by(
            launched=False).group_by(
            Gift.isbn).order_by(
            Gift.create_time).limit(
            current_app.config['RECENT_BOOK_COUNT']).all()
         return recent_gift

