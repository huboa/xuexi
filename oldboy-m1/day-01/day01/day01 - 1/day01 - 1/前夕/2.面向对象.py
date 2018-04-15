"""
面向对象封装
"""

class Foo(object):
    def __init__(self,age,name):
        self.age = age
        self.name = name

class Bar(object):
    def __init__(self,counter):
        self.counter = counter
        self.obj = Foo('18','石鹏')

b1 = Bar(1)