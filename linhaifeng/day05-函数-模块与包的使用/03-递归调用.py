###递归调用：在调用一个函数过程中，直接或间接地调用函数
# def func():
#     print('from func')
#     yield
#     func()
#
# func()
#
# #间接递归
# def foo():
#     print('from foo')
#     bar
# def bar():
#     print("from bar")
#     foo()
#
# foo()

# age(5)=age(4)+2
# age(4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(n)=age(n-1)+2 ##n>1

def age(n):
    if n == 1:
        return 18
    return age(n-1)+2

print(age(5))