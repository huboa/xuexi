#先看如何隐藏
class Foo:
    __N=111111 #_Foo__N
    def __init__(self,name):
        self.__Name=name #self._Foo__Name=name

    def __f1(self): #_Foo__f1
        print('f1')
    def f2(self):
        self.__f1() #self._Foo__f1()

f=Foo('egon')
# print(f.__N)
# f.__f1()
# f.__Name
# f.f2()


#这种隐藏需要注意的问题：
#1：这种隐藏只是一种语法上变形操作，并不会将属性真正隐藏起来
# print(Foo.__dict__)
# print(f.__dict__)
# print(f._Foo__Name)
# print(f._Foo__N)

#2:这种语法级别的变形，是在类定义阶段发生的，并且只在类定义阶段发生
# Foo.__x=123123123123123123123123123123123123123123
# print(Foo.__dict__)
# print(Foo.__x)
# f.__x=123123123
# print(f.__dict__)
# print(f.__x)

#3:在子类定义的__x不会覆盖在父类定义的__x，因为子类中变形成了：_子类名__x,而父类中变形成了：_父类名__x，即双下滑线开头的属性在继承给子类时，子类是无法覆盖的。
class Foo:
    def __f1(self): #_Foo__f1
        print('Foo.f1')

    def f2(self):
        self.__f1() #self._Foo_f1

class Bar(Foo):
    def __f1(self): #_Bar__f1
        print('Bar.f1')

# b=Bar()
# b.f2()



#封装不是单纯意义的隐藏
#1：封装数据属性：将属性隐藏起来，然后对外提供访问属性的接口，关键是我们在接口内定制一些控制逻辑从而严格控制使用对数据属性的使用
class People:
    def __init__(self,name,age):
        if not isinstance(name,str):
            raise TypeError('%s must be str' %name)
        if not isinstance(age,int):
            raise TypeError('%s must be int' %age)
        self.__Name=name
        self.__Age=age
    def tell_info(self):
        print('<名字：%s 年龄：%s>' %(self.__Name,self.__Age))

    def set_info(self,x,y):
        if not isinstance(x,str):
            raise TypeError('%s must be str' %x)
        if not isinstance(y,int):
            raise TypeError('%s must be int' %y)
        self.__Name=x
        self.__Age=y

# p=People('egon',18)
# p.tell_info()
#
# # p.set_info('Egon','19')
# p.set_info('Egon',19)
# p.tell_info()



#2：封装函数属性：为了隔离复杂度

#取款是功能,而这个功能有很多功能组成:插卡、密码认证、输入金额、打印账单、取钱
#对使用者来说,只需要知道取款这个功能即可,其余功能我们都可以隐藏起来,很明显这么做
#隔离了复杂度,同时也提升了安全性

class ATM:
    def __card(self):
        print('插卡')
    def __auth(self):
        print('用户认证')
    def __input(self):
        print('输入取款金额')
    def __print_bill(self):
        print('打印账单')
    def __take_money(self):
        print('取款')

    def withdraw(self):
        self.__card()
        self.__auth()
        self.__input()
        self.__print_bill()
        self.__take_money()

a=ATM()
a.withdraw()


# _x=123