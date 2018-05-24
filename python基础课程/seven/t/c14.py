'''
    c14模块
'''
A = 2
B = 3
infos = dir()
print(infos)
print('name:' + __name__)
print('package: ' + (__package__ or '当前模块不属于任何包'))
print('doc:' + __doc__)
print('file:' + __file__)
# print('spec:' + __spec__)