class Animal:
    x=1
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def eat(self):
        print('%s eat' %self.name)

    def talk(self):
        print('%s say' %self.name)

class People(Animal):
    x=10
    def __init__(self,name,age,sex,education):
        Animal.__init__(self,name,age,sex)
        self.education=education
    def talk(self):
        Animal.talk(self)
        print('这个是人在说话')

peo1=People('zz',18,'male','肖肖')
print(peo1.__dict__)
peo1.talk()
print(peo1.x)