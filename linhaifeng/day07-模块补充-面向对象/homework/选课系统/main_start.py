class school:
    def __init__(self, name, address,city):
        self.name = name
        self.address = address
        self.city=city
class student:
    def __init__(self, name, age, sex='male'):
        self.name = name
        self.age = age
        self.sex = sex
class teacher:
    def __init__(self, name, age, sex='male'):
        self.name = name
        self.age = age
        self.sex = sex
class course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<课程名:%s 周期：%s 价格：%s>' %(self.name,self.period,self.price))
class classes:
    def __init__(self,name,semester,course,date,teacher):
        self.name=name
        self.semester=semester
        self.course=course
        self.date=date
        self.teacher=teacher
class classes_record:
    def __init__(self,classes,times,date):
        self.classes=classes
        self.times=times
        self.date=date

class study_record:
   def __init__(self,classes_record,status,date,score):
       self.classes_record=classes_record
       self.status=status
       self.date=date
       self.score=score


python=course('python','9','20000')
python.tell_info()



