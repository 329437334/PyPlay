

'''
正则表达式

正则表达式:一个特殊的字符序列,用于检测一个字符串是否与我们所设定的字符序列相匹配
快速检索,替换文本的操作

1. 检测一串数字是否是电话号码
2. 检测字符串是否是email格式
3. 把文本里指定单词替换为另一个

'''

import re

a = 'C|C++|Java|C#|Python|Javascript'

b = 'fda42313123r4523849hfdzs8978312'
# print(a.index('Python') > -1)


# 用常量匹配套路
r = re.findall('Python', a)
# 'Python'普通字符 '\d'元字符
r1 = re.findall('\d', b)
print(r1)


# 字符集套路
s = 'abc, acc, adc, aec, afc, ahc'
# 找出中间单词是c或者f的单词
r2 = re.findall('a[cf]c', s)
print(r2)
# 找出中间单词不是c不是f不是d的单词
r3 = re.findall('a[^cfd]c', s)
print(r3)
r4 = re.findall('a[b-f]c', s)
print(r4)


# 概括字符集套路
# \d \d
# \w 单词字符
# \s 空白字符
# .匹配除换行符\n之外所有字符
a1 = 'python1111java6789&c#'
r5 = re.findall('\w', a1)
print(r5)


# 数量词
a2 = 'python 1111 java 6789& php'
# 贪婪
r6 = re.findall('[a-z]{3,6}', a2)
# 非贪婪
r7 = re.findall('[a-z]{3,6}?', a2)
print(r6)
print(r7)
#正则贪婪与非贪婪, python默认贪婪匹配
# * 表示匹配*前面字符0次或者无限多次
# + 表示匹配*前面字符1次或者无限多次
# ? 表示匹配*前面字符1或0次或者无限多次
a3 = 'pytho0python1pythonn2'
r8 = re.findall('python?', a3)
print(r8)

# 边界匹配 表达式前^ 表达式后$
# ^指从字符串开头进行匹配
# $从字符串末尾开始匹配
qq = '1000000001'
# 4~8
r9 = re.findall('000', qq)
print(r9)

# 组
# []中是或关系
# ()中是切关系
a4 = 'PythonPythonPythonPython'
r10 = re.findall('(Python){3}', a4)
print(r10)

# 模式,第三个参数 re.I 忽略大小写 |加入更多匹配模式
lanuage = 'PythonC#JavaPHP\nObjC'
r11 = re.findall('c#.{1}', lanuage, re.I | re.S)
print(r11)


# 字符串替换
lanuage2 = 'PythonC#JavaC#PHPC#'
r12 = re.sub('C#', 'GO', lanuage2, 1)
print(r12)

def convert(value):
    matched = value.group()
    # print(value)
    return '!!' + matched + '!!'

r13 = re.sub('C#', convert, lanuage2)
print(r13)

