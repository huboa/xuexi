#迭代：是一个重复的过程，每一次重复，都是基于上一次的结果而来
# while True: #单纯的重复
#     print('你瞅啥')

# l=['a','b','c','d']
# count=0
# while count < len(l):
#     print(l[count])
#     count+=1

dic={'name':'egon','sex':'m',"age":18} #上述按照索引的取值方式，不适于没有索引的数据类型

#迭代器：
#可迭代对象iterable：凡是对象下有__iter__方法：对象.__iter__，该对象就是可迭代对象
# s='hello'
# l=['a','b','c','d']
# t=('a','b','c','d')
# dic={'name':'egon','sex':'m',"age":18}
# set1={1,2,3}
# f=open('db.txt')

# s.__iter__()
# l.__iter__()
# t.__iter__()
# dic.__iter__()
# set1.__iter__()
# f.__iter__()


#迭代器对象：可迭代对象执行内置的__iter__方法，得到的结果就是迭代器对象

# dic={'name':'egon','sex':'m',"age":18}
#
# i=dic.__iter__()
# # print(i) #iterator迭代器
#
# # i.__next__() #next(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)) #StopIteration
#
# l=['a','b','c','d']
#
# i=l.__iter__()
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i)) #StopIteration




#不依赖于索引的取值方式
# l=['a','b','c','d']
# dic={'name':'egon','sex':'m',"age":18}
# iter_l=iter(l)
# iter_dic=iter(dic)
# while True:
#     try:
#         # print(next(iter_l))
#         k=next(iter_dic)
#         print(k,dic[k])
#     except StopIteration:
#         break


#什么是迭代器对象：
#1 有__iter__,执行得到仍然是迭代本身
#2 有__next__


#迭代器对象的优点
#1：提供了一种统一的（不依赖于索引的）迭代方式
#2：迭代器本身，比起其他数据类型更省内存
# l=['a','b','c','d']
# i=iter(l)

# dic={'a':1,'b':2}
# x=dic.keys()
# print(x)
# i=x.__iter__()
#
# with open('a.txt') as f:
#     # print(next(f))
#     # print(next(f))
#     # print(next(f))
#     f.read()


#迭代器对象的缺点
#1:一次性，只能往后走，不能回退，不如索引取值灵活
#2：无法预知什么时候取值结束，即无法预知长度
# l=['a','b','c','d']
# i=iter(l)
# print(next(i))
# print(next(i))
# print(next(i))


#for循环原理

#
# l=['a','b','c','d']
# for item in l: #iter_l=l.__iter__()
#     print(item)


# for item in {1,2,3,4}:
#     print(item)


# with open('a.txt') as f:
#     # for line in f: #i=f.__iter__()
#     #     print(line)
#     print(f is f.__iter__())





#补充：判断可迭代对象与迭代器对象(了解)

from collections import Iterable,Iterator
s='hello'
l=['a','b','c','d']
t=('a','b','c','d')
dic={'name':'egon','sex':'m',"age":18}
set1={1,2,3}
f=open('a.txt')


# print(isinstance(s,Iterable))
# print(isinstance(l,Iterable))
# print(isinstance(t,Iterable))
# print(isinstance(dic,Iterable))
# print(isinstance(set1,Iterable))
# print(isinstance(f,Iterable))

print(isinstance(s,Iterator))
print(isinstance(l,Iterator))
print(isinstance(t,Iterator))
print(isinstance(dic,Iterator))
print(isinstance(set1,Iterator))
print(isinstance(f,Iterator))