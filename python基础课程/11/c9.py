# 闭包 = 函数 + 函数的环境

def curve_pre(a):
    a = 25
    def curve(x):
        return a*x*x
    return curve


f = curve_pre()
result = f(2)
print(result)


