'''
闭包
'''

# 函数中定义函数,外部无法调用局部函数
# 把函数作为返回值返回
def curve_pre():
    a = 25
    def curev(x):
        print('This is a function')
        return a*x*x
    return curev

fun = curve_pre()
fun()
