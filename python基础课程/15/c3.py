'''
可迭代对象,迭代器
凡是可以被for in 的对象就是可迭代对象
for in iterable
'''


class Book:
    pass


class BookCollection:
    '''
    实现iter和next就是迭代器
    '''
    def __init__(self):
        self.data = ['<往事>', '<回味>', '<茶馆>']
        self.cur = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.cur >= len(self.data):
            raise StopIteration()
        r = self.data[self.cur]
        self.cur += 1
        return r



books = BookCollection()
print(next(books))
for book in books:
    print(book)

'''
迭代器iterator,迭代器一定是可迭代对象
重新遍历就重新实例化一个对象
'''