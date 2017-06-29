##位置参数
##定义一个幂函数
# def power(x):
#     return  x*x
# print(power(4))


# def power(x,n):
#     s =1
#     while n > 0:
#         n = n -1
#         s = s * x
#     return s
# print(power(9,3))


###默认参数
# def power(x,n=2):
#     s =1
#     while n > 0:
#         n = n -1
#         s = s * x
#
#     return s
# print(power(9))


# def enroll(name, gender, age=6, city='Beijing'):
#     print('name:', name)
#     print('gender:', gender)
#     print('age:', age)
#     print('city:', city)
# print(enroll('Sarah', 'F'))
#
# def add_end(L=None):
#     if L is None:
#         L = []
#         L.append('END')
#         return L
# print(add_end())

# ##可变参数+*  可变参数就是传入的参数个数是可变的
# def calc(*numbers):
#     sum = 0
#     for n in numbers:
#         sum = sum + n * n
#     return sum
# print(calc(1,2,3))
#
# nums=[1,2,3,4]
#
# print(calc(*nums))


##关键参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)
print(person('Michael',30))
print(person('Adam', 45, gender='M', job='Engineer'))


##*args是可变参数，args接收的是一个tuple；
#**kw是关键字参数，kw接收的是一个dict。

##添加默认值的变量传参
def person(name, age, *, city='Beijing', job):
    print(name, age, city, job)

#由于命名关键字参数city具有默认值，调用时，可不传入city参数：
person('Jack', 24, job='Engineer')

##组合参数

def f1(a, b, c=0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f1(1,2,c=3)
f1(1,2,3,'a','b')
f1(1,2,3,'a','b',x=99)
f1(1,2,3,x=99)

###函数也可以调用tuple dict
args = (1, 2, 3, 4)
kw = {'d': 99, 'x': '#'}
f1(*args, **kw)
#
args = (1, 2)
kw = {'d': 88, 'x': '#'}

f2(*args, **kw)


