##迭代：是一个重复的过程，每次重复，都是基于上次结果而来
##while True:单纯的重复
##     print()
# l=['a','b','c']
# count=0
# while count < len(l):
#     print(l[count])
#     count+=1
#

##迭代器
#可迭代对象： 凡是对象下有__iter__方法：
# s='hello'
# l=['a','b','c']
# t=('a','b','c')
# dic={'name':'zsc',"sex":"m",'age':18}
# i=dic.__iter__()
# print(dic.__iter__())##iterator 迭代器
# print(next(i))
# print(next(i))
# print(next(i))

#
# l_iter=iter(l)
# while True:
#     try:
#          print(next(l_iter))
#     except StopIteration:
#         break

# dic_iter=iter(dic)
# while True:
#     try:
# #        print(next(dic_iter))
#         k=next(dic_iter)
#         print(k,dic[k])
#     except StopIteration:
#         break

#什么是迭代器对象
#1 有__iter__,执行得到仍然是迭代本身
#2 有__next__
####迭代器对象的优点
# 提供了一种统一的（不依赖索引的）迭代方式
## 迭代器本身，比其他数据类型更省内存

####缺点
#1：一次性，只能往后走，不能回退，不如索引灵活
#2：有索引可以取长度，迭代长度，无法预知结束时间

#for 循环原理
# for item in dic:
#     print(item,dic[item])


s='hello'
l=['a','b','c']
t=('a','b','c')
dic={'name':'zsc',"sex":"m",'age':18}
##补充迭代器
print(isinstance(dic,Iterator))