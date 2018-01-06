class Foo:
    x=1
    def __init__(self,name):
        self.name=name

    def f1(self):
        print('from f1')


# print(Foo.x) #Foo.__dict__['x']

f=Foo('egon')
# print(f.__dict__)
#
# #1:
# print(f.name)

#2:
# print(f.__dict__['name'])

#hasattr
# print(hasattr(f,'name')) #f.name
# print(hasattr(f,'f1')) #f.f1
# print(hasattr(f,'x')) #f.x


#setattr
# setattr(f,'age',18)#f.age=18

#getattr
# print(getattr(f,'name'))#f.name
# print(getattr(f,'abc',None))#f.abc
# print(getattr(f,'name',None))#f.abc

# func=getattr(f,'f1')#f.f1
# print(func)
# func()
#

#delattr
# delattr(f,'name')# del f.name
# print(f.__dict__)



class Ftpserver:
    def __init__(self,host,port):
        self.host=host
        self.port=port

    def run(self):
        while True:
            cmd=input('>>: ').strip()
            if not cmd:continue
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func()
    def get(self):
        print('get func')

    def put(self):
        print('put func')




f=Ftpserver('192.168.1.2',21)
f.run()




