# print(abs(-1))
#
# print(all([1,2,'a',None]))
# print(all([]))

#bool值为假的情况：None，空，0，False


# # print(any([]))
# print(any([' ',None,False])) #True
# print(any(['',None,False])) #False
# print(any(['',None,False,1])) #True
#

#bin,oct,hex
# print(bin(10))
# print(oct(10))
# print(hex(10))

#bytes
#unicode----encode----->bytes
# print('hello'.encode('utf-8'))
# print(bytes('hello',encoding='utf-8'))

#callable
# print(callable(bytes))
# print(callable(abs))


#chr,ord
# print(chr(65))
# print(chr(90))
#
# print(ord('#'))



#内置函数，又被称为工厂函数
# int
# x=1 #x=int(1)
# print(type(x))
# x=int(2)


complex
float

str
list
tuple
dict

set #可变集合
frozenset #不可变集合

# s={1,2,3,4} #s=set({1,2,3,4})
# print(type(s))
#
# s1=frozenset({1,2,3,4})
# print(type(s1))



#dir
# import sys
# # sys.path
# # sys.argv
# print(dir(sys))


#divmod
# print(divmod(10,3))
# print(divmod(102,20))


#enumerate
# l=['a','b','c']
# res=enumerate(l)
# for i in res:
#     print(i)
# for index,item in enumerate(l):
#     print(index,item)



#globals,locals #查看全局作用域和局部作用域
# print(globals())


#hash
# print(hash('abcdefg123'))
# print(hash('abcdefg123'))
# print(hash('abcdefg123'))
# print(hash('abcdefg123'))


#给函数加文档解释，用到单引号，双引号，三引号
def func():
    # '''
    # test function
    # :return:
    # '''
    pass

# print(help(func))

#id:是python解释器实现的功能，只是反映了变量在内存的地址
#但并不是真实的内存地址
# x=1
# print(id(x))

# def func():pass
# print(id(func))
# print(func)


#isinstance
# x=1
# print(type(x) is int)
# print(isinstance(x,int)) #x=int(1)


#迭代器
iter
next

#len
#max
# print(max([1,2,3,10]))
# print(max(['a','b']))
# print(min([1,2,3,10]))

#pow
# print(pow(3,2,2)) #3**2%2

#range

# #repr，str
# print(type(str(1)))
# print(type(repr(1)))


#reversed
# l=[1,'a',2,'c']
# print(list(reversed(l)))
# print(l)


#slice
# l=[1,2,3,4,5,6]
# print(l[0:4:2])
#
# s=slice(0,4,2)
# print(l[s])


#sorted
# l=[1,10,4,3,-1]
# print(sorted(l,reverse=True))

#sum
# print(sum([1, 2,3]))
#
# print(sum(i for i in range(10)))




#vars
# import m1
# print(vars(m1) == m1.__dict__)


#zip:拉链
# s='hellosssssssssssssssss'
# l=[1,2,3,4,5]
#
# print(list(zip(s,l)))

#__import__
import sys

# m_name=input('module>>: ')
# if m_name == 'sys':
#     m=__import__(m_name)
#     print(m)
#     print(m.path)
#
# sys=__import__('sys')
# print(sys)



#round
print(round(3.565,2))
print(round(3.555,2))




#filter,map,reduce 重点
#max min sorted



#面向对象
object

super

# __dict__


isinstance
issubclass


classmethod
staticmethod
property

delattr
hasattr
setattr
getattr







#了解
compile
eval
exec