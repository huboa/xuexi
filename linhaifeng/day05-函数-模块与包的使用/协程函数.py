#yield:
#1: 把函数的执行结果封装好

# def func(count):
#     print('start')
#     while True:
#         yield count
#         count+=1
#
# g=func(10)
# print(next(g))
# print(next(g))


#yield 的表达式形式的应用
def eater(name):
    print('%s start to eat' %name)
    while True:
        food=yield
        print('%s eat %s' %(name,food))

zsc_g=eater('zsc')
print(next(zsc_g))
print(next(zsc_g))