
##如果给定一个list或tuple，我们可以通过for循环来遍历这个list或tuple，这种遍历我们称为迭代（Iteration）。
# LL=range(100)
# for n in LL:
#     print(n)

###字典diedaik可以迭代key value both
d = {'a': 1, 'b': 2, 'c': 3}

for key in d:
    print(key)

for v in d.values():
     print(v)

for k,v in d.items():
    print(k,v)

###循环下标
ll=['A', 'B', 'C']
for i, value in enumerate(ll):
     print(i,value)
for x, y in [(1, 1), (2, 4), (3, 9)]:
    print(x,y)