#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author: gelujing
import os
import sys
from conf import settings
from db.db_handler import Db_handler

class Manage_school:
    '''管理学校视图类'''

    def __init__(self):
        if os.path.exists(settings.db_file): #查找数据库文件如果存在
            self.db_data = Db_handler(settings.db_file).read_db() #读取数据库
            self.run_manage() #执行run_manage方法
        else:
            print("\033[31;1m无数据，请先创建学校\033[0m")
            exit()


    def run_manage(self):
        while True:
            for key in self.db_data:
                print(key)
            choice_school = input("选择学校>>>").strip()
            if choice_school in self.db_data:
                self.choice_school = choice_school #如果输入的学校在数据库中存在，定义选择的学校
                self.school_obj = self.db_data[choice_school] #定义学校的实例
                while True:
                    print("==欢迎来到%s校区==\n"
                          "添加课程 add_course\n"
                          "添加班级 add_class\n"
                          "添加老师 add_teacher\n"
                          "查看课程 check_course\n"
                          "查看班级 check_class\n"
                          "查看老师 check_teacher\n"
                          "退出 exit" % choice_school)
                    user_func = input("输入要操作的命令>>>").strip()
                    if hasattr(self,user_func):
                        getattr(self,user_func)()
                    else:
                        print("\033[31;1m请输入正确的操作命令\033[0m")
            else:
                print("\033[31;1m请输入正确学校名\033[0m")


    def add_course(self):
        course_name = input("请输入要添加课程的名称>>>").strip()
        course_price = input("请输入要添加课程的价格>>>").strip()
        course_time = input("请输入要添加课程的周期>>>").strip()
        if course_name in self.school_obj.school_course :
            self.school_obj.create_course(course_name,course_price,course_time) #执行school类中的创建课程方法，更新课程
            print("\033[32;1m更新课程 %s 完成\033[0m" % course_name)
        elif course_name=='' or course_price=='' or course_time=='' :
            pass
        else:
            self.school_obj.create_course(course_name,course_price,course_time) #执行school类中的创建课程方法，创建课程
            print("\033[32;1m创建课程 %s 完成\033[0m" % course_name)
        Db_handler(settings.db_file).write_db(self.db_data)

    def add_class(self):
        class_name = input("请输入要添加班级的名称>>>").strip()
        course_name = input("请输入要关联的课程>>>").strip()
        if class_name not in self.school_obj.school_class:
            if course_name in self.school_obj.school_course:
                course_obj = self.school_obj.school_course[course_name]
                self.school_obj.create_class(class_name,course_obj) #执行school类中的创建班级方法，创建班级
                Db_handler(settings.db_file).write_db(self.db_data)  #写入数据库
                print("\033[32;1m创建班级 %s 成功，关联课程为 %s\033[0m" % (class_name,course_name))
            else:
                print("\033[31;1m关联课程不存在\033[0m")
        else:
            print("\033[31;1m班级已存在\033[0m")

    def add_teacher(self):
        teacher_name = input("请输入要添加老师的名字>>>").strip()
        teacher_salary = input("请输入要添加老师的工资>>>").strip()
        teacher_class = input("请输入要关联的班级>>>").strip()
        if teacher_class in self.school_obj.school_class:
            class_obj = self.school_obj.school_class[teacher_class]
            if teacher_name not in self.school_obj.school_teacher:
                self.school_obj.create_teacher(teacher_name,teacher_salary,teacher_class,class_obj) #执行学校类中的创建老师方法
                print("\033[32;1m创建老师 %s 成功，关联班级为 %s\033[0m" % (teacher_name,teacher_class))
            else:
                self.school_obj.update_teacher(teacher_name,teacher_class,class_obj)
                print("\033[32;1m更新老师 %s 成功\033[0m" % teacher_name)
            Db_handler(settings.db_file).write_db(self.db_data)
        else:
            print("\033[31;1m关联班级不存在\033[0m")

    def check_course(self):
        self.school_obj.show_course()   #执行学校类下的显示课程方法

    def check_class(self):
        self.school_obj.show_class()   #执行学校类下的显示班级方法

    def check_teacher(self):
        self.school_obj.show_teacher()  #执行学校类下的显示老师方法

    def exit(self):
        sys.exit("退出系统")

