# class Foo:
#     @property
#     def f1(self):
#          print('f1')
#
#
# f=Foo()
#
# # f.f1()
#
# f.f1


'''
例：BMI指数（bmi是计算而来的，但很明显它听起来像是一个属性而非方法，如果我们将其做成一个属性，更便于理解）
成人的BMI数值：
过轻：低于18.5
正常：18.5-23.9
过重：24-27
肥胖：28-32
非常肥胖, 高于32
　　体质指数（BMI）=体重（kg）÷身高^2（m）
　　EX：70kg÷（1.75×1.75）=22.86
'''

class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height=height
    @property
    def bmi(self):
        return self.weight / (self.height**2)

# p=People('egon',75,1.80)
# p.height=1.86
# print(p.bmi())
# print(p.bmi)

#访问，设置，删除(了解)
class Foo:
    def __init__(self,x):
        self.__Name=x

    @property
    def name(self):
        return self.__Name

    @name.setter
    def name(self,val):
        if not isinstance(val,str):
            raise TypeError
        self.__Name=val

    @name.deleter
    def name(self):
        # print('=-====>')
        # del self.__Name
        raise PermissionError

f=Foo('egon')
# print(f.name)
#
# # f.name='Egon'
# f.name=123123123213
# print(f.name)

del f.name
print(f.name)