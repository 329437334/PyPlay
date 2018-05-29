'''
    Create by MccRee

'''

# sqlachemy
# Flask_sqlachemy

from sqlalchemy import Column, Integer, String


class Book():
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    author = Column(String(30), default='未知作者')
    #精装平装
    binding = Column(String(20))
    #出版社
    publisher = Column(String(50))
    price = Column(String(20))
    pages = Column(Integer)
    pubdate = Column(String(20))
    #unique唯一索引
    isbn = Column(String(15), nullable=False, unique=True)
    #简介
    summary = Column(String(1000))
    image = Column(String(50))

    def sample(self):
        pass


