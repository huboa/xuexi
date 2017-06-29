###生成器是小括号
# l = [x * x for x in range(10)]
# g = (x * x for x in range(10))
# print(l)
# for n in g:
#     print(n)

#generator保存的是算法
# def fib(max):
#          n, a, b = 0, 0, 1
#
#          while n < max:
#              print(b)
#              a,b = b,a+b
#              n = n + 1
#
#          return 'done'
# fib(8)

###
# def fib(max):
#     n, a, b = 0, 0, 1
#
#     while n < max:
#         yield b
#         a,b = b,a+b
#         n = n + 1
#
#     return 'done'
#
# for n in fib(9):
#     print(n)
# -*- coding: utf-8 -*-

def triangles():
    line = [1]
    while True:
        yield line
        line = [x + y for x, y in zip([0] + line, line + [0])]

n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

def triangles1():         # 杨辉三角形
    L = [1]
    while True:
        yield L
        L = [1] + [L[n] + L[n-1] for n in range(1, len(L))] + [1]

def triangles2():      # 杨辉三角形
    L = [1]
    while True:
        yield L
        L = [L[n - 1] + L[n] for n in range(len(L))]

def triangles3():      # 杨辉三角形
    L = [1]
    while True:
        yield L
        for n in range(1, len(L)):
            L[n] = pre[n] + pre[n - 1]
        L.append(1)
        pre = L[:]