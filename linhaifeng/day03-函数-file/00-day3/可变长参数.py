#可变长参数指的是实参的个数多了
#实参无非位置实参和关键字实参两种

#形参必须要两种机制来分别处理按照位置定义的实参溢出的情况：*
#跟按照关键字定义的实参溢出的情况：**

# def foo(x,y,*args): #nums=(3,4,5,6,7)
#     print(x)
#     print(y)
#     print(args)

# foo(1,2,3,4,5,6,7) #*
# foo(1,2) #*



#*args的扩展用法
# def foo(x,y,*args): #*args=*(3,4,5,6,7)
#     print(x)
#     print(y)
#     print(args)
#
# # foo(1,2,3,4,5,6,7) #*
#
#
# foo(1,2,*(3,4,5,6,7)) #foo(1,2,3,4,5,6,7)


# def foo(x,y=1,*args): #
#     print(x)
#     print(y)
#     print(args)
#
# # foo('a','b',*(1,2,3,4,5,6,7)) #foo('a','b',1,2,3,4,5,6,7)
# # foo('egon',10,2,3,4,5,6,9,y=2) #报错
# foo('egon',10,2,3,4,5,6,9)




# def foo(x,y,**kwargs): #nums={'z':3,'b':2,'a':1}
#     print(x)
#     print(y)
#     print(kwargs)
# foo(1,2,z=3,a=1,b=2) #**


# def foo(x,y,**kwargs): #kwargs={'z':3,'b':2,'a':1}
#     print(x)
#     print(y)
#     print(kwargs)
#
# foo(1,2,**{'z':3,'b':2,'a':1}) #foo(1,2,a=1,z=3,b=2)


# def foo(x, y):  #
#     print(x)
#     print(y)
#
# foo(**{'y':1,'x':2})  # foo(y=1,x=2)





# def foo(x,*args,**kwargs):#args=(2,3,4,5) kwargs={'b':1,'a':2}
#     print(x)
#     print(args)
#     print(kwargs)
#
#
# foo(1,2,3,4,5,b=1,a=2)


#这俩东西*args，**kwargs干甚用？？？
def register(name,age,sex='male'):
    print(name)
    print(age)
    print(sex)


# def wrapper(*args,**kwargs): #args=(1,2,3) kwargs={'a':1,'b':2}
#     # print(args)
#     # print(kwargs)
#     register(*args,**kwargs)
#     # register(*(1, 2, 3),**{'a': 1, 'b': 2})
#     # register(1, 2, 3,a=1,b=2)
#
#
# wrapper(1,2,3,a=1,b=2)

import time

# def register(name,age,sex='male'):
#     # start_time=time.time()
#     print(name)
#     print(age)
#     print(sex)
#     time.sleep(3)
    # stop_time=time.time()
    # print('run time is %s' %(stop_time-start_time))

# def wrapper(*args, **kwargs): #args=('egon',) kwargs={'age':18}
#     start_time=time.time()
#     register(*args, **kwargs)
#     stop_time=time.time()
#     print('run time is %s' %(stop_time-start_time))
#
#
# wrapper('egon',age=18)

# register('egon',18)










#命名关键字参数:  在*后面定义的形参称为命名关键字参数，必须是被以关键字实参的形式传值
# def foo(name,age,*args,sex='male',group):
#     print(name)
#     print(age)
#     print(args)
#     print(sex)
#     print(group)
#
# foo('alex',18,19,20,300,group='group1')





def foo(name,age=18,*args,sex='male',group,**kwargs):
    pass
