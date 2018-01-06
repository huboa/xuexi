'''
面向过程：核心是过程二字，过程指的是问题的解决步骤，即先干什么再干什么，基于
面向过程去设计程序就好比在设计一条流水线，是一种机械式的思维方式
优点：复杂的问题流程化，进而简单化
缺点：可扩展性差
应用：脚本程序，比如linux系统管理脚本，著名案例：linux内核，httpd，git

面向对象：核心是对象二字，对象就是特征与技能的结合体，如果把设计程序比喻成
创造一个世界，那你就是这个世界的上帝，与面向过程对机械流水的模拟形式鲜明的对比
面向对象更加注重的对现实时间的模拟。

优点：可扩展性
缺点：


类即种类，类别，对象是特征和与技能的结合体，那么类就是一系列对象相似的
特征与技能的结合体
在现实世界中：先有一个个具体存在的对象----》（总结相似之处）---》现实中的类
在程序中：一定是先定义类，后调用类来产生对象

#第一阶段：现实中的对象----》现实中类
obj1：
    特征
        学校=oldboy
        名字=李大炮
        年龄=18
        性别=女
    技能
        学习
        吃饭

obj2：
    特征
        学校=oldboy
        名字=张全蛋
        年龄=28
        性别=男
    技能
        学习
        吃饭

obj3：
    特征
        学校=oldboy
        名字=牛榴弹
        年龄=18
        性别=女
    技能
        学习
        吃饭

现实中的老男孩学生类：
    相似的特征
        学校=oldboy
    相似的技能
        学习
        吃饭

#第二阶段：程序中的类----》程序中的对象
'''
# class OldboyStudent:
#     school = 'oldboy' #类的数据属性
#     def learn(self): #类的函数属性
#         print('is learning')
#
#     def eat(self):
#         print('is eating')
    # print('======>')

#类体的代码在类定义阶段就会执行,理所应当会产生类的名称空间，用__dict__属性查看
# print(OldboyStudent.__dict__)
# print(OldboyStudent.__dict__['school'])
# print(OldboyStudent.__dict__['learn'])


#类的属性操作
# print(OldboyStudent.school)
# print(OldboyStudent.learn)

#
# def func():pass
# print(func)
# OldboyStudent.learn(123)

# OldboyStudent.x=1111111111111111111111
# OldboyStudent.school='Oldboy'
# del  OldboyStudent.school
# print(OldboyStudent.__dict__)

# OldboyStudent.__dict__['x']=1111111111111111111111



#产生程序中的对象：类名加括号，调用类，产生一个该类的实际存在的对象，该调用过程称为实例化，产生的结果又可以成为实例
# class OldboyStudent:
#     school = 'oldboy'
#     #obj1,'李大炮',18,'女'
#     def __init__(self,name,age,sex): #在实例化时,产生对象之后执行
#         # if not isinstance(name,str):
#         #     raise TypeError('名字必须是字符串类型')
#         self.name=name
#         self.age=age
#         self.sex=sex
#         # return None #__init__方法必须返回None
#         #obj1.name='李大炮'
#         #obj1.age=18
#         #obj1.sex='女'
#
#     def learn(self):
#         print('is learning')
#
#     def eat(self):
#         print('is eating')

# obj1=OldboyStudent('李大炮',18,'女') #
# 分两步：
# 第一步：先产生一个空对象obj1
# 第二步：OldboyStudent.__init__(obj1,'李大炮',18,'女')
# print(obj1.__dict__)
#
# obj2=OldboyStudent('张全蛋',28,'男')
# obj3=OldboyStudent('牛榴弹',18,'女')
#
# print(obj2.__dict__)
# print(obj3.__dict__)
#
#
#
# print(obj1.name)#obj1.__dict__['name']
#
# obj1.name='大炮'
# print(obj1.__dict__)
# obj1.__dict__['name']='炮'
# print(obj1.name)
#
# obj1.__dict__.pop('name')
# # print(obj1.name)
# print(obj1.__dict__)




# obj1=OldboyStudent(123123123,18,'女') #




school='hahahahahahaah'
class OldboyStudent:
    # school = 'oldboy'

    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def learn(self):
        print('%s is learning'  %self.name)

    def eat(self):
        print('is eating')

obj1=OldboyStudent('李大炮',18,'女')
obj2=OldboyStudent('张全蛋',28,'男')
obj3=OldboyStudent('牛榴弹',18,'女')
# print(obj1.__dict__)

# print(obj1.name,obj1.age,obj1.sex)
#对象可以访问类的数据属性，结论：类的数据属性共享给所有对象使用，id对一样
# print(obj1.school,id(obj1.school))
# print(obj2.school,id(obj2.school))
# print(obj3.school,id(obj3.school))
# print(OldboyStudent.school,id(OldboyStudent.school))

#类的函数属性是绑定给所有对象使用的，绑定给不同的对象是不同的绑定方法，绑定方法有何特殊之处？
#暂且抛开绑定方法，类肯定可以访问自己的函数属性
# OldboyStudent.learn(obj1)
# OldboyStudent.learn(obj2)
# OldboyStudent.learn(obj3)


# print(obj1.learn)
# print(obj2.learn)
# print(obj3.learn)
# print(OldboyStudent.learn)


#绑定方法：绑定给谁，就由谁来调用，谁来调用就把“谁”本身当做第一个参数传入
# obj1.learn() #OldboyStudent.learn(obj1)
# obj2.learn() #OldboyStudent.learn(obj1)
# obj3.learn() #OldboyStudent.learn(obj1)





#在python3中类型就类
# print(OldboyStudent)
# print(list)

# l1=list()
# l2=list()
# l3=list()
# # print(type(l1))
# # print(type(obj1))
#
# # l1.append(3) #list.append(l1,3)
# list.append(l1,3)
# print(l1)
# print(l2)
# print(l3)



#属性查找顺序：先从对象的__dict__中找，然后到类的__dict__中找，然后父类....
# OldboyStudent.school='哈佛'
# obj1.school='hahahahahahahhahahahahahah'
# print(obj1.__dict__)
# print(obj1.school)
#
# print(obj2.school)
# print(obj3.school)


class Foo:
    count=0
    def __init__(self,x,y,z):
        self.x=x
        self.y=y
        self.z=z
        Foo.count+=1


obj1=Foo(1,1,1)
obj2=Foo(1,2,1)
obj3=Foo(1,2,3)


# print(obj1.count)
# print(Foo.count)






class OldboyStudent:
    # school = 'oldboy'

    def __init__(self,name,age,sex='male'):
        self.name=name
        self.age=age
        self.sex=sex

    def learn(self):
        print('%s is learning'  %self.name)

    def eat(self,y):
        print('is eating')

obj1=OldboyStudent('李大炮',18)

# OldboyStudent.eat()
# obj1.eat(1)
obj1.learn()
