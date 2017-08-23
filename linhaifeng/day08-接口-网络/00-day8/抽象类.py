import abc
class Interface(metaclass=abc.ABCMeta):#定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
    all_type='file'
    @abc.abstractmethod
    def read(self): #定接口函数read
        pass

    @abc.abstractmethod
    def write(self): #定义接口函数write
        pass


class Txt(Interface): #文本，具体实现read和write
    def read(self):
        pass

    def write(self):
        pass
t=Txt()

print(t.all_type)

