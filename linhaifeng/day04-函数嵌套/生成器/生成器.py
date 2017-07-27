##生成器：在函数内部包含yield 关键，那么该函数执行的结果就是生成器
##生成器就是迭代器
##yield 的功能：
##1把函数结果做迭代器（以一种优雅的方法封装好————iter__,__next__）
##2 函数暂停与再继续运行的状态是yield 保持状态
def func():
    print('first')
    yield 11111
    print('second')
    yield 2222
    print('third')
    yield '3333'

g=func()
# print(next(g))
# print(next(g))
# print(next(g))
# print(next(g))
# #
for n in g:
    print(n)

def func(n):
    while True:
        print(n)
        yield n
        n=n+1
g=func(0)

next(g)


for i in range(1000):
    print(i)

def my_range(start,stop):
    while True:
        if start == stop:
            raise StopIteration
        yield start
        start+=1
for n in my_range(1,3):
    print(n)

##yield与return的比较
