#名称空间：存放名字的地方，准确的说名称空间是存放名字与变量值绑定关系的地方

#内置名称空间：在python解释器启动时产生，存放一些python内置的名字
#全局名称空间：在执行文件时产生，存放文件级别定义的名字
# x=1
# def func():
#     y=2
#     def f1():pass
#     print
#
#
# import os
#
# class Foo:
#     pass
#
# if x==1:z=3

# del x


#局部名称空间:在执行文件的过程中，如果调用了函数，则会产生该函数的局部名称空间
#用来存放该函数内定义的名字，该名字在函数调用时生效，在函数调用结束后失效



#加载顺序：内置---》全局---》局部


#优先掌握一：名字的查找顺序是：局部-》全局-》内置

# # max=1
# def foo():
#     max=2
#     # print(max)
#
# foo()
# print(max)




# x=0
# def f1():
#     x=1
#     def f2():
#         x=2
#         def f3():
#             x=3
#             print(x)
#         f3()
#     f2()
#     print('=f1========',x)
#
#
# f1()



#
# def func1():
#     print('from func1')
#
# def func1():
#     print('=====?>')
#
# func1()
#
# x=1
# x=10
# print(x)





#作用域：作用的范围，
#全局作用域：全局存活，全局有效:globals()
# max=1111111
# def f1():
#     def f2():
#         def f3():
#             def f4():
#                 # print(x)
#                 print(max)
#             f4()
#         f3()
#     f2()
#
#
# f1()
#局部作用域：临时存活，局部有效:locals()

x=11111111111111111111111111111111111111111111

# def f1():
#     x=1
#     y=2
#     def f2():pass
#     # print(locals())
#     print(globals())
#
# f1()
# print(locals() is globals())
# print(locals())
#
# print(dir(globals()['__builtins__']))



#global nonlocal掌握
# x=1
# def f1():
#     global x
#     x=2
#
# f1()
# print(x)


# l=[]
# def f2():
#     l.append('f2')
#
# f2()
# print(l)


# x=0
# def f1():
#     # x=1
#     def f2():
#         # x=2
#         def f3():
#            # global x
#            nonlocal x
#            x=3
#         f3()
#         # print(x)
#     f2()
#     print(x)
# f1()
# print(x)




#优先掌握二：作用域关系，在函数定义时就已经固定
# ，于调用位置无关,在调用函数时，必须必须必须
#回到函数原来定义的位置去找作用域关系

x=1
def  f1():
    def f2():
        print(x)
    return f2


# func=f1()
# print(func)
# x=10000000
# func()
# x=10000000



def foo(func):
    x=300000000
    func() #f2()
x=10000000000000000000000



foo(f1())
# x=10000000000000000000000
# foo(f1())










