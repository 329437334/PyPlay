'''
    Create by MccRee
'''

# 必须继承自db.Model
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash

from app import login_manager
from app.libs.helper import is_isbn_or_key
from app.models.base import Base
from sqlalchemy import Column, Integer, String, Boolean, Float
from flask_login import UserMixin

from app.models.gift import Gift
from app.models.wish import Wish
from app.spider.yushu_book import YuShuBook
from itsdangerous import JSONWebSignatureSerializer as Serializer

class User(Base, UserMixin):
    # 如果数据库不用默认表名, 需指定表名
    # __tablenam__ = 'users'
    id = Column(Integer, primary_key=True)
    nickname = Column(String(24), nullable=False)
    phone_number = Column(String(18), unique=True)
    # 默认属性nickname 对应数据库nickname 如果要对应数据库中别的字段名就Column('username')
    _password = Column('password', String(128), nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    confirmed = Column(Boolean, default=False)
    # beans 鱼豆数量
    beans = Column(Float, default=0)
    send_counter = Column(Integer, default=0)
    receive_counter = Column(Integer, default=0)
    wx_open_id = Column(String(50))
    wx_name = Column(String(32))

    # 好比get方法
    @property
    def password(self):
        return self._password

    # 好比set方法, raw代表原始密码
    @password.setter
    def password(self, raw):
        self._password = generate_password_hash(raw)

    # 生成token
    def generate_token(self, expiration=600):
        s = Serializer(current_app.config['SECRET_KEY'])
        temp = s.dumps({'id':self.id}).decode('utf-8')
        return temp

    @staticmethod
    def reset_password(new_password):
        pass

    def check_password(self, raw):
        '''
        验证密码
        '''
        return check_password_hash(self._password, raw)

    def can_save_to_list(self, isbn):
        if is_isbn_or_key(isbn) != 'isbn':
            return False
        yushu_book = YuShuBook()
        yushu_book.search_by_isbn(isbn)
        if not yushu_book.first:
            return False
        # 不允许同一个用户同时赠送多本相同的图书
        # 不允许一个用户同时是赠送者又是索要者
        gifting = Gift.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        wishing = Wish.query.filter_by(uid=self.id, isbn=isbn, launched=False).first()
        if not gifting and not wishing:
            return True
        else:
            return False

    # def get_id(self):
    #     '''
    #     flask-login使用时,对于传入的user对象必须实现get_id
    #     :return: 表示用户身份的id
    #     如果继承自了UserMimix,并且唯一标识就是id字段则可以不用实现get_id,否则还是要自己实现
    #     '''
    #     return self.id


@login_manager.user_loader
def get_user(uid):
    # 拿到用户模型
    User.query.get(int(uid))
