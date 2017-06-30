###显示奇数
def is_odd(n):
    return n % 2 == 1
print(is_odd(3))
print(list(filter(is_odd,[1, 2, 4, 5, 6, 9, 10, 15])))
###去除空行
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty, ['A', '', 'B', None, 'C', ' '])))

###大小写排序
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower))
###倒叙
print(sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True))

def by_name(t):
    return t[0]

L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L,key = by_name)
print(L2)

def by_score(t):
    return t[1]

L=[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
L2 = sorted(L,key = by_score,reverse = True)
print(L2)

import sys