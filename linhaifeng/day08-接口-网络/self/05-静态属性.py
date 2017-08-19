##类里面 把功能变成属性
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height = height
    @property
    def bmi(self):
        return self.weight /(self.height**2)
p=People('zsc',75,1.80)
p.height=1.8
print(p.bmi)
# print(p.bmi())

###可以增删改查


###反射的应用

class Ftpserver:
    def __init__(self,host,port):
        self.host=host
        self.port=port
    def run(self):
        while True:
            cmd=input('>>:').strip()
            if not cmd:continue
            if hasattr(self,cmd):
                func=getattr(self,cmd)
                func
    def get(self):
        print('get func')
    def put(self):
        print('put func')
f=Ftpserver('10.199.3.193',21)