import time

# current_user={'user':None}
# def auth(auth_type='file'):
#     def deco(func):
#         def wrapper(*args, **kwargs):
#             if auth_type == 'file':
#                 if current_user['user']:
#                     return func(*args, **kwargs)
#                 name = input('name: ').strip()
#                 password = input('password: ').strip()
#
#                 with open('db.txt', encoding='utf-8') as f:
#                     user_dic = eval(f.read())
#                 if name in user_dic and password == user_dic[name]:
#                     res = func(*args, **kwargs)
#                     current_user['user'] = name
#                     return res
#                 else:
#                     print('user or password error')
#             elif auth_type == 'mysql':
#                 print('mysql')
#
#             elif auth_type == 'ldap':
#                 print('ldap')
#             else:
#                 print('not valid auth_type')
#         return wrapper
#     return deco
#
# @auth('file')
# def main():
#     print("aut")



def timmer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)
        stop=time.time()
        print('run time is %s' %(stop-start))
        return res
    return wrapper


# @timmer # index=timmer(index)
# def index():
#     time.sleep(1)
#     print('welcome to index')
#     return "from index return"

@timmer # home=timmer(home)
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)

# res=index() #res=wrapper()
# print(res)

res1=home('egon') #wrapper('egon')
print(res1)