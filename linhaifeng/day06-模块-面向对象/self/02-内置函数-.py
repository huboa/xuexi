# ##绝对值
# print(abs(-1))
# ###可迭代对象
# print(all([1,2,'a',None]))
#
# ##bool 值为假的情况：None,空 ，0 ，False
# print(any([]))
# print(any(['',None,False])) ##True
# print(any([' ',None,False]))#False
#
#
# #bin，October，hex
# print(bin(10))
# print(oct(10))
# print(hex(10))
#
#
# #bytes
# #unicode---encodee---bytes
# print('hell0'.encode("utf-8"))
# print(bytes('hell0'.encode("utf-8")))
#
# ###callable
#
# #chr,ord
# print(chr(65))
# print(chr(90))
# print(ord("A"))
#
# ##数据类型内置函数，又被称为工厂函数
# int
# x=1 #x=int(1)
# print(type(x))
# complex
# float
#
# str
# list
# tuple
# dict
#
# set
# frozenset  #不可变
#
# s={1,2,3,4}#s=set({1,2,3,4})
# s1=frozenset({1,2,3,4})
#
#
#

#
# ##compile
# # delattr()
# # hasattr()
# # setattr()
# # getattr()
#
# ##dir
# import sys
# print(sys.path)
# print(sys.argv)
# print(dir(sys))
#
# ###divmod
# print(divmod(10,3))
# print(divmod(101,30))
# print(divmod(100,10))
#
# ##ennumerate
# l=['a','b','c']
# res=enumerate(l)
# for n  in res:
#     print(n)
#
# for index,value in enumerate(l):
#     print(index,value)
#
# ##globals,locals ## 查看全局作用域和局部作用域
# print(globals())
#
# ##hash
# print(hash('hasd'))
#
# ###给函数加文档用引号#号
# def func():
#     '''
#     test
#     '''
#     pass
#
# print(help(func))

##id 是python 解释器的一种实现
# x=1
# print(id(x))
#
# def func():pass
# print(id(func()))
# print(func)
#
# ##isinstance
# x=1
# print(type(x) is int)
# print(isinstance(x,int))
#
#
# ##迭代器
# # iter()
# # next()
#
# #len
# #max
# print(max([1,2,34]))
# print(min([1,2,34]))

# ##面向对象
# classmethod
# staticmethod
# property

#ininstance

##filter,map,reduce
##max min sorted

##pow 平方取模数
# print(pow(32,2))
#
# ##range
# #repr:对象转字符串
# ##reversed
# l=[1,"a",2,"c"]
# print(list(reversed(l)))
# print(l)
#
# ##round
# print(round(3.356,2))
# print(round(3.356,1))
#
# ##slice
# l=[1,2,3,4,5,6]
# print(l[0:4:2])
# s=slice(0,4,2)
# print(l[s])

###sorted
# l=[1,10,4,3,-1]
# print(sorted(l,reverse=True))
# print(sorted(l))

###sum

# print(sum)
#
# #vars
# import m1
# print(vars(m1) == m1.__dict__)

##zip 拉链
s='hello'
l=[1,2,3,4,5,6]
print(list(zip(s,l)))

##__import__
import sys
#
# m_name=input('module>>:')
# if m_name='sys':
#     m=__import__(m_name)



