import time

# 正真业务写在wrapper中,看起来就像wrapper被decorator装饰了
#


def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        print('decorator')
        func(*args, **kw)
    return wrapper

def decorator2(func):
    def wrapper(*args, **kw):
        print('decorator2')
        func(*args, **kw)
    return wrapper


@decorator
@decorator2
def f1(func_name):
    print('This is a function' + func_name)


@decorator
def f2(func_name1, func_name2, func_name3,):
    print('This is func f2')


@decorator2
@decorator
def f3(func_name1, func_name2, func_name3, **kw):
    print('This is func f3')
    print(kw)


f1('testName')
# f2('1', '2', '3')
# f3('name1', 'name2', 'name3', a=1,b=2,c='123')


