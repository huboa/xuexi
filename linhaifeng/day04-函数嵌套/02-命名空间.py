##命名空间 存放名字与变量绑定关系的地方

#内置名称空间:在python 启动时启动产生，存放名字与变量绑定的关系
#全局命名空间：在执行文件时产生，文件级别定义的名字
#局部命名空间：在执行文件的过程中，如果调用了函数，则会产生函数的局部名称空间
#用来存放该函数内定义的名字，该名字在函数调用时生效，函数调用结束后失效


#加载顺序 内置 ---》》全局 ----》》内置 名称空间
#名字的查找顺序



# max=1
# def foo():
#     max=2
#     print(max)
# foo()

x=0
def f1():
    x=1
    def f2():
        x=2
        def f3():
            x=3
            print(x)
f1()

###作用域：作用的范围，
# 全局作用域：全局存活，全局有效 内置命名空间，全局命名空间
x=1
def f1():
    def f2():
        def f3():
            def f4():
                print(max)
                print(x)



f1()
# 局部作用域：临时存活，局部有效
def f1():
    x=1
    x=2
    def f2():pass
    print(locals())
    print(globals())
print(locals())
print(globals())
print(locals() is globals())


###global nonlocal  #尽量不用影响

x=1
def f1():
    global x
    x=2

f1()
print(x)

l=[]
def f2():
    l.append('f2')
f2()
print(l)

x=0
def f1():
    x=1
    def f2():
        x=2
        def f3():
            nonlocal x
            x = 3

        f3()
    f2()
    print(x)
f1()
print(x)


###优先掌握：
#作用域关系，在函数定义时就已经固定了，与调用位置无关
##优先掌握二：
x=1
def f1():
    def f2():
        print(x)
    return f2()



