def f1():
    a = 10

    def f2():
        #a赋值后就变成了局部变量, 就不是闭包了
        a = 20
        print(a)
    print(a)
    f2()
    print(a)


f1()
