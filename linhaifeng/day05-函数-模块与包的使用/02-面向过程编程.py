###面向过程：核心是过程二字，过程既解决问题的步骤，基于面向过程去设计程序
##一条工业流水线，是一种机械式思维方式
###优点：
#缺点：
#应用场景：

##grep -rl 'error' /dir/


##第一阶段：找到文件的绝对路径

##第二阶段 ：打开文件

##第三阶段：循环读出每一行内容

##第四阶段： 过滤

##第五阶段： 打印文件名


import os
def search(filepath):
    l=[]
    g=os.walk(filepath)

    for pardir,-,files in g:
        for file in files:
            abspath=r'%s\%s' %(pardir,file)
            print(abspath)

