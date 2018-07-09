
import time

# 函数作为参数调用
def print_current_time(func):
    print(time.time())
    func()

# 闭包
def f3():
    a = 10

    def f4():
        # 闭包的存在一定需要函数内部引用函数外部环境
        return a
    return f4

# 装饰器
def decorator(func):
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func_name, func_name2):
    print('This is f1 named' + func_name)
    print('This is f1 named' + func_name2)


# f = decorator(f2)
# f()
# 装饰器定义复杂,调用简单
f1('test name', 'name2')

# @decorator

@decorator
def f3(name1, name2, **kw):
    print('This is a func named ' + name1)
    print('This is a function named ' + name2)
    print(kw)

f3('test func1', 'test func2', a=1, b=2, c='123')
