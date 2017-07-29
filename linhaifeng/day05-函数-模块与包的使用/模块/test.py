##导入模块做了那些事
#1执行源文件
#2以一个源文件的全局名称空间
#3在当前位置拿到一个模块名，指向2创建的名称空间
# import spam
# money = 10000000
# def read1():
#     print('from test')
# print(spam.money)
# print(spam.read1)
# spam.read1()
# spam.read2()
# spam.change()
# print(money)
# spam.read1()

import spam as s1
print(s1.money)