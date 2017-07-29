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
# def eater(name):
#     print('%s start to eat' %name)
#     while True:
#         food=yield
#         print('%s eat %s' %(name,food))
#
# zsc_g=eater('zsc')
# print(next(zsc_g))
# print(next(zsc_g))


#########
# ##用法
# def eater(name):
#     print('%s start to eat' %name)
#     food_list=[]
#     while True:
#         food=yield  food_list
#         food_list.append(food)  ##[保存列表]
#         print('%s eat %s' %(name,food))
#
# zsc_g=eater('zsc')
# # print(next(zsc_g))
# # print(next(zsc_g))
#
# ##第一阶段：初始化
# next(zsc_g)##等于 zsc_g.send(None)
# #zsc_g.send(None)
#
#
# ##第二阶段：给yield 传值
# zsc_g.send('粥')
# print(zsc_g.send('大虾'))


######
##用法
# def eater(name):
#     print('%s start to eat' %name)
#     food_list=[]
#     while True:
#         food=yield  food_list
#         food_list.append(food)  ##[保存列表]
#         print('%s eat %s' %(name,food))
#
#
# def producer():
#
#     zsc_g=eater('zsc')
#     # print(next(zsc_g))
#     # print(next(zsc_g))
#
#     ##第一阶段：初始化
#     next(zsc_g)##等于 zsc_g.send(None)
#     #zsc_g.send(None)
#
#
#     ##第二阶段：给yield 传值
#     while True:
#         food=input(">>: ").strip()
#         if not food:continue
#         print(zsc_g.send(food))
#
#
# producer()


###解决初始化问题加装饰器
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def eater(name):
    print('%s start to eat' %name)
    food_list=[]
    while True:
        food=yield  food_list
        food_list.append(food)  ##[保存列表]
        print('%s eat %s' %(name,food))


def producer():

    zsc_g=eater('zsc')
    while True:
        food=input(">>: ").strip()
        if not food:continue
        print(zsc_g.send(food))


producer()

