'''
生成器, 在gen中保存了算法
'''

n = [i for i in range(0, 10001)]

def gen(max):
    n = 0
    while n <= max:
        n+=1
        yield n
g = gen(10000)
print(next(g))
print(next(g))