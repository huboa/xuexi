#优点：使用源文件内的名字时无需加前缀，使用方便
#缺点：容易与当前文件的名称空间内的名字混淆
# from spam import money,read1,read2,change
# money=0
# print(money)
# print(read1)
#
# read1()

# def read1():print('ok')
# read2()

#
# money=10
# change()
# print(money)


# from spam import money as m
#
# print(m)




from spam import *

# print(_money)
# read1()
# print(read2)

print(money)
print(x)
print(read1)