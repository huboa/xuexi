#继承的基本形式
# class ParentClass1(object): #定义父类
#     pass
#
# class ParentClass2: #定义父类
#     pass
#
# class SubClass1(ParentClass1): #单继承，基类是ParentClass1，派生类是SubClass
#     pass
#
# class SubClass2(ParentClass1,ParentClass2): #python支持多继承，用逗号分隔开多个继承的类
#     pass
#
#
#
#
# print(SubClass1.__bases__)
# print(SubClass2.__bases__)
# print(ParentClass1.__bases__)

#经典类与新式类的区别



# class Animal:
#     x=1
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         # print('Animal.__init__')
#     def eat(self):
#         print('%s eat' %self.name)
#
#     def talk(self):
#         print('%s say' %self.name)
#
# class People(Animal):
#     x=10
#     def __init__(self,name,age,sex,education):
#         Animal.__init__(self,name,age,sex)
#         self.education=education
#         # print('People.__init__')
#
#     def talk(self):
#         Animal.talk(self)
#         print('这是人在说话')
#
# class Dog(Animal):
#     pass
# class Pig(Animal):
#     pass
#
#
# peo1=People('alex',18,'male','小学肄业')
# print(peo1.__dict__)
# peo1.talk()
# print(peo1.x)

# dog1=Dog('yuanhao',28,'male')
# pig1=Pig('wupeiqi',18,'male')
#
#
# print(peo1.name)
# print(dog1.name)
# print(pig1.name)




class OldboyPeople:
    school = 'oldboy'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def eat(self):
        print('is eating')

class OldboyStudent(OldboyPeople):
    def learn(self):
        print('%s is learning'  %self.name)


class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,salary,title):
        OldboyPeople.__init__(self,name,age,sex)
        self.salary=salary
        self.title=title

    def teach(self):
        print('%s is teaching'  %self.name)


yl_obj=OldboyStudent('yanglei',28,'female')
egon_obj=OldboyTeacher('egon',18,'male',3.1,'沙河霸道金牌讲师')

#
# yl_obj.learn()
# yl_obj.eat()

print(egon_obj.__dict__)

'''
总结：
1 继承的功能之一：解决类与类之间的代码重复问题
2 继承是类与类之间的关系，是一种，什么是什么的关系
3 在子类派生出的新的属性，已自己的为准
4 在子类派生出的新的方法内重用父类的功能的方式：指名道姓法
OldboyPeople.__init__
  这种调用方式本身与继承是没有关系
'''









