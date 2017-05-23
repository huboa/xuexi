# classmates = ['Michael', 'Bob', 'Tracy']
# print(classmates)
# print(len(classmates))
# print(classmates[0],classmates[2],classmates[-1],classmates[-2])
# classmates.insert(1,'zsc')
# print(classmates)
# classmates.pop()
# classmates.pop(0)
# print(classmates)
# classmates[1]="zsc2"
# print(classmates)
#
# classlevel = ['leve1','level1-2',classmates]
# print(classlevel,len(classlevel))
#
# L = [
#     ['Apple', 'Google', 'Microsoft'],
#     ['Java', 'Python', 'Ruby', 'PHP'],
#     ['Adam', 'Bart', 'Lisa']
# ]
# print(L[0][0],L[1][1],L[2][2])
##if
# age = 2
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# elif age >=6 :
#     print('your age is', age)
#     print('teenager')
# else:
#     print('kid')
#
# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
#
# height=1.75
# weight=80.5
# bmi=weight/(height/weight)
# if bmi < 18.5:
#     print("too light")
# elif bmi <= 25:
#     print("stand")
# elif bmi <= 28:
#     print("too weight")
#
# else:
#     print("没法要了")
#
#
# names = ['Michael', 'Bob', 'Tracy',['Michael', 'Bob', 'Tracy']]
# for name in names[3]:
#     print(name)
###t
sum = 0
for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
    sum = sum + x
print(sum)

###
d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'],d['Bob'])
d.pop('Bob')
print(d.get('Thomas'))
print('Thomas' in d )
print(d)
d = {
    'Michael': 95,
    'Bob': 75,
    'Tracy': 85
}
print('d[\'Michael\'] =', d['Michael'])
print('d[\'Bob\'] =', d['Bob'])
print('d[\'Tracy\'] =', d['Tracy'])
print('d.get(\'Thomas\', -1) =', d.get('Thomas', -1))


##set集合
s = set([1, 2, 3])
print(s)