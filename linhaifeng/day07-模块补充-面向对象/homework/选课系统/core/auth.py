import pickle,json
def auth(func):
    def wrapper(*args,**kwargs):
        if True:
            res=func(*args,**kwargs)
            return res
    return wrapper

@auth
def foo(name):
    print(name)

foo(123)

dic=json.load(open('../db/user.json','r'))
print(dic)
#
# with open ('../db/user.json','w') as f:
#     f.write(json.dumps(dic))

print(dic['zsc'])