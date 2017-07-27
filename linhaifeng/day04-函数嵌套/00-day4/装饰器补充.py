#补充一：wraps

# import time
# from functools import wraps
#
# def timmer(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         start=time.time()
#         res=func(*args,**kwargs)
#         stop=time.time()
#         print('run time is %s' %(stop-start))
#         return res
#     return wrapper
#
#
# @timmer # index=timmer(index)
# def index():
#     '''这是index函数'''
#     time.sleep(3)
#     print('welcome to index')
#     return 123
#
# print(index.__doc__)
# # print(help(index))



#补充二：一个函数头顶上可以多个装饰器
import time
from functools import wraps
current_user={'user':None}

def timmer(func):
    @wraps(func)
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        stop=time.time()
        print('run time is %s' %(stop-start))
        return res
    return wrapper
def auth(auth_type='file'):
    def deco(func):
        def wrapper(*args, **kwargs):
            if auth_type == 'file':
                if current_user['user']:
                    return func(*args, **kwargs)
                name = input('name: ').strip()
                password = input('password: ').strip()

                with open('db.txt', encoding='utf-8') as f:
                    user_dic = eval(f.read())
                if name in user_dic and password == user_dic[name]:
                    res = func(*args, **kwargs)
                    current_user['user'] = name
                    return res
                else:
                    print('user or password error')
            elif auth_type == 'mysql':
                print('mysql')

            elif auth_type == 'ldap':
                print('ldap')
            else:
                print('not valid auth_type')
        return wrapper
    return deco



@timmer #index=timmer(wrapper)
@auth() # @deco #index=deco(index) #wrapper
def index():
    '''这是index函数'''
    time.sleep(3)
    print('welcome to index')
    return 123

# print(index.__doc__)
# print(help(index))

index()












