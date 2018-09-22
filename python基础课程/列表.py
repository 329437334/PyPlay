print(type([1, 2, 3, '1321', 'abc']))

# 序列
'hello world'[2]
# 切片
'hello world'[-1:]
# 每两个切一次片
print('hello world'[0:8:2])

# 判断是否在序列中
print(3 in [1, 3, 4, 5, 6, 7])

# 获取ASCII码序号
print(ord('A'))

# 值类型
a = 1
b = a
a = 3
print(b)
# 引用类型
a = [1, 2, 3]
b = a
a[0] = '4'
print(b)

# list是可变的

# tuple是不可变的


'''
    模块说明
    python中的常亮不是真正意义上的常量
'''

ACCOUNT = 'qiyue'
PASSWORD = '123456'


while 0:
    print('ture')
else:
    print('false')


a = [1, 2, 3]

for x in a:
    if x == 2:
        break
        # continue
    print(x)
else:
    print('EOF')

for y in range(0, 10, 3):
    print(y, end='|')

for x in range(10, 0, -2):
    print(x, end='|')
