# ##dict-字典
# d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
# print(d['Michael'],d['Bob'])
# print("Bob-dect=",d.get('Bob'))
# d.pop('Bob')
# print("Bob-dect=",d.get('Thomas'))
# print('Thomas' in d )
#
# print(d)
# d = {
#     'Michael': 95,
#     'Bob': 75,
#     'Tracy': 85
# }
# print('d[\'Michael\'] =', d['Michael'])
# print('d[\'Bob\'] =', d['Bob'])
# print('d[\'Tracy\'] =', d['Tracy'])
# print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))

# ##set集合
###集合的添加删除
s = set([1, 2, 3])
print(s)
s.add(5)
print(s)
s.remove(2)
print(s)
####集合的并集交集
s1=set([1,2,3,5])
print(s1)
s2=set([2,4,6])
print(s1 & s2)
print(s1|s2)

####不可变对象
##sort
a = ['c', 'b', 'a']
a.sort()
print(a)

a = 'abc'
a.replace('a','A')
print(a)
b = a.replace('a', 'A')
print(b)

