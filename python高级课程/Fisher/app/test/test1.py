'''
    Create by MccRee
'''

import threading, time

from werkzeug.local import Local


def download():
    print('i am thread')
    t = threading.current_thread()
    print(t.getName())


t = threading.current_thread()
print(t.getName())

new_t = threading.Thread(target=download)
# Python在解释器层 加了锁GIL 多核CPU只允许1个线程执行
new_t.start()


# flask web框架
# 请求             线程
# 多个请求     webserver开启
# Java PHP Nginx Apache Tomcat IIS

# werkzeug Local 线程隔离 字典结构
# LocalStack Local 字典
# Local使用字典的方式实现线程隔离
# LocalStack封装了Local作为自己的属性实现了栈结构

class A:
    b = 1


# my_obj = A()
# 使用Local对象来线程隔离,原理就是用线程id作为字典key
my_obj = Local()
my_obj.b = 1


def worker():
    my_obj.b = 2
    print('in new thread b is :' + str(my_obj.b))


new_t2 = threading.Thread(target=worker, name='qy_thread')
new_t2.start()
time.sleep(1)
print('in main thread b is :' + str(my_obj.b))
