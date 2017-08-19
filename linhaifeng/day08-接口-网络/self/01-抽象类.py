
##继承必须子类有父类的方法
import abc
class interface(metaclass=abc.ABCMeta):
    all_type='file'
    @abc.abstractclassmethod
    def read(self):
        pass

    @abc.abstractclassmethod
    def write(self):
        pass
class Txt(interface):
    def read(self):
        pass
    def write(self):
        pass
t=Txt()
print(t.all_type)