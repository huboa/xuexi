#生成器：在函数内部包含yield关键，那么该函数执行的结果是生成器
#生成器就是迭代器
#yield的功能：
# 1 把函数的结果做生迭代器（以一种优雅的方式封装好__iter__,__next__）
# 2 函数暂停与再继续运行的状态是由yield




# def func():
#     print('first')
#     yield 11111111
#     print('second')
#     yield 2222222
#     print('third')
#     yield 33333333
#     print('fourth')
#
#
# g=func()
# print(g)
# from collections import Iterator
# print(isinstance(g,Iterator))

# print(next(g))
# print('======>')
# print(next(g))
# print('======>')
# print(next(g))
# print('======>')
# print(next(g))

# for i in g: #i=iter(g)
#     print(i)




# def func(n):
#     print('我开动啦')
#     while True:
#         yield n
#         n+=1
#
# g=func(0)
#
# # print(next(g))
# # print(next(g))
# # print(next(g))
# for i in g:
#     print(i)





#
# for i in range(10000):
#     print(i)

# def my_range(start,stop):
#     while True:
#         if start == stop:
#             raise StopIteration
#         yield start #2
#         start+=1 #3
#
# g=my_range(1,3)
# #
# print(next(g))
# print(next(g))
# print(next(g))
#

#
# for i in my_range(1,3):
#     print(i)



#yield与return的比较？
#相同：都有返回值的功能
#不同：return只能返回一次值，而yield可以返回多次值




# python3 02--tail.py -f access.log | grep 'error'
import time

def tail(filepath):
    with open(filepath, 'r') as f:
        f.seek(0, 2)
        while True:
            line = f.readline()
            if line:
                yield line
            else:
                time.sleep(0.2)


def grep(pattern,lines):
    for line in lines:
        if pattern in line:
            print(line,end='')

grep('error',tail('access.log'))