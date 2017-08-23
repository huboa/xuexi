# aaaaaaaaa
# print('===>')

#语法错误
# if :pass
# def func:pass


#逻辑错误
# TypeError
# for i in 3:
#     pass

# NameError
# aaaaa

# ValueError
# int('asdfsadf')

#IndexError
# l=[1,2]
# l[1000]

#KeyError
# d={'a':1}
# d['b']

# AttributeError
# class Foo:pass
#
# Foo.x



# try:
#     f=open('a.txt')
#     next(f)
#     next(f)
#     next(f)
#     next(f)
#     next(f)
#     next(f)
#     next(f)
# except StopIteration as e:
#     pass
#
#
# print('====>')



# try:
#     # aaaa
#     print('==-==>1')
#     l=[]
#     l[3]
#     print('==-==>2')
#     d={}
#     d['x']
#     print('==-==>3')
# except NameError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)

#
# try:
#     # aaaa
#     print('==-==>1')
#     l=[]
#     l[3]
#     print('==-==>2')
#     d={}
#     d['x']
#     print('==-==>3')
# except Exception as e:
#     print(e)



# try:
#     aaaa
#     print('==-==>1')
#     # l=[]
#     # l[3]
#     # print('==-==>2')
#     # d={}
#     # d['x']
#     # print('==-==>3')
# except NameError as e:
#     print(e)
# except IndexError as e:
#     print(e)
# except KeyError as e:
#     print(e)
# except Exception as e:
#     print(e)
# else:
#     print('在没有错误的时候执行')
# finally:
#     print('无论有无错误，都会执行')



# raise TypeError('----')


# class EgonException(BaseException):
#     def __init__(self,msg):
#         self.msg=msg
#     def __str__(self):
#         return '<%s>' %self.msg
#
# raise EgonException('egon 的异常')



# l=[1,2,3]
# assert len(l) > 3


#什么时候用try ...except
#错误一定会发生，但是无法预知错误发生条件