from contextlib import contextmanager

@contextmanager
def book_mark():
    '''
    自动加书名号
    '''
    print('<<',end='')
    yield
    print('>>',end='')

with book_mark():
    print('且将生活饮而尽')