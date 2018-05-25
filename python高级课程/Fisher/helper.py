'''
    Create by MccRee
'''


def is_isbn_or_key(word):
    '''
    判断q是isbn还是普通关键字
    search?q=&isbn= 参考的豆瓣
    q: 区分普通关键字 / isbn
    isbn10 10个0到9数字组成,含一些'-'
    page: 页码 每页条数
    '''
    isbn_or_key = 'key'
    # q.isdigit用来判断是否全部由数字组成
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    short_word = word.replace('-', '')
    if "-" in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
