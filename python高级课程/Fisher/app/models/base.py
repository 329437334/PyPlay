'''
    Create by MccRee
'''

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import SmallInteger, Column, Integer

db = SQLAlchemy()


class Base(db.Model):
    # __abstract__ = True 这样就不会真实创建表
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def set_attrs(self, attrs_dict):
        '''
        类似OC的字典转属性,动态增加属性
        :param attrs_dict:
        :return:
        '''
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)
