# class cals(object):
#     def __init__(self,name,food):
#         self.NAME = name
#         self.FOOD = food
#     def sayhi(self):
#         print("hello，i am ok ",self.NAME)
#     def eat(self):
#         print("dads %s" %(self.FOOD))
#     def look(self,age):
#         print("age=%s last"%age)
#
# d1=cals("d1name","apple") ##实例化d1
# d2=cals("d2name","banana")##实例化d2
#
#
#
# d1.sayhi()
# d2.sayhi()
#
# d1.eat()
# d2.eat()
#
# d1.look(18)  ##传形参
# d2.look(18)  ##传形参
# cals("name=d3","er").sayhi()




class Role(object):

    nation="CN"  ##定义公有属性
    def __init__(self, name, role, weapon, life_value=100, money=15000):
        self.name = name
        self.role = role
        self.weapon = weapon
        self.life_value = life_value
        self.money = money
        self.__heart ="Normore"

    def shot(self):
        print("%s is shooting..."%self.name)
    def get_heart(self):    ###调用私有方法的用法
        return self.__heart

    def got_shot(self):
        print("ah...,I got shot...%s"%self.name)

    def buy_gun(self,gun_name):
        print(" just bought %s" % gun_name)
        self.weapon = gun_name
    def __del__(self):       ##析构函数
        print("del....run....")

r1 = Role('zsc','police','AK47') #生成一个角色
r2 = Role('Jack','terrorist','B22')  #生成一个角色

# r1.shot()
# r2.buy_gun("AK47")
print(r1.name)  ##正常访问
print(r1.get_heart())  ##提供对外的访问
print(r1._Role__heart) ##强制访问私有属性
print(Role('asdf','asf','sdf').shot())##test
print(r1.got_shot())
print(r2.buy_gun("qwe"))

r1.nation="us"
print(r1.nation)   ##访问公有属性
print(r2.nation)
Role.nation="us"    ##更改公有属性
print(r1.nation)   ##访问公有属性
print(r2.nation)