#这种隐藏需要的问题：
class Foo:
    __N=11111 #_Foo__N
    def __init__(self,name):
        self.__Name=name#self._Foo__Name=name
    def __f1(self):#_Foo__f1
        print('f1')
    def f2(self):
        self.__f1()##self.Foo__f1

f=Foo('zsc')
print(f.__N)
f.__f1()
f.__Name
f.f2()
