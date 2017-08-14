class school:
    pass
class student:
    def __init__(self, name, age, sex='male'):
        self.name = name
        self.age = age
        self.sex = sex

    def learn(self):
        print('%s is learning' % self.name)

    def eat(self, y):
        print('is eating')


class teacher:
    pass
class course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<课程名:%s 周期：%s 价格：%s>' %(self.name,self.period,self.price))

class classes:
    pass
class classes_record:
    pass
class study_record:
    pass





