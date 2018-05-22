import time

# 正真业务写在wrapper中,看起来就像wrapper被decorator装饰了
#


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        print('decorator')
        func(*args, **kw)
    return wrapper




@decorator
def f1(func_name):
    '''
        f1说明
    '''
    print('This is a function' + func_name)
    print(f1.__name__)




# f1('testName')
print(help(f1))
# f2('1', '2', '3')
# f3('name1', 'name2', 'name3', a=1,b=2,c='123')


