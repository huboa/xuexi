#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author: gelujing


from core.school import Manage_school
from core.student import Manage_student
from core.teacher import Manage_teacher
from core.classes import School
from db.db_handler import  Db_handler
from conf import  settings
import os


class Manage_center:
    '''管理中心视图类'''

    def run(self):
        while True:
            print("welcome")
            print("\t1.学生视图\n"
                  "\t2.老师视图\n"
                  "\t3.管理视图\n"
                  "\t4.创建学校\n"
                  "\tq.退出")
            user_choice = input("请输入要选择的视图>>>")
            if user_choice == "1":
                Manage_student()
            elif user_choice == "2":
                Manage_teacher()
            elif user_choice == "3":
                Manage_school()
            elif user_choice == "4":
                if not os.path.exists(settings.db_file):
                   db_dict={}
                else:
                    db_dict = Db_handler(settings.db_file).read_db()
                a=input('创建的学校')
                if a not in db_dict:
                    db_dict[a] = School(a)
                    db_dict[a] = School(a)
                    Db_handler(settings.db_file).write_db(db_dict)  # 写数据库
                else:
                    print('创建的学校已存在')

            elif user_choice == "q":
                break
            else:
                print("\033[31;1m请输入正确的视图编号\033[0m")