'''
    Create by MccRee
'''

class BookViewModel:
    # 描述特征(类变量, 实例变量)
    # 行为(方法)
    def __init__(self, book):
        self.title = book['title']
        self.publisher = book['publisher']
        self.author = ','.join(book['author'])
        self.image = book['image']
        self.price = book['price']
        self.summary = book['summary']
        self.pages = book['pages']

class BookCollection:
    '''
    一组bookViewModel
    '''
    def __init__(self):
        self.total = 0
        self.books = []
        self.keyword = ''

    def fill(self, yushu_book, keyword):
        self.total = yushu_book.total
        self.keyword = keyword
        self.books = [BookViewModel(book) for book in yushu_book.books]

