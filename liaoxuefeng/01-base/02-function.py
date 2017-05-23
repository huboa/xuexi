# print(abs(-151351))
# print(max(1,2,3,45,23,56))
#
# print(int(12.34))
# print(float(1.23))
# print(str(1.3212))
# print(hex(16))
# print(bool(12))
# print(bool())
#
# ##变量指向函数
# a=abs
# print(a(-1))
#
#
# x = abs(100)
# y = abs(-20)
# print(x, y)
# print('max(1, 2, 3) =', max(1, 2, 3))
# print('min(1, 2, 3) =', min(1, 2, 3))
# print('sum([1, 2, 3]) =', sum([1, 2, 3]))

# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
# #         return -x
# def my_abs(x):
#     if not isinstance(x, (int, float)):
#         raise TypeError('bad operand type')
#     if x >= 0:
#         return x
#     else:
#         return -x
# print(my_abs(-3))
# print(my_abs('A'))

# import math
#
# def move(x, y, step, angle=0):
#     nx = x + step * math.cos(angle)
#     ny = y - step * math.sin(angle)
#     return nx, ny
# print(move(100,200,2,angle=30))
#
# def quadratic(a,b,c):
#     ax2 + bx + c = 0
#

#
# def power(x,n=2):
#     s =1
#     while n > 0:
#         n = n -1
#         s = s * x
#
#     return s
# print(power(9,3))
# ##可变参数+*
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(9,25,3))

#关键参数
# def person(name, age, **kw):
#     print('name:', name, 'age:', age, 'other:', kw)
#
# print(person('Michael',30))
# print(person('Adam', 45, gender='M', job='Engineer'))
#
# def f1(a, b, c=0, *args, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)
#
# def f2(a, b, c=0, *, d, **kw):
#     print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)
#
# args = (1, 2, 3, 4)
# kw = {'d': 99, 'x': '#'}
# f1(*args, **kw)
#
# args = (1, 2, 3)
# kw = {'d': 88, 'x': '#'}
# f2(*args, **kw)

##*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。

import math
###递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(3))

def move(n,a,b,c):
    if n==1:
        print(a,'->',c)
    else:
        move(n-1,a,c,b)
        move(1,a,b,c)
        move(n-1,b,a,c)
print(move(4))