a=abs(-10)
print(a)
b=abs
print(b(-10))

####map
def f(x):
    return x * x  * x
print(list(map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])))
##reduce 求和
from functools import reduce
def add(x,y):
    return x + y
print(reduce(add, [1, 3, 5, 7, 9]))

###reduce
def fn(x, y):
   return x*100 + y
print(reduce(fn, [1, 3, 5, 7, 9]))

def fn(x, y):
    return x * 10 + y
def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
print(char2num)
print(reduce(fn, map(char2num, '135798')))
from functools import reduce

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))
print(str2int("123"))

####首字母大写
def normalize(LL):
    return LL[0].upper() + LL[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)

from functools import reduce

def str2float(s):
    j,k = s.split('.')
    return str2int(j) + str2dot(k)

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))

def str2dot(s):
    return reduce(lambda x, y: x * 10 + y, map(char2num, s))/10**len(s)