import abc

#多态：同一种事物的多种形态
class Animal: #同一类事物:动物
    def talk(self):
        pass

class People(Animal): #动物的形态之一:人
    def talk(self):
        print('say hello')

class Dog(Animal): #动物的形态之二:狗
    def talk(self):
        print('say wangwang')

class Pig(Animal): #动物的形态之三:猪
    def talk(self):
        print('say aoao')

class Cat(Animal):
    def talk(self):
        print('say miaomiao')


class Bird:
    def talk(self):
        print('jijiji')

#多态性：可以在不考虑实例类型的前提下使用实例
p1=People()
d=Dog()
p2=Pig()
c=Cat()
b=Bird()

# p1.talk()
# d.talk()
# p2.talk()
# c.talk()
# b.talk()

def Talk(animal):
    animal.talk() #p1.talk()

Talk(p1)
Talk(d)
Talk(p2)
Talk(c)
Talk(b)

#多态性的好处



#list,str,tuple
l=list([1,2,3])
t=tuple((1,2))
s=str('hello')


l.__len__()
t.__len__()
s.__len__()



def my_len(obj):
    return obj.__len__()


print(my_len(l))
print(my_len(t))
print(my_len(s))

#len






