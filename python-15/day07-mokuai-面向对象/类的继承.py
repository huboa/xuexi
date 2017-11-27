##先继承后重构

class Person(object):     ##定义父类
    def __init__(self,name ,age):
        self.name=name#
        self.age=age
        self.sex="noraml"
    def talk(selfself):
        print("person is talking....")
class WhitePersion(Person):
    def walk(self):
        print("is walking ...")

    def talk(self):
        print("is talking...")
class BlackPerson(Person):
    def __init__(self,name,age,strength): ##先继承后重构
        Person.__init__(self,name,age)
        print(self.name,self.age,self.sex)
    def walk(self):
        print("is walking ...")
    def talk(self):
        print("is talking...")
    def sex(self):
        print(self.sex())
b = BlackPerson('zsc',30,'power')
b.talk()

b.sex()


