'''
闭包 的本质是 函数 + 它的环境变量
'''

# 函数中定义函数,外部无法调用局部函数
# 把函数作为返回值返回


def curve_pre():
    a = 25

    def curev(x):
        return a*x*x
    return curev


a = 10

f = curve_pre()
print(f(2))
