
###反射的应用类

hasattr()
getattr()
setattr()
delattr()


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
                func()
    def get(self):
        print('get func')
    def put(self):
        print('put func')
f=Ftpserver('10.199.3.193',21)

f.run()