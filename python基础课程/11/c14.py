
def f1():
    a = 10
    def f2():
        # f2内部的a被python认为是局部变量,无法影响外部环境a
        a = 20
        return a
    return f2

f =  f1()
print(f.__closure__)
r =  f() 
print(r)


def f3():
    a = 10
    def f4():
        # 闭包的存在一定需要函数内部引用函数外部环境
        return a
    return f4

fn =  f3()
print(fn.__closure__)
r =  fn() 
print(r)
