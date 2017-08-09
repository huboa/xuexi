def func(x,y,z=1):
    return x+y+z

# print(func)
# print(func(1,2,3))

#匿名函数:1. 没有名字 2：函数体自带return
# print(lambda x,y,z=1:x+y+z)

f=lambda x,y,z=1:x+y+z
print(f)
print(f(1,2,3))

# x=1
# 1
# print(x)
# print(1)

#匿名函数的应用场景：
#应用于一次性的场景，临时使用