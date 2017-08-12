###继承的基本形式
class ParentClass1:##定义父类
    pass
class ParentClass2:##定义父类
    pass
class SubClass1(ParentClass1):
    pass
class SubClass2(ParentClass1,ParentClass2):
    pass
print(SubClass2.__base__)