class OldboyPeople:
    school = 'oldboy'
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def eat(self):
        print('is eating')

class OldboyStudent(OldboyPeople):

    def __init__(self,name,age,sex):
        OldboyPeople.__init__(self,name,age,sex)
        self.course=[]

    def learn(self):
        print('%s is learning'  %self.name)


class OldboyTeacher(OldboyPeople):
    def __init__(self,name,age,sex,salary,title):
        OldboyPeople.__init__(self,name,age,sex)
        self.salary=salary
        self.title=title
        self.course=[]

    def teach(self):
        print('%s is teaching'  %self.name)


class Course:
    def __init__(self,course_name,course_period,course_price):
        self.course_name=course_name
        self.course_period=course_period
        self.course_price=course_price
    def tell_info(self):
        print('<课程名:%s 周期：%s 价格：%s>' %(self.course_name,self.course_period,self.course_price))

python=Course('Python','6mons',3000)
linux=Course('Lnux','3mons',2000)
bigdata=Course('BigData','1mons',1000)

# python.tell_info()


egon_obj=OldboyTeacher('egon',18,'male',3.1,'沙河霸道金牌讲师')
#
# egon_obj.course.append(python)
# egon_obj.course.append(linux)
#
# for obj in egon_obj.course:
#     obj.tell_info()


yl_obj=OldboyStudent('yanglei',28,'female')
yl_obj.course.append(python)

for i in yl_obj.course:
    # print(i.course_name,i.course_period,i.course_price)
    i.tell_info()