'''
map
'''

list_x = [1, 2, 3, 4, 5, 6, 7, 8]
list_y = [1, 2, 3, 4, 5]


def square(x):
    return x * x


r = map(square, list_x)
print(r)
print(list(r))

r = map(lambda x, y: x * x + y, list_x, list_y)
# map个数取决于 List中较少的那个个数
print(list(r))
