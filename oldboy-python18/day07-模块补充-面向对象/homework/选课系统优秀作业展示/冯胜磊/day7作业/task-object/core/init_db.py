# 此程序作为初始化数据库
import sys,os
sys.path.append(os.path.dirname(os.path.dirname(__file__))+"\\"+"module")
from modules import pickle_wb,pickle_rb

teacher_db = [["学校","讲师","年龄","性别"]]
classes_db = [["班级","学校","课程","讲师","周期","价格"]]
stu_db = [["编号","姓名","年龄","性别","学费","班级"]]

def init_db():
    if "teacher_db" not in os.listdir(os.path.dirname(os.path.dirname(__file__))+"\\"+"db"):
        pickle_wb("teacher_db", teacher_db)


    if "classes_db" not in os.listdir(os.path.dirname(os.path.dirname(__file__))+"\\"+"db"):
        pickle_wb("classes_db", classes_db)

    if "stu_db" not in os.listdir(os.path.dirname(os.path.dirname(__file__))+"\\"+"db"):
        pickle_wb("stu_db", stu_db)
