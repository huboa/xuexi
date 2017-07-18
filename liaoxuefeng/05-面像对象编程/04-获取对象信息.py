
##type  types
def fn():
    pass
print(type(fn))  ##查看类型
import types

###查看不同类形
print(type(fn)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print( type((x for x in range(10)))==types.GeneratorType)

###使用isinstance()
##对于class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()函数

print(isinstance('abbbb', str))
print(isinstance(123, int))
print(isinstance(b'a', bytes))

###并且还可以判断一个变量是否是某些类型中的一种，比如下面的代码就可以判断是否是list或者tuple：
print(isinstance([1, 2, 3], (list, tuple)))
print(isinstance((1, 2, 3), (list, tuple)))


##如果要获得一个对象的所有属性和方法，可以使用dir()函数
print(dir("abc"))