# class OldboyTeacher:
#     school='oldboy'
#     def __init__(self,name,age,sex,salary,tilte):
#         self.name=name
#         self.age=age
#         self.sex=sex
#         self.salary=salary
#         self.title=tilte
#         self.course=[]
#
#     def teach(self):
#         print('%s is teaching' %self.name)
#
#     def eat(self):
#         print('%s is eating' %self.name)
#
#
# class OldboyStudent:
#     school = 'oldboy'
#
#     def __init__(self, name, age, sex,):
#         self.name = name
#         self.age = age
#         self.sex = sex
#         self.course = []
#
#     def learn(self):
#         print('%s is learning' % self.name)
#
#     def eat(self):
#         print('%s is eating' % self.name)
#
#
# class Course:
#     def __init__(self,name,price,period):
#         self.name=name
#         self.price=price
#         self.period=period
#     def tell_info(self):
#         print(obj.name, obj.price, obj.period)
#
#
# python=Course('Python','6mons',3000)
# linux=Course('Lnux','3mons',2000)
# bigdata=Course('BigData','1mons',1000)
#
# egon_obj=OldboyTeacher('egon',18,'male',3.1,'沙河霸道金牌讲师')
# egon_obj.course.append(python)
# egon_obj.course.append(linux)
# #
# # for obj in egon_obj.course:
# #     obj.tell_info()
#
#
#
# yl_obj=OldboyStudent('yanglei',28,'female')
# yl_obj.course.append(python)
# yl_obj.course.append(bigdata)
#
# for obj in yl_obj.course:
#     obj.tell_info()



#优化：减少重复代码
# class OldboyPoeple:
#     school = 'oldboy'
#     def __init__(self, name, age, sex):
#         self.name = name
#         self.age = age
#         self.sex = sex
#     def eat(self):
#         print('%s is eating' % self.name)
#
#
# class OldboyTeacher(OldboyPoeple):
#     def __init__(self,name,age,sex,salary,tilte):
#         OldboyPoeple.__init__(self,name,age,sex)
#         self.salary=salary
#         self.title=tilte
#         self.course=[]
#
#     def teach(self):
#         print('%s is teaching' %self.name)
#
#
#
# class OldboyStudent(OldboyPoeple):
#     def __init__(self, name, age, sex,):
#         OldboyPoeple.__init__(self, name, age, sex)
#         self.course = []
#
#     def learn(self):
#         print('%s is learning' % self.name)
#
#
# class Course:
#     def __init__(self,name,price,period):
#         self.name=name
#         self.price=price
#         self.period=period
#     def tell_info(self):
#         print(obj.name, obj.price, obj.period)
#
#
# python=Course('Python','6mons',3000)
# linux=Course('Lnux','3mons',2000)
# bigdata=Course('BigData','1mons',1000)
#
# egon_obj=OldboyTeacher('egon',18,'male',3.1,'沙河霸道金牌讲师')
# egon_obj.course.append(python)
# egon_obj.course.append(linux)
# #
# # for obj in egon_obj.course:
# #     obj.tell_info()
#
#
#
# yl_obj=OldboyStudent('yanglei',28,'female')
# yl_obj.course.append(python)
# yl_obj.course.append(bigdata)
#
# for obj in yl_obj.course:
#     obj.tell_info()



#再找找组合
x=1
class OldboyPoeple:
    school = 'oldboy'

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def eat(self):
        print('%s is eating' % self.name)


class OldboyTeacher(OldboyPoeple):
    def __init__(self, name, age, sex, salary, tilte):
        OldboyPoeple.__init__(self, name, age, sex)
        self.salary = salary
        self.title = tilte
        self.course = []
        self.students=[]
    def teach(self):
        print('%s is teaching' % self.name)


class OldboyStudent(OldboyPoeple):
    def __init__(self, name, age, sex, ):
        OldboyPoeple.__init__(self, name, age, sex)
        self.course = []

    def learn(self):
        print('%s is learning' % self.name)

    def tell_info(self):
        print('<name:%s age:%s sex:%s>' %(self.name,self.age,self.sex))

class Course:
    def __init__(self, name, price, period):
        self.name = name
        self.price = price
        self.period = period

    def tell_info(self):
        print(self.name, self.price, self.period)


python = Course('Python', '6mons', 3000)
linux = Course('Lnux', '3mons', 2000)
bigdata = Course('BigData', '1mons', 1000)


s1 = OldboyStudent('yanglei', 18, 'female')
s2 = OldboyStudent('lilei', 18, 'male')
s3 = OldboyStudent('liulei', 16, 'female')
s4 = OldboyStudent('zhanglei', 17, 'female')


egon_obj = OldboyTeacher('egon', 18, 'male', 3.1, '沙河霸道金牌讲师')
egon_obj.course.append(python)
egon_obj.course.append(linux)



egon_obj.students.append(s1)
egon_obj.students.append(s2)
egon_obj.students.append(s3)
egon_obj.students.append(s4)

for obj in egon_obj.students:
    obj.tell_info()




# for obj in egon_obj.course:
#     obj.tell_info()


#
# yl_obj = OldboyStudent('yanglei', 28, 'female')
# yl_obj.course.append(python)
# yl_obj.course.append(bigdata)
#
# for obj in yl_obj.course:
#     obj.tell_info()
