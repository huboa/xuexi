class People:
    def __init__(self,name,age,sex):
        self.name=name
        self.age=age
        self.sex=sex

    def __str__(self): #在对象被打印时触发执行
        return '<name:%s age:%s sex:%s>' %(self.name,self.age,self.sex)

p1=People('egon',18,'male')
p2=People('alex',38,'male')


print(p1)
print(p2)





# l=list([1,2,3])
# print(l)