'''
旅行者
x,y

x = 0
3 result = 3
5 result = 8
6 resutl = 14
'''

origin = 0


def factory(pos):
    def go(step):
        # 强制声明pos不是局部变量
        nonlocal pos
        new_pos = pos + step
        pos = new_pos
        return new_pos
    return go


tourist = factory(origin)
print(tourist(2))
print(tourist.__closure__)
print(tourist(3))
print(tourist.__closure__)
print(tourist(5))
print(tourist.__closure__)
