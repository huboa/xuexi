#
#
# class Foo(object):
#     def func1(self):
#         self.func2()
#
#     def func2(self):
#         print('Foo.func2')
#
# class Bar(Foo):
#     def func2(self):
#         print('Bar.func2')
#
#
# # 示例1
# # obj = Foo()
# # obj.func1()
#
# # 示例2， 对象.xxxx,想去自己对应类中查找
# bar_obj = Bar()
# foo_obj=Foo()
#
#
# bar_obj.func1()
# bar_obj.func2()
#
# foo_obj.func1()
# foo_obj.func2()




class Foo(object):

    def __init__(self,model_class):
        self.model_class = model_class

    def changelist_view(self):
        print(self.model_class)


class Bar(Foo):
    def changelist_view(self):
        print(666)


registry = {
    "alex":Foo('alex'), # 该对象（model_class=alex），从Foo开始找  Foo('alex').xxx
    "eric":Bar('eric'), # 该对象(model_class=eric)，从Bar开始找  Bar('eric').xxx
}
for k,v in registry.items():
    # v ，Foo对象
    # v.func1()   Foo对象中找
    # v，Bar对象(model_class=eric)
    # v.func1()
    print(k,v.changelist_view())




"""
alex
eric
"""



























