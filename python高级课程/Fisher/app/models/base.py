'''
    Create by MccRee
'''
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy

from sqlalchemy import SmallInteger, Column, Integer

# 这里在引入SQLAlchemy时,因为子类想要用SQLAlchemy名字,所以父类引入时就as _SQLAlchemy
db = _SQLAlchemy()


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


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
