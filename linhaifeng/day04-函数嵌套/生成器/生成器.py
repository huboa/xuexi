##生成器：在函数内部包含yield 关键，那么该函数执行的结果就是生成器
##生成器就是迭代器
##yield 的功能：1

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
