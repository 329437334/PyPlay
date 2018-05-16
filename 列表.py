print(type([1,2,3,'1321','abc']))

#序列
'hello world'[2]
#切片
'hello world'[-1:]
#每两个切一次片
print('hello world'[0:8:2])

#判断是否在序列中
print(3 in [1,3,4,5,6,7])

#获取ASCII码序号
print(ord('A'))

#值类型
a=1
b=a
a=3
print(b)
#引用类型
a = [1,2,3]
b = a
a[0] = '4'
print(b)

#list是可变的

#tuple是不可变的