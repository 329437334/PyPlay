'''
    Create by MccRee
'''

# 必须继承自db.Model
from werkzeug.security import generate_password_hash

from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float


class User(Base):
    # 如果数据库不用默认表名, 需指定表名
    # __tablenam__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    # 默认属性nickname 对应数据库nickname 如果要对应数据库中别的字段名就Column('username')
    _password = Column('password')
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    # 好比get方法
    @property
    def password(self):
        pass

    # 好比set方法, raw代表原始密码
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)
