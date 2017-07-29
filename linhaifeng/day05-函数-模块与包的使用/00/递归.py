#递归调用：在调用一个函数的过程中，直接或间接地调用了函数本身

#直接
# def func():
#     print('from func')
#     func()
#
# func()

#间接
# def foo():
#     print('from foo')
#     bar()
#
# def bar():
#     print('from bar')
#     foo()
#
# foo()


#
# age(5)=age(4)+2
# age(4)=age(3)+2
# age(3)=age(2)+2
# age(2)=age(1)+2
# age(1)=18

# age(n)=age(n-1)+2 #n>1
# age(1)=18 #n=1

def age(n):
    if n == 1:
        return 18
    return age(n-1)+2

print(age(5))

#递归的执行分为两个阶段：
#1 递推
#2 回溯


l =[1, 2, [3, [4, 5, 6, [7, 8, [9, 10, [11, 12, 13, [14, 15,[16,[17,]],19]]]]]]]

def search(l):
    for item in l:
        if type(item) is list:
            search(item)
        else:
            print(item)

search(l)



















