#无参装饰器版本
# current_user={'user':None}
# def auth(func):
#     def wrapper(*args,**kwargs):
#         if current_user['user']:
#             return func(*args,**kwargs)
#
#         name=input('name: ').strip()
#         password=input('password: ').strip()
#
#         with open('db.txt', encoding='utf-8') as f:
#             user_dic = eval(f.read())
#         if name in user_dic and password == user_dic[name]:
#             res=func(*args,**kwargs)
#             current_user['user']=name
#             return res
#         else:
#             print('user or password error')
#     return wrapper
#
# @auth #index=auth(index) index=wrapper
# def index():
#     print('from index')
# index()

# @auth
# def home(name):
#     print('welcome %s' %name)

# index() #wrapper()
# home('egon')




#有参装饰器版本
current_user={'user':None}
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
@auth(auth_type='mysql') #@deco  #index=deco(index)
def index():
    print('from index')
@auth(auth_type='file')
def home(name):
    print('welcome %s' %name)
index() #wrapper()
home('egon')




