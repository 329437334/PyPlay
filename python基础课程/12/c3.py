from functools import reduce

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
# 连续计算,连续调用lambda,initial初始值,10+1+2...
r = reduce(lambda x, y: x+y, list_x, 10)
print(r)

# ((1+2)+3)+4...

list_y = ['1', '2', '3', '4', '5', '6', '7']
r2 = reduce(lambda x, y: x+y, list_y, 'aaa')
print(r2)
