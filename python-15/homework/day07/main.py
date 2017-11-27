import sys
import pickle

###创建学校类
class School(object):

    def __init__(self,name,addr):
        self.name=name
        self.addr=addr

##定义老师类
class Techer(object):
    def __init__(self,name ,age):
        self.name=name
        self.age=age

####创建班级类
class Class(object):
    def __init__(self,name):
        self.name=name
        self.student = {}
###创建课程
class Course(School):
     def __init__(self,name,date,price):
         self.name=name
         self.date=date
         self.price=price
##学生类
class Student(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age
