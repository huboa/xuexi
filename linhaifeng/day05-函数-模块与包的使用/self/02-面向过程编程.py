###面向过程：核心是过程二字，过程既解决问题的步骤，基于面向过程去设计程序
##一条工业流水线，是一种机械式思维方式
###优点：程序结构清晰，把复杂问题简单化，流程化
#缺点：可扩展性差，一条流水线只能解决一个问题
#应用场景：linux内核，git httpd shell 脚本

##grep -rl 'error' /dir/


##第一阶段：找到文件的绝对路径

##第二阶段 ：打开文件

##第三阶段：循环读出每一行内容

##第四阶段： 过滤

##第五阶段： 打印文件名


import os

def init(func):
    def wrapper(*args,**kwargs):
        g=func(*args,**kwargs)
        next(g)
        return g
    return wrapper

@init
def search(filepath):
    while True:
        g=os.walk(filepath)

        for pardir,_,files in g:
            for file in files:
                abspath=r'%s\%s' %(pardir,file)
                opener().send(abspath)


###打开文件
@init
def opener():
    while True:
        abspath=yield
        with open(abspath) as f:


###循环读取
@init
def cat(target):
    while True:
        f=yield
        for line in f:
            target.send(line)


 ##第四阶段
@init
def grep(pattern):

    while True:
        line=yield
        if pattern in line:
            print(line)


g = search()
g.send(\)

def print():
    while True:
