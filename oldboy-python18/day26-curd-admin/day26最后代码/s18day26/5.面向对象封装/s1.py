
# 1. 保存一个人的姓名
# name = "alex"

# 2. 保存10个人的姓名
# name_list = ['alex','xxx','xxx']

# 3. 保存10个人的信息（姓名，年龄）
# user_list = [
#     {'name':'alex1','age':18}, # dict(name='alex1',age=18)
#     {'name':'alex2','age':18},
#     {'name':'alex3','age':18},
#     {'name':'alex4','age':18},
#     {'name':'alex5','age':18},
# ]
#
#
# class Foo(object):
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
# user_list = [
#     Foo('alex1',18),
#     Foo('alex2',18),
#     Foo('alex3',18),
# ]

# 3. 保存10个人的信息（姓名，年龄）,打印每个人：  姓名+大王;118

# user_list = [
#     {'name':'alex1','age':18}, # dict(name='alex1',age=18)
#     {'name':'alex2','age':18},
#     {'name':'alex3','age':18},
#     {'name':'alex4','age':18},
#     {'name':'alex5','age':18},
# ]
#
# for item in user_list:
#     value = "%s 大王;年龄：%s" %(item['name'],item['age']+100)
#     print(value)


class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        value = "%s 大王;年龄：%s" % (self.name, self.age + 100)
        return value


user_list = [
    Foo('alex1',18),
    Foo('alex2',18),
    Foo('alex3',18),
]
for item in user_list:
    value = item.show()
    print(value)