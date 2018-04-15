from types import MethodType,FunctionType


class F3(object):
    def __init__(self):
        pass

    def ff3(self):
        print('ff3')

#
# v1 = isinstance(F3.ff3,MethodType)
# v2 = isinstance(F3.ff3,FunctionType)
# print(v1,v2) # False,True

obj = F3()
v1 = isinstance(obj.ff3,MethodType)
v2 = isinstance(obj.ff3,FunctionType)
print(v1,v2) # True False