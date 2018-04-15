def f1():
    print('f1')

class F2(object):
    pass

class F3(object):
    def __init__(self):
        pass

    def ff3(self):
        print('ff3')

class F4(object):
    def __init__(self):
        pass

    def __call__(self, *args, **kwargs):
        print('f4')


def func(arg):
    """
    由于arg在函数中加括号，所以他只有4中表现形式：
        - 函数
        - 类
        - 方法
        - 对象
    :param arg:
    :return:
    """
    arg()

# 1. 函数，内部执行函数
func(f1)
# 2. 类,内部执行__init__方法
func(F2)

# 3. 方法，obj.ff3
obj1 = F3()
func(obj1.ff3)

# 4. 对象
obj2 = F4()
func(obj2)