from types import FunctionType,MethodType

# 函数，函数的所有参数都必须自己传递。
# 方法，第一个self参数无需自己传递，默认会将执行方法的对象自动传递。


def func(arg):
    pass


class Foo:
    def fun(self):
        """
        如果 obj.func    => 方法
        如果 Foo.func    => 函数
        :return:
        """
        pass

# obj = Foo()
# func_list = [obj.fun, obj.fun]
# for item in func_list:
#     item()


# func_list = [Foo.fun, Foo.fun]
# for item in func_list:
#     item(123)

# 记住：Foo.xxx