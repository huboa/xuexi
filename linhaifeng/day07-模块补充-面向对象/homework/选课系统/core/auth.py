import pickle,json,os,sys
def auth(func):
    def wrapper(*args,**kwargs):
        name=input('name:').strip()
        password=input('password:').strip()
        dic = json.load(open('../db/user.json', 'r'))
        if name in dic and password == dic[name]["password"]:

            res=func(*args,**kwargs)
            return res
        else:
            print('user or passwd error')
    return wrapper

@auth
def foo(name):
    print(name)

while True:
    foo('认证OK')



#
# with open ('../db/user.json','w') as f:
#     f.write(json.dumps(dic))

