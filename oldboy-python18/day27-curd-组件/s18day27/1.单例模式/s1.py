
# ###################### 多例模式 ######################
# class Foo(object):
#     pass
#
# # 创建对象、创建Foo类的实例
# obj1 = Foo()
# obj2 = Foo()
#
# print(obj1,obj2)
# ###################### 单例模式 ######################
class Foo(object):
    instance = None # 创建一个对象

    @staticmethod
    def get_instance():
        if not Foo.instance:
            Foo.instance = Foo()
        return Foo.instance

obj1 = Foo.get_instance()
obj2 = Foo.get_instance()
obj3 = Foo.get_instance()
print(obj1,obj2,obj3)













