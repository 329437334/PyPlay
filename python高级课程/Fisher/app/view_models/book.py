'''
    Create by MccRee
'''


class BookViewModel:
    # 描述特征(类变量, 实例变量)
    # 行为(方法)

    @classmethod
    def package_single(cls, data, keyword):
        '''
        :param data:
        :param keyword:
        :return: 单本书
        '''
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }

        if data:
            result['total'] = 1
            result['books'] = [cls.__cut_bookdata(data)]
        return result

    @classmethod
    def package_collection(cls, data, keyword):
        '''
        :param keyword:
        :return:书集合
        '''
        result = {
            'books': [],
            'total': 0,
            'keyword': keyword
        }
        if data:
            result['total'] = data['total']
            result['books'] = [cls.__cut_bookdata(book) for book in data['books']]
        return result

    # 处理data成book数据, 作者list处理成string
    @classmethod
    def __cut_bookdata(cls, data):
        book = {
            'title': data['title'],
            'publisher': data['publisher'],
            'pages': data['pages'] or '',
            'author': ','.join(data['author']),
            'price': data['price'],
            'summary': data['summary'] or '',
            'image': data['image']
        }
        return book
