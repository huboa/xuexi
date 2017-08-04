#面向过程：核心是过程二字，过程即解决问题的步骤，基于面向过程去设计程序就像是在设计
# 一条工业流水线，是一种机械式的思维方式

#优点：程序结构清晰，可以把复杂的问题简单化，流程化
#缺点：可扩展性差，一条流线只是用来解决一个问题
#应用场景：linux内核，git，httpd，shell脚本

#grep -rl 'error' /dir/
import os
def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

#第一阶段：找到所有文件的绝对路径
@init
def search(target):
    while True:
        filepath=yield
        g=os.walk(filepath)
        for pardir,_,files in g:
            for file in files:
                abspath=r'%s\%s' %(pardir,file)
                target.send(abspath)
# search(r'C:\Users\Administrator\PycharmProjects\python18期周末班\day5\aaa')
# g=search()
# g.send(r'C:\Python27')

#第二阶段：打开文件
@init
def opener(target):
    while True:
        abspath=yield
        with open(abspath,'rb') as f:
            target.send((abspath,f))




#第三阶段：循环读出每一行内容
@init
def cat(target):
    while True:
        abspath,f=yield #(abspath,f)
        for line in f:
            res=target.send((abspath,line))
            if res:break



#第四阶段：过滤
@init
def grep(pattern,target):
    tag=False
    while True:
        abspath,line=yield tag
        tag=False
        if pattern in line:
            target.send(abspath)
            tag=True


#第五阶段：打印该行属于的文件名
@init
def printer():
    while True:
        abspath=yield
        print(abspath)

g = search(opener(cat(grep('os'.encode('utf-8'), printer()))))
# g.send(r'C:\Users\Administrator\PycharmProjects\python18期周末班\day5\aaa')

g.send(r'D:\data\git\xuexi\linhaifeng\day05-函数-模块与包的使用\self')
#a1.txt,a2.txt,b1.txt