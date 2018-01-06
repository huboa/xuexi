# pythons=['alex','egon','yuanhao','wupeiqi','gangdan','biubiu']
# linuxs=['wupeiqi','oldboy','gangdan']
#
# res=[]
# for p in pythons:
#     if p in linuxs:
#         res.append(p)
#
# print(res)
#关系运算？？？


#1 集合内可以有多个元素，但是每个元素都必须是不可变类型，即可hash类型
#2 集合内的元素唯一
#3 集合是无序的
# s={1,'a',1,1,1,1,1,1} #s=set({1,'a',1,1,1,1,1,1})


# s1=set('hello')
# print(s1,type(s1))
# s={'a',3,9,'b'}
# print(s)

#集合优先掌握的方法
# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}

# print('alex' not in pythons)
# print(pythons)

#关系运算
s1={1,10,11,22}
s2={1,11,33}

#交集
# print(s1 & s2)

#并集
# print(s1 | s2)

#差集
# print(s1 - s2)
# print(s2 - s1)

#对称差集
print(s1 ^ s2)



#父集
# s1={1,2,3,4}
# s2={1,5}
# print(s1 >= s2)
#
# #子集
# print(s1 <= s2)
# print(s2 <= s1)


#集合练习一

# pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
# linuxs={'wupeiqi','oldboy','gangdan'}
#
#
# # 1. 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# # 　　2. 求出所有报名的学生名字集合
# print(pythons | linuxs)
# # 　　3. 求出只报名python课程的学员名字
# print(pythons - linuxs)
# # 　　4. 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)



#集合练习二：
#  1. 有列表l=['a','b',1,'a','a']，列表元素均为可hash类型，去重，得到新列表,且新列表无需保持列表原来的顺序
# l=['a','b',1,'a','a']
#
# s=set(l)
# print(s)
# print(list(s)
# )


# 　　 2.在上题的基础上，保存列表原来的顺序
# l=['a','b',1,'a','a']
#
# l1=[]
# for item in l:
#     if item not in l1:
#         l1.append(item)
# print(l1)
#
# l1=[]
# s=set()
# for item in l:
#     if item not in s:
#         s.add(item) #{'a','b',1}
#         # l1.append(item)
#         l1.append(item)
#
# print(l1)

# 　　
# 　　 4.有如下列表，列表元素为不可hash类型，去重，得到新列表，且新列表一定要保持列表原来的顺序
#
# l=[
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'alex','age':73,'sex':'male'},
#     {'name':'egon','age':20,'sex':'female'},
#     {'name':'egon','age':18,'sex':'male'},
#     {'name':'egon','age':18,'sex':'male'},
# ]
#
# l1=[]
# for item in l:
#     if item not in l1:
#         l1.append(item)
# print(l1)




# l1=[]
# s=set()
# for item in l:
#     val=(item['name'],item['age'],item['sex'])
#     # print(val)
#     if val not in s:
#         s.add(val)
#         # print(val)
#         l1.append(item)
#
# print(l1)





#集合的内置方法
pythons={'alex','egon','yuanhao','wupeiqi','gangdan','biubiu'}
linuxs={'wupeiqi','oldboy','gangdan'}
# 1. 求出即报名python又报名linux课程的学员名字集合
# print(pythons & linuxs)
# print(pythons.intersection(linuxs))

# 　　2. 求出所有报名的学生名字集合
# print(pythons | linuxs)
# print(pythons.union(linuxs))
# 　　3. 求出只报名python课程的学员名字
# print(pythons - linuxs)
# print(pythons.difference(linuxs))
# 　　4. 求出没有同时这两门课程的学员名字集合
# print(pythons ^ linuxs)
# print(pythons.symmetric_difference(linuxs))

s={1,2,3,'a'}
# s.add(4)
# print(s)

# print(s.pop())

# s.remove('a')
# print(s)

# s.remove('vvvvvvvvvv')
# s.discard('aaaaaa')
# print(s)

