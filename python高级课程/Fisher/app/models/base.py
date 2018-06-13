'''
    Create by MccRee
'''
import datetime
from contextlib import contextmanager

from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery

from sqlalchemy import SmallInteger, Column, Integer


class SQLAlchemy(_SQLAlchemy):

    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            self.session.rollback()
            raise e


# 实现自定义的filter_by
class Query(BaseQuery):
    def filter_by(self, **kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query, self).filter_by(**kwargs)


# 这里在引入SQLAlchemy时,因为子类想要用SQLAlchemy名字,所以父类引入时就as _SQLAlchemy
db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    # __abstract__ = True 这样就不会真实创建表
    __abstract__ = True
    create_time = Column('create_time', Integer)
    status = Column(SmallInteger, default=1)

    def __init__(self):
        self.create_time = int(datetime.datetime.now().timestamp())

    def set_attrs(self, attrs_dict):
        '''
        类似OC的字典转属性,动态增加属性
        :param attrs_dict:
        :return:
        '''
        for key, value in attrs_dict.items():
            if hasattr(self, key) and key != 'id':
                setattr(self, key, value)

    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.formatimestamp(self.create_time)
        else:
            return None
