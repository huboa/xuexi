class SchoolMember(object): ###学校类
    members = 0  # 初始学校人数为0

    def __init__(self, name, age,sex):
        self.name = name
        self.age = age
        self.sex =sex
        self.enroll()


    def enroll(self):
        '''注册'''
        SchoolMember.members += 1
        print("\033[32;1mnew member [%s] is enrolled,now there are [%s] members.\033[0m " % (
        self.name, SchoolMember.members))

    def __del__(self):
        '''析构方法'''
        print("\033[31;1mmember [%s] is dead!\033[0m" % self.name)


    def tell(self):
        print("----info:%s----"%self.name)
        for k,v in self.__dict__.items():
            print("\t",k,":",v)

class Teacher(SchoolMember):  ###老师的类
    def __init__(self, name, age, course, salary):
        SchoolMember.__init__(self,name,age,sex)

        self.course = course
        self.salary = salary
        self.enroll()

    def teaching(self):
        '''讲课方法'''
        print("Teacher [%s] is teaching [%s] for class [%s]" % (self.name, self.course, 's12'))

    def tell(self):
        '''自我介绍方法'''
        msg = '''Hi, my name is [%s], works for [%s] as a [%s] teacher !''' % (self.name, 'Oldboy', self.course)
        print(msg)


class Student(SchoolMember):###学生的类
    def __init__(self, name, age, sex,course,tuition):
        SchoolMember.__init__(self,name,age,sex)
        self.course = course
        self.tuition = tuition##fee
        self.amount=0
    def pay_tuition(self,amount):
        print("student[%s] has just paied [%s]"%(self.name.amount))
        self.amount+=amount



    t1 = Teacher("Alex", 22,"F*M",'Python', 20000)
    t2 = Teacher("TengLan", 29,"N/A" 'Linux', 3000)

    s1 = Student("Qinghua", 24, "M","Python S15", 1483)
    s2 = Student("SanJiang", 26, "M","Python S15", 1484)

    t1.teaching()
    t2.teaching()
    t1.tell()
    print(SchoolMember.members)