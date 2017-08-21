#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author: gelujing
import os
import sys
from conf import settings
from db.db_handler import Db_handler
class Manage_teacher:
    '''管理老师视图类'''

    def __init__(self):
        if os.path.exists(settings.db_file):
            self.db_data = Db_handler(settings.db_file).read_db()   #读取数据库
            self.run_manage()
        else:
            print("\033[31;1m无数据，请联系管理员\033[0m")
            exit()

    def run_manage(self):
        '''
        :return:
        '''
        while True:
            for key in self.db_data:
                print(key)
            choice_school = input("选择学校>>>").strip()
            if choice_school in self.db_data: #如果输入的学校在数据库中存在，定义选择的学校
                self.choice_school = choice_school #如果输入的学校在数据库中存在，定义选择的学校
                self.school_obj = self.db_data[choice_school] #定义学校的实例
                teacher_name = input("请输入老师姓名>>>").strip()
                while True:
                    if teacher_name in self.school_obj.school_teacher:  #老师的名字存在
                        print("查看班级 check_class\n"
                              "修改学生分数 update_score\n"
                              "查看学生分数 check_student_score\n"
                              "退出 exit")
                        user_func = input("输入要操作的命令>>>").strip()
                        if hasattr(self,user_func):  #如果有这个方法
                            getattr(self,user_func)(teacher_name) #执行这个方法
                        else:
                            print("\033[31;1m请输入正确的操作命令\033[0m")
                    else:
                        print("\033[31;1m请输入正确老师名\033[0m")
                        break
            else:
                print("\033[31;1m请输入正确学校名\033[0m")

    def check_class(self,teacher_name):
        self.school_obj.show_teacher_classinfo(teacher_name)

    def update_score(self,teacher_name):
        teacher_obj = self.school_obj.school_teacher[teacher_name]
        class_name = input("请输入班级名>>>").strip()
        student_name = input("请输入学生姓名>>>").strip()
        student_score = input("请输入学生分数>>>").strip()
        if class_name in self.school_obj.school_class:
            if class_name in teacher_obj.teacher_class:
                class_obj = teacher_obj.teacher_class[class_name]  #实例化班级
                if student_name in class_obj.class_student:  #学生在这个班级内
                    self.school_obj.update_student_score(class_name,student_name,student_score) #执行学校类的更新学生成绩方法
                    Db_handler(settings.db_file).write_db(self.db_data) #写入数据库
                else:
                    print("\033[31;1m该班级内没有学生 %s\033[0m" % student_name)
            else:
                print("\033[31;1m该老师不负责班级 %s\033[0m" % class_name)
        else:
            print("\033[31;1m该学校内没有班级 %s\033[0m" % class_name)

    def check_student_score(self,teacher_name):
        teacher_obj = self.school_obj.school_teacher[teacher_name] #实例化老师
        class_name = input("请输入班级名>>>").strip()
        student_name = input("请输入学生姓名>>>").strip()
        if class_name in self.school_obj.school_class: #学校有该班级
            if class_name in teacher_obj.teacher_class: #该老师负责这个班级
                class_obj = teacher_obj.teacher_class[class_name] #实例化班级
                if student_name in class_obj.class_student:  #学生在这个班级内
                    self.school_obj.show_student_score(class_name,student_name) #执行学校类的更新学生成绩方法
                else:
                    print("\033[31;1m该班级内没有学生 %s\033[0m" % student_name)
            else:
                print("\033[31;1m该老师不负责班级 %s\033[0m" % class_name)
        else:
            print("\033[31;1m该学校内没有班级 %s\033[0m" % class_name)

    def exit(self,teacher_name):
        sys.exit("退出系统")

