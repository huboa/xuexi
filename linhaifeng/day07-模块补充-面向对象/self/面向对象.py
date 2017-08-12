'''
面向过程：核心是过程二字，过程指问题的解决步骤，流水线机械式
优点：复杂的问题流程化，进而简单化
缺点：可扩展性差
应用：脚本程序，linux 系统管理，linux git httpd

面向对象：核心是对象二字，对象就是特征与技能的结合体，与面向过程形成鲜明的对比
优点：可扩展性强
缺点：

类既种类，类别，对象是特征与技能的结合体那么类就是一系列对象相似的特征与技能的结合体
在现实世界中，现有对象 ，根据对象划分了类
在程序中：一定先定义类，后使用类

#第一阶段：现实中的对象---》》》现实中的类
obj1:
    特征
        学校=oldboy
        名字=zhaosi
        年龄=18
        性别=怒

    技能
        吃饭
        睡觉


obj2
    特征
        学校=oldboy
        名字=zhaosi
        年龄=18
        性别=怒

    技能
        吃饭
        睡觉


现实中的特能与技能

第二阶段：程序中的类----》》程序中的类


# '''
# class oldboy_student:
#     school='oldboy' ##类的数据属性
#     def learn(self):
#         print('is learning')##类的函数属性
#     def eat(self):
#         print('is eating')
# #    print('=====>')

##类体的代码在类定义阶段会执行
# print(oldboy_student.__dict__)
# print(oldboy_student.__dict__['school'])
# print(oldboy_student.__dict__['learn'])
# res=oldboy_student.__dict__['learn']
# res('learn')
# print(oldboy_student.school)
# oldboy_student.learn(111)
#
# oldboy_student.x=111111
# oldboy_student.school='33'
# del oldboy_student.school
# print(oldboy_student.__dict__)
# print(oldboy_student.__dict__)


###产生程序对象 类名加（）调用类，产生一个实际存在的对象，称为实例化，产生结果又称为实例

#
# class oldboy_student:
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     school='oldboy' ##类的数据属性
#     def learn(self):
#         print('is learning')##类的函数属性
#     def eat(self):
#         print('is eating')
# #    print('=====>')
# print(callable(oldboy_student))
# obj1=oldboy_student('zz','18','女')
# # obj2=oldboy_student()
# # obj3=oldboy_student()
#
# print(obj1)
# # print(obj2)
# # print(obj3)


###
class oldboy_student:

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex
        self.cc+=1


    school='oldboy' ##类的数据属性
    def learn(self):
        print('%s is learning' %self.name)##类的函数属性
    def eat(self):
        print('is eating')
#    print('=====>')
print(callable(oldboy_student))
obj1=oldboy_student('zz','18','女')
obj2=oldboy_student('zz','18','女')
obj3=oldboy_student('zz','18','女')

print(obj1.learn())
print(oldboy_student.__dict__)
# print(obj2)
# print(obj3)
