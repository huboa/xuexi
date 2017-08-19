# #这种隐藏需要的问题：
# class Foo:
#     __N=11111 #_Foo__N
#     def __init__(self,name):
#         self.__Name=name#self._Foo__Name=name
#     def __f1(self):#_Foo__f1
#         print('f1')
#     def f2(self):
#         self.__f1()##self.Foo__f1
#
# f=Foo('zsc')
# print(f.__N)
# f.__f1()
# f.__Name
# f.f2()


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
