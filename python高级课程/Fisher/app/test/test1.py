'''
    Create by MccRee
'''

import threading, time

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
# 10个请求     webserver开启
# Java PHP Nginx Apache Tomcat IIS