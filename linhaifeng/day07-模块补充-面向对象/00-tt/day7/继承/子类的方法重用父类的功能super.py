# class OldboyPeople:
#     school = 'oldboy'
#     def __init__(self,name,age,sex):
#         self.name=name
#         self.age=age
#         self.sex=sex
#
#     def eat(self):
#         print('is eating')
#     def teach(self):
#         print('这是父类的teach')
#
# class OldboyTeacher(OldboyPeople):
#     def __init__(self,name,age,sex,salary,title):
#         # OldboyPeople.__init__(self,name,age,sex)
#         #在Python2中需要写全：super(OldboyTeacher,self)
#         super().__init__(name,age,sex)
#         self.salary=salary
#         self.title=title
#
#     def teach(self):
#         # OldboyPeople.teach(self)
#         super().teach()
#         print('%s is teaching'  %self.name)
# print(OldboyTeacher.mro())
#
# egon_obj=OldboyTeacher('egon',18,'male',3.1,'沙河霸道金牌讲师')
# # print(egon_obj.title)
# # print(egon_obj.__dict__)
# egon_obj.teach()







class A:
    def test(self):
        super().test()

class B:
    def test(self):
        print('B')

class C(A,B):
    pass

# a=A()
# a.test()

print(C.mro())
c=C()
c.test()