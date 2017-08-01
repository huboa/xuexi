###开放封闭原则：对扩展是开放的，对修改是封闭的

#2 装饰器： 装饰函数的工具，目的是添加新功能
##装饰器本身可以是任意可调用对象，被装饰的对象本身也可以是任意可调用对象
#2.1 装饰器的遵循原则：不修改被调用对象源代码，不修改被调用对象的调用方式
#2.2 装饰器的目的是： 在遵循1，2 的前提下添加新功能
# import time
#
# def timmer(func):
#     #func=index
#     def wrapper(*args,**kwargs):
#
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print("run time is %s" %(stop-start))
#         return res
#     return wrapper
#
# @timmer   #index=timmer(index)
# def index():
#     time.sleep(3)
#     print('welcom to index')
#     return 123
#
#
# @timmer   #home=timmer(home)
# def home(name):
#     time.sleep(2)
#     print('welcom to home page %s'%name)
#
#
# print(index())
# print(home('egon'))


###无参数装饰器
current_user={'user':None}

def auth(func):
    #func=index
    def wrapper(*args,**kwargs):
        if current_user['user']:
            return func(*args,**kwargs)

        name=input("name: ").strip()
        password=input('password:' ).strip()
        with open('db.txt',encoding='utf-8') as f:
            user_dic = eval(f.read())
        if name  in  user_dic and password == user_dic[name]:
            res=func(*args,**kwargs)
            current_user['user']=name

            return res
    return wrapper

@auth
def tprint():
    print("pass ok")


tprint()

###有参数认证

###
from functools import wraps

###补充 wraper
#def timmer(func):
#    @wraps(func)

##补充可以多个 装饰器