class Interface:#定义接口Interface类来模仿接口的概念，python中压根就没有interface关键字来定义一个接口。
    def read(self): #定接口函数read
        pass

    def write(self): #定义接口函数write
        pass


class Txt(Interface): #文本，具体实现read和write
    def read(self):
        print('文本数据的读取方法')

    def write(self):
        print('文本数据的写方法')

class Sata(Interface): #磁盘，具体实现read和write
    def du(self):
        print('硬盘数据的读取方法')

    def write(self):
        print('硬盘数据的写方法')

class Process(Interface):
    def read(self):
        print('进程数据的读取方法')

    def xie(self):
        print('进程数据的写方法')



t=Txt()
s=Sata()
p=Process()


t.read()
s.read()
p.read()