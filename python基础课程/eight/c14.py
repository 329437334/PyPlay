import c13

print(c13.c)

class Myresource(object):
    # def __enter__(self):
        # print('connect to resource')
        # return self
    
    # def __exit__(self, exc_type, exc_value, tb):
        # print('close resource connection')

    
    def query(self):
        print('query data')

# with Myresource() as r:
    # r.query()
from contextlib import contextmanager

@contextmanager
def make_myresource():
    print('connect to resource')
    yield Myresource()
    print('close resource connection')
# yield 生成器
with make_myresource() as r:
    r.query()
