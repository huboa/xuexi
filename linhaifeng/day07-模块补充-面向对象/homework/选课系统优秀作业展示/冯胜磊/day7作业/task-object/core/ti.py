
class Ti(object):
    def run(self):
        import sys,os,pickle
        sys.path.append(os.path.dirname(os.path.dirname(__file__))+"\\"+"module")
        from init_db import init_db
        from modules import School,Classes,Lesson,Schoolmember,Teacher,Student,pickle_wb,pickle_rb


        mgr = """
            校长管理系统
            1、创建讲师
            2、创建班级
            3、创建课程
            4、查看讲师信息
            5、查看班级、课程信息
            6、返回上一级
        """
        mgg="""
            老师管理系统
            1、创建班级
            2、创建课程
            3、查看讲师信息
            4、查看班级、课程信息
            5、返回上一级

        """
        stu = """
            学员管理系统
            1、注册
            2、交学费
            3、选择班级
            4、查看学员信息
            5、返回上一级
        """
        msg = """
            学校管理平台
            1、学校管理系统
            2、讲师管理系统
            3、学员管理系统
            4、退出
        """

        init_db()
        school_bj = School("北京")
        school_sh = School("上海")
        lesson_linux = Lesson("linux",12000,"8 month")
        lesson_python = Lesson("python",16600,"9 month")
        lesson_go = Lesson("go",10000,"5 month")
        mark = True
        while mark:
            print('\033[1;35m %s \033[0m' % msg)
            choice = input("请选择系统 ：")
            if choice == "1":
                while True:
                    print('\033[1;34m %s \033[0m' % mgr)
                    choice = input("请选择功能 ：")
                    if choice == "1":
                        print("创建讲师 ：\n请选择学校：\n1、北京\n2、上海")
                        num = 0
                        while True:
                            school_num = input("请选择学校 ：")
                            if num < 2:
                                if school_num == "1":
                                    school_choice = school_bj.school_name
                                    break
                                elif school_num == "2":
                                    school_choice = school_sh.school_name
                                    break
                                else:
                                    print("请输入正确编号！")
                                    num += 1
                            else:
                                print("尝试次数过多！")
                                exit()
                        teacher_name = input("请输入教师名字 ：")
                        age = input("请输入教师年龄 ：")
                        sex = input("请输入教师性别 ：")
                        teacher_data = school_bj.create_teacher(school_choice,teacher_name,age,sex)
                        teacher_db_data = pickle_rb("teacher_db")
                        teacher_db_data.append(teacher_data)
                        pickle_wb("teacher_db",teacher_db_data)
                    elif choice == "2":
                        classes_data = []
                        c_name_list = []
                        classes_db_data = pickle_rb("classes_db")
                        while True:
                            c_name = input("\n创建班级\n请输入班级编号（格式001） ：")
                            for i in classes_db_data:
                                c_name_list.append(i[0])
                            if c_name in c_name_list:
                                print("班级名称已存在！")
                                print("已有如下班级：")
                                for j in c_name_list:
                                    print(j)
                            else:break
                        school_num = input("\n1、北京(linux与python课程)\n2、上海(go课程)\n请选择学校 ：")
                        lesson_choice = ""
                        if school_num == "1":
                            school_choice = school_bj.school_name
                            lesson_num = input("\n1、linux\n2、python\n请选择课程 ：")
                            if lesson_num == "1":
                                lesson_choice = lesson_linux.lesson_name
                                lesson_choice_cycle = lesson_linux.cycle
                                lesson_choice_price = lesson_linux.price
                            elif lesson_num == "2":
                                lesson_choice = lesson_python.lesson_name
                                lesson_choice_cycle = lesson_python.cycle
                                lesson_choice_price = lesson_python.price
                            else:
                                print("没有这门课程")
                                exit()
                        elif school_num == "2":
                            school_choice = school_sh.school_name
                            lesson_choice = lesson_go.lesson_name
                            lesson_choice_cycle = lesson_go.cycle
                            lesson_choice_price = lesson_go.price
                        else:
                            print("没有此编号！")
                            exit()
                        teacher_data = pickle_rb("teacher_db")
                        teacher_name = {}
                        #teacher_choice = input("请选择讲师 ：")
                        for i,ele in enumerate(teacher_data):
                            teacher_name[i] = ele[1]
                        for key,value in teacher_name.items():
                            #if key == 0:continue
                            #else:
                            print("%s、%s" % (key,value))
                        teacher_choice = input("请选择讲师 ：")
                        classes_data.append(c_name)
                        classes_data.append(school_choice)
                        classes_data.append(lesson_choice)
                        classes_data.append(teacher_name[int(teacher_choice)])
                        classes_data.append(lesson_choice_cycle)
                        classes_data.append(lesson_choice_price)
                        classes_db_data = pickle_rb("classes_db")
                        classes_db_data.append(classes_data)
                        pickle_wb("classes_db",classes_db_data)
                    elif choice == "3":
                        classes_data = []
                        c_name_list = []
                        classes_db_data = pickle_rb("classes_db")
                        school_num = input("\n1、北京(linux与python课程)\n2、上海(go课程)\n请选择学校 ：")
                        lesson_choice = ""
                        if school_num == "1":
                            school_choice = school_bj.school_name
                            lesson_num = input("\n1、linux\n2、python\n请选择课程 ：")
                            if lesson_num == "1":
                                lesson_choice = lesson_linux.lesson_name
                                lesson_choice_cycle = lesson_linux.cycle
                                lesson_choice_price = lesson_linux.price
                            elif lesson_num == "2":
                                lesson_choice = lesson_python.lesson_name
                                lesson_choice_cycle = lesson_python.cycle
                                lesson_choice_price = lesson_python.price
                            else:
                                print("没有这门课程")
                                exit()
                        elif school_num == "2":
                            school_choice = school_sh.school_name
                            lesson_choice = lesson_go.lesson_name
                            lesson_choice_cycle = lesson_go.cycle
                            lesson_choice_price = lesson_go.price
                        else:
                            print("没有此编号！")
                            exit()
                        while True:
                            c_name = input("\n创建班级\n请输入班级编号（格式001） ：")
                            for i in classes_db_data:
                                c_name_list.append(i[0])
                            if c_name in c_name_list:
                                print("班级名称已存在！")
                                print("已有如下班级：")
                                for j in c_name_list:
                                    print(j)
                            else:break
                        teacher_data = pickle_rb("teacher_db")
                        teacher_name = {}
                        for i,ele in enumerate(teacher_data):
                            teacher_name[i] = ele[1]
                        for key,value in teacher_name.items():
                            print("%s、%s" % (key,value))
                        teacher_choice = input("请选择讲师 ：")
                        classes_data.append(c_name)
                        classes_data.append(school_choice)
                        classes_data.append(lesson_choice)
                        classes_data.append(teacher_name[int(teacher_choice)])
                        classes_data.append(lesson_choice_cycle)
                        classes_data.append(lesson_choice_price)
                        classes_db_data = pickle_rb("classes_db")
                        classes_db_data.append(classes_data)
                        pickle_wb("classes_db",classes_db_data)
                    elif choice == "4":
                        teacher_data = pickle_rb("teacher_db")
                        for i,item in enumerate(teacher_data):
                            print(i,item)
                        #input("回车返回上级菜单:")
                    elif choice == "5":
                        classes_db_data = pickle_rb("classes_db")
                        for i,item in enumerate(classes_db_data):
                            print(i,item)
                        #input("回车返回上级菜单:")
                    elif choice == "6":
                        break

            elif choice == "2":
                while True:
                    print('\033[1;33m %s \033[0m' % mgg)
                    choice = input("请选择功能 ：")
                    if choice == "1":

                        classes_data = []
                        c_name_list = []
                        classes_db_data = pickle_rb("classes_db")
                        while True:
                            c_name = input("\n创建班级\n请输入班级编号（格式001） ：")
                            for i in classes_db_data:
                                c_name_list.append(i[0])
                            if c_name in c_name_list:
                                print("班级名称已存在！")
                                print("已有如下班级：")
                                for j in c_name_list:
                                    print(j)
                            else:
                                break
                        school_num = input("\n1、北京(linux与python课程)\n2、上海(go课程)\n请选择学校 ：")
                        lesson_choice = ""
                        if school_num == "1":
                            school_choice = school_bj.school_name
                            lesson_num = input("\n1、linux\n2、python\n请选择课程 ：")
                            if lesson_num == "1":
                                lesson_choice = lesson_linux.lesson_name
                                lesson_choice_cycle = lesson_linux.cycle
                                lesson_choice_price = lesson_linux.price
                            elif lesson_num == "2":
                                lesson_choice = lesson_python.lesson_name
                                lesson_choice_cycle = lesson_python.cycle
                                lesson_choice_price = lesson_python.price
                            else:
                                print("没有这门课程")
                                exit()
                        elif school_num == "2":
                            school_choice = school_sh.school_name
                            lesson_choice = lesson_go.lesson_name
                            lesson_choice_cycle = lesson_go.cycle
                            lesson_choice_price = lesson_go.price
                        else:
                            print("没有此编号！")
                            exit()
                        teacher_data = pickle_rb("teacher_db")
                        teacher_name = {}
                        # teacher_choice = input("请选择讲师 ：")
                        for i, ele in enumerate(teacher_data):
                            teacher_name[i] = ele[1]
                        for key, value in teacher_name.items():
                            # if key == 0:continue
                            # else:
                            print("%s、%s" % (key, value))
                        teacher_choice = input("请选择讲师 ：")
                        teacer_int=int(teacher_choice)
                        if key < teacer_int:
                            print('输入的序号太大，需要从头再来')
                            break
                        classes_data.append(c_name)
                        classes_data.append(school_choice)
                        classes_data.append(lesson_choice)
                        classes_data.append(teacher_name[int(teacher_choice)])
                        classes_data.append(lesson_choice_cycle)
                        classes_data.append(lesson_choice_price)
                        classes_db_data = pickle_rb("classes_db")
                        classes_db_data.append(classes_data)
                        pickle_wb("classes_db", classes_db_data)
                    elif choice == "2":
                        classes_data = []
                        c_name_list = []
                        classes_db_data = pickle_rb("classes_db")
                        school_num = input("\n1、北京(linux与python课程)\n2、上海(go课程)\n请选择学校 ：")
                        lesson_choice = ""
                        if school_num == "1":
                            school_choice = school_bj.school_name
                            lesson_num = input("\n1、linux\n2、python\n请选择课程 ：")
                            if lesson_num == "1":
                                lesson_choice = lesson_linux.lesson_name
                                lesson_choice_cycle = lesson_linux.cycle
                                lesson_choice_price = lesson_linux.price
                            elif lesson_num == "2":
                                lesson_choice = lesson_python.lesson_name
                                lesson_choice_cycle = lesson_python.cycle
                                lesson_choice_price = lesson_python.price
                            else:
                                print("没有这门课程")
                                exit()
                        elif school_num == "2":
                            school_choice = school_sh.school_name
                            lesson_choice = lesson_go.lesson_name
                            lesson_choice_cycle = lesson_go.cycle
                            lesson_choice_price = lesson_go.price
                        else:
                            print("没有此编号！")
                            exit()
                        while True:
                            c_name = input("\n创建班级\n请输入班级编号（格式001） ：")
                            for i in classes_db_data:
                                c_name_list.append(i[0])
                            if c_name in c_name_list:
                                print("班级名称已存在！")
                                print("已有如下班级：")
                                for j in c_name_list:
                                    print(j)
                            else:
                                break
                        teacher_data = pickle_rb("teacher_db")
                        teacher_name = {}
                        for i, ele in enumerate(teacher_data):
                            teacher_name[i] = ele[1]
                        for key, value in teacher_name.items():
                            print("%s、%s" % (key, value))
                        teacher_choice = input("请选择讲师 ：")
                        classes_data.append(c_name)
                        classes_data.append(school_choice)
                        classes_data.append(lesson_choice)
                        classes_data.append(teacher_name[int(teacher_choice)])
                        classes_data.append(lesson_choice_cycle)
                        classes_data.append(lesson_choice_price)
                        classes_db_data = pickle_rb("classes_db")
                        classes_db_data.append(classes_data)
                        pickle_wb("classes_db", classes_db_data)
                    elif choice == "3":
                        teacher_data = pickle_rb("teacher_db")
                        for i, item in enumerate(teacher_data):
                            print(i, item)
                        input("回车返回上级菜单:")
                    elif choice == "4":
                        classes_db_data = pickle_rb("classes_db")
                        for i, item in enumerate(classes_db_data):
                            print(i, item)
                        input("回车返回上级菜单:")
                    elif choice == "5":
                        break

            elif choice == "3":
                while True:
                    print('\033[1;32m %s \033[0m' % stu)
                    choice = input("请选择功能 ：")
                    if choice == "1":
                        stu_list = []
                        stu_db_data = pickle_rb("stu_db")
                        len_stu_db_data = len(stu_db_data)
                        stu_list.append("00" + str(len_stu_db_data))
                        stu_name = input("请输入学生姓名 ：")
                        stu_age = input("请输入学生年龄 ：")
                        stu_sex = input("请输入学生性别 ：")
                        stu_data = Student(stu_name, stu_age, stu_sex)
                        stu_list.append(stu_data.name)
                        stu_list.append(stu_data.age)
                        stu_list.append(stu_data.sex)
                        stu_list.append("未付款")
                        stu_list.append("未选择")
                        stu_db_data = pickle_rb("stu_db")
                        stu_db_data.append(stu_list)
                        pickle_wb("stu_db", stu_db_data)

                    elif choice == "2":
                        stu_db_data = pickle_rb("stu_db")
                        stu_unpay = []
                        stu_unpay_id = []
                        stu_id = []
                        for i in stu_db_data:
                            if i[4] == "未付款":
                                stu_unpay_id.append(i[0])
                                stu_unpay.append(i)
                        if len(stu_unpay_id) == 0:
                            a = input("不存在未付款的学员，回车键返回。")
                            break
                        else:
                            print("如下同学还未付款 ：")
                            for i in stu_unpay:
                                print(i)
                        for i in stu_db_data:
                            stu_id.append(i[0])
                        pay_id = input("\n请输入付款学员的编号 ：")
                        if pay_id not in stu_id:
                            a = input("没有这个学员编号，请输入正确学员编号，回车键返回")
                            break
                        elif pay_id in stu_id and pay_id not in stu_unpay_id:
                            a = input("这个学员已付款，回车键返回")
                        elif pay_id in stu_unpay_id:
                            for i in stu_db_data:
                                if pay_id == i[0]:
                                    i[4] = "已付款"
                        pickle_wb("stu_db", stu_db_data)
                        a = input("编号：%s，此学员已付款完毕，回车键返回。" % (pay_id))

                    elif choice == "3":
                        stu_db_data = pickle_rb("stu_db")
                        stu_unchoice = []
                        stu_unchoice_id = []
                        stu_id = []
                        classes_db_data_id = []
                        for i in stu_db_data:
                            if i[5] == "未选择":
                                stu_unchoice_id.append(i[0])
                                stu_unchoice.append(i)
                        if len(stu_unchoice_id) == 0:
                            a = input("不存在未选课的学员，回车键返回。")
                            break
                        else:
                            print("如下同学还未选课 ：")
                            for i in stu_unchoice:
                                print(i)
                        for i in stu_db_data:
                            stu_id.append(i[0])
                        choice_id = input("\n请输入选课学员的编号 ：")
                        print("\n")
                        if choice_id not in stu_id:
                            a = input("没有这个学员编号，请输入正确学员编号，回车键返回")
                            break
                        elif choice_id in stu_id and choice_id not in stu_unchoice_id:
                            a = input("这个学员已选课，回车键返回")
                        elif choice_id in stu_unchoice_id:
                            classes_db_data = pickle_rb("classes_db")
                            for i, item in enumerate(classes_db_data):
                                classes_db_data_id.append(item[0])
                                print(item[0], item)
                            classes_id = input("请选择班级编号（如：001） :")
                            if classes_id not in classes_db_data_id:
                                a = input("没有这个班级，请输入正确班级号，回车键返回。")
                                break
                            else:
                                for i in stu_db_data:
                                    if choice_id == i[0]:
                                        i[5] = classes_id
                            pickle_wb("stu_db", stu_db_data)
                            a = input("编号：%s学员，已选择班级%s，回车键返回:" % (choice_id, classes_id))

                    elif choice == "4":
                        stu_data = pickle_rb("stu_db")
                        for i, item in enumerate(stu_data):
                            print(i, item)
                        input("回车返回上级菜单。")
                    elif choice == "5":
                        break
            elif choice == "4":
                exit()
            else:
                a = input("请输入正确编号！按回车键返回:")
        return

