import time

# 正真业务写在wrapper中,看起来就像wrapper被decorator装饰了
#


def decorator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


@decorator
def f1():
    print('This is a function')


# f = decorator(f1)
# f()
f1()
