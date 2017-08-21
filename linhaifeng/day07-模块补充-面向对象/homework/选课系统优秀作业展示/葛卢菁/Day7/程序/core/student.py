#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author: gelujing
import os
from conf import settings
from db.db_handler import Db_handler
class Manage_student:
    '''管理学生视图类'''

    def __init__(self):
        if os.path.exists(settings.db_file):   #查找数据文件存在
            self.db_data = Db_handler(settings.db_file).read_db()   #读取数据库
            self.run_manage()  #执行run_manage方法
        else:
            print("\033[31;1m无数据，请先联系管理员\033[0m")
            exit()

    def run_manage(self):
        while True:
            for key in self.db_data:
                print(key)
            print("退出q")
            choice_school = input("选择学校>>>").strip()
            if choice_school in self.db_data:
                self.choice_school = choice_school
                self.school_obj = self.db_data[choice_school]
                student_name = input("请输入学生姓名>>>").strip()
                if student_name not in self.school_obj.school_student:
                    student_age = input("请输入学生年龄>>>").strip()
                    self.school_obj.show_class_course()
                    class_choice = input("请输入要加入的班级>>>").strip()
                    if class_choice in self.school_obj.school_class:
                        money = input("请输入要交的学费>>>").strip()
                        course_obj = self.school_obj.school_class[class_choice].course_obj
                        if int(money) >= int(course_obj.course_price):
                            self.school_obj.create_student(student_name,student_age,class_choice)
                            Db_handler(settings.db_file).write_db(self.db_data)  #写入数据库
                            print("\033[32;1m学生 %s 注册成功\033[0m" % student_name)
                        else:
                            print("\033[31;1m交的学费不够\033[0m")
                    else:
                        print("\033[31;1m请输入正确班级名\033[0m")
                else:
                    self.school_obj.show_student(student_name)
            elif choice_school == "q":
                exit()
            else:
                print("\033[31;1m请输入正确学校名\033[0m")