import re

s = '83C72D1D8E6E78'
# match从字符串首字母开始匹配,没匹配到就返回空与findAll最大区别就是一匹配到就结束匹配
r = re.match('\d', s)
# span返回位置
print(r)
r1 = re.search('\d',s)
print(r1.group())