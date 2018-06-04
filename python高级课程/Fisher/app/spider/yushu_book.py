'''
    Create by MccRee
'''
from app.libs.httper import HTTP
from flask import current_app


class YuShuBook:
    per_page = 15
    isbn_url = 'http://t.yushu.im/v2/book/isbn/{}'
    keyword_url = 'http://t.yushu.im/v2/book/search?q={}&count={}&start={}'

    def __init__(self):
        self.total = 0
        self.books = []

    def search_by_isbn(self, isbn):
        url = self.isbn_url.format(isbn)
        result = HTTP.get(url)
        self.__fill_single(result)

    def __fill_single(self, data):
        '''
        处理单本书
        :param data:
        :return:
        '''
        if data:
            self.total = 1
            self.books.append(data)

    def __fill_collection(self, data):
        self.total = data['total']
        self.books = data['books']

    def search_by_keyword(self, keyword, page=2):
        url = self.keyword_url.format(keyword, self.per_page, self.per_page * (page - 1))
        result = HTTP.get(url)
        self.__fill_collection(result)


    def calculate_start(page):
        return (page - 1) * current_app.config['PER_PAGE']


