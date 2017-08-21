#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author: gelujing

class Student:
    '''学生类'''

    def __init__(self,student_name,student_age):
        self.student_name = student_name
        self.student_age = student_age
        self.student_score = None

class Teacher:
    '''老师类'''

    def __init__(self,teacher_name,teacher_salary):
        self.teacher_name = teacher_name
        self.teacher_salary = teacher_salary
        self.teacher_class = {}

    def teacher_add_class(self,class_name,class_obj):
        self.teacher_class[class_name] = class_obj

class Course:
    '''课程类'''

    def __init__(self,course_name,course_price,course_time):
        self.course_name = course_name
        self.course_price = course_price
        self.course_time = course_time



class Class:
    '''班级类'''

    def __init__(self,class_name,course_obj):
        self.class_name = class_name
        self.course_obj = course_obj
        self.class_student = {}


class School:
    '''学校类'''

    def __init__(self,school_addr):
        self.school_addr = school_addr
        self.school_course = {}
        self.school_class = {}
        self.school_teacher = {}
        self.school_student={}

    def create_course(self,course_name,course_price,course_time):   #创建/更新课程方法
        course_obj = Course(course_name,course_price,course_time)   #实例化课程
        self.school_course[course_name] = course_obj   #将课程名为key，课程实例为value，添加到学校课程字典中

    def show_course(self): #查看课程方法
        for key in self.school_course:
            course_obj = self.school_course[key]
            print("\33[32;1m课程：%s\t价格：%s\t周期：%s周\33[0m" % (course_obj.course_name,
                                                                   course_obj.course_price,
                                                                   course_obj.course_time))

    def create_class(self,class_name,course_obj): #创建班级方法
        class_obj = Class(class_name,course_obj) #实例化班级
        self.school_class[class_name] = class_obj #将班级名为key，班级实例为value，添加到学校班级字典中

    def show_class(self):  #查看班级方法
        for key in self.school_class:
            class_obj = self.school_class[key]
            print("\33[32;1m班级：%s\t课程：%s\33[0m" % (class_obj.class_name,
                                                        class_obj.course_obj.course_name))

    def create_teacher(self,teacher_name,teacher_salary,class_name,class_obj):  #创建老师方法
        teacher_obj = Teacher(teacher_name,teacher_salary)  #实例化老师
        teacher_obj.teacher_add_class(class_name,class_obj)  #执行老师类下的添加班级方法
        self.school_teacher[teacher_name] = teacher_obj  #将老师名为key，老师实例为value，添加到学校老师字典中

    def update_teacher(self,teacher_name,class_name,class_obj):  #更新老师方法
        teacher_obj = self.school_teacher[teacher_name]  #取到对应老师的实例
        teacher_obj.teacher_add_class(class_name,class_obj) #执行老师类下的添加班级方法

    def show_teacher(self):
        for key in self.school_teacher:
            teacher_obj = self.school_teacher[key]
            class_list = []
            for i in teacher_obj.teacher_class:
                class_list.append(i)
            print("\33[32;1m老师：%s\t工资：%s\t班级：%s\33[0m" % (teacher_obj.teacher_name,
                                                                  teacher_obj.teacher_salary,
                                                                  class_list))

    def show_class_course(self):
        for key in self.school_class:
            class_obj = self.school_class[key]
            course_obj = class_obj.course_obj
            print("\33[32;1m班级：%s\t课程：%s\t价格：%s\t周期：%s周\33[0m" % (class_obj.class_name,
                                                                             course_obj.course_name,
                                                                             course_obj.course_price,
                                                                             course_obj.course_time))

    def create_student(self,student_name,student_age,class_choice):
        student_obj = Student(student_name,student_age)
        self.school_student[student_name]=student_obj
        class_obj = self.school_class[class_choice]
        class_obj.class_student[student_name] = student_obj
        self.school_class[class_choice] = class_obj
        #更新学校班级字典
    def show_student(self,student_name):
        student_obj=self.school_student[student_name]
        print("\33[32;1m姓名：%s\t年龄：%s\t分数：%s\33[0m" % (student_obj.student_name,
                                                   student_obj.student_age,student_obj.student_score))

    def show_teacher_classinfo(self,teacher_name):
        teacher_obj = self.school_teacher[teacher_name]
        for i in teacher_obj.teacher_class:
            class_obj = self.school_class[i]
            student_list = []
            for k in class_obj.class_student:
                student_list.append(k)
            print("\33[32;1m班级：%s\t课程：%s\t学员:%s\33[0m" % (class_obj.class_name,
                                                                 class_obj.course_obj.course_name,
                                                                 student_list))

    def update_student_score(self,class_name,student_name,student_score):
        class_obj = self.school_class[class_name]
        student_obj = class_obj.class_student[student_name]
        student_obj.student_score = student_score
        print("\033[32;1m班级：%s\t学生：%s\t分数：%s\033[0m" % (class_name,
                                                              student_name,
                                                              student_score))

    def show_student_score(self,class_name,student_name):
        class_obj = self.school_class[class_name]
        student_obj = class_obj.class_student[student_name]
        print("\033[32;1m班级：%s\t学生：%s\t分数：%s\033[0m" % (class_name,
                                                        student_name,
                                                        student_obj.student_score))
