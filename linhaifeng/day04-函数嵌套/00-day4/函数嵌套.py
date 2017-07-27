#函数的嵌套调用：在调用一个函数的过程中，由调用了其他函数
# def bar():
#     print('from nbar')
#
# def foo():
#     print('from foo')
#     bar()
#
# foo()


# def max2(x,y):
#     if x > y:
#         return x
#     else:
#         return y
#
#
# def max4(a,b,c,d):
#     res1=max2(a,b)
#     res2=max2(res1,c)
#     res3=max2(res2,d)
#     return res3
#
#
# print(max4(1,2,3,-1))



#函数的嵌套定义：在一个函数的内部，又定义另外一个函数

def f2():
    print('from f2')

def f1():
    x=1
    # def f2()
    #     print('from f2')
    f2()

f1()



















