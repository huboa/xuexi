#yield:
#1:把函数的执行结果封装好__iter__和__next__，即得到一个迭代器
#2：与return功能类似，都可以返回值，但不同的是，return只能
#返回一次值，而yield可以返回多次值
#3：函数暂停与再继续运行的状态是有yield保存
# def func(count):
#     print('start')
#     while True:
#         yield count
#         count+=1
#
# g=func(10)
# # print(g)
# print(next(g))
#
# print(next(g))



#yield的表达式形式的应用
# def eater(name):
#     print('%s 说：我开动啦' %name)
#     while True:
#         food=yield
#         print('%s eat %s' %(name,food))
#
# alex_g=eater('alex')
# print(alex_g)

# print(next(alex_g))
# print('==============>')
# print(next(alex_g))
# print('==============>')
# print(next(alex_g))

#用法：
# def eater(name):
#     print('%s 说：我开动啦' %name)
#     food_list=[]
#     while True:
#         food=yield food_list
#         food_list.append(food) #['骨头'，'菜汤']
#         print('%s eat %s' %(name,food))
#
# alex_g=eater('alex')
# #第一阶段：初始化
# next(alex_g) #等同于alex_g.send(None)
# print('===========>')
#
# #第二阶段：给yield传值
# print(alex_g.send('骨头')) #1 先给当前暂停位置的yield传骨头 2 继续往下执行，直到再次碰到yield，然后暂停并且把yield后的返回值当做本次调用的返回值
# # print('===========>')
# print(alex_g.send('菜汤'))
# print(alex_g.send('狗肉包子'))













# def eater(name):
#     print('%s 说：我开动啦' %name)
#     food_list=[]
#     while True:
#         food=yield food_list
#         food_list.append(food) #['骨头'，'菜汤']
#         print('%s eat %s' %(name,food))
#
#
# def producer():
#     alex_g=eater('alex')
#     #第一阶段：初始化
#     next(alex_g)
#     #第二阶段：给yield传值
#     while True:
#         food=input('>>: ').strip()
#         if not food:continue
#         print(alex_g.send(food))
#
#
# producer()



#解决初始化问题
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def eater(name):
    print('%s 说：我开动啦' %name)
    food_list=[]
    while True:
        food=yield food_list
        food_list.append(food) #['骨头'，'菜汤']
        print('%s eat %s' %(name,food))

alex_g=eater('alex')
#第二阶段：给yield传值
# print(alex_g.send('骨头')) #1 先给当前暂停位置的yield传骨头 2 继续往下执行，直到再次碰到yield，然后暂停并且把yield后的返回值当做本次调用的返回值
# print('===========>')