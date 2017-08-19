##类里面 把功能变成属性
class People:
    def __init__(self,name,weight,height):
        self.name=name
        self.weight=weight
        self.height = height
    @property
    def bmi(self):
        return self.weight /(self.height**2)
p=People('zsc',75,1.80)
p.height=1.8
print(p.bmi)
# print(p.bmi())