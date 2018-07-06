'''
    Create by MccRee
'''
from sqlalchemy import Column, Integer, String, SmallInteger
from werkzeug.security import generate_password_hash

from app.models.base import Base, db


class User(Base):
    id = Column(Integer, primary_key=True)
    email = Column(String(24), unique=True, nullable=False)
    nickname = Column(String(24), unique=True)
    #auth = 1 管理员 auth = 2 普通用户
    auth = Column(SmallInteger, default=1)
    #Column('password')制定了数据库中的字段名
    _password = Column('password', String(100))

    @property
    def password(self):
        return self._password

    @property.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    @staticmethod
    def register_by_email(nickname, account, secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)

