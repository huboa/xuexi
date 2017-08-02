import os,sys
x=1

def func1():
    print('from m1')
def func2():
    print('from m2')
def func3():
    print('from m3')
# print(__name__)
#文件当做脚本运行时__name__等于__main__
#文件当做模块被加载运行时__name__等于模块名
if __name__ == '__main__':
    #当做脚本使用
    func1()
    func2()
    func3()