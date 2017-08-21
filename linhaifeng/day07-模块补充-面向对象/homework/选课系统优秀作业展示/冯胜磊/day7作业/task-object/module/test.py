import pickle
import os
import pprint
info=[1,2,3,'abc','iplaypthon']
#print('原始数据')
#pprint.pprint(info)
data1=pickle.dumps(info)
data2=pickle.loads(data1)

#print(data1)
#print(data2)

#f = open(os.path.dirname(os.path.dirname(__file__))+"\\"+aa,"rb")
#print(os.path.dirname('D:/zong/python/xin/test-lian/day7/school_management/module')+"\\"+aa)
#data = pickle.loads(f.read())
'''
file won't be set if you're writing this in the interpretor

__file__ is the name of the file that was called by the python interpretor - so if you ran this from a
script it would school_management
the script is exactly the same as what i put into the interpretor hence no error or output

from what i've observed using IDLE before,it acts as an interpretor - so it'll run the file in question
however,it wasn't started with that file,so the __file__ is never set

'''
import sys, os, pickle

sys.path.append(os.path.dirname(os.path.dirname(__file__)) + "\\" + "module")
##from init_db import init_db
from school import School
from lesson import Lesson
from classes import Classes
from school_member import Schoolmember, Teacher, Student
from pickle_file import pickle_wb, pickle_rb
#
# teacher_data = pickle_rb("teacher_db")
# #print(teacher_data)
# teacher_name = {}
# for i,ele in enumerate(teacher_data):
#     print(i)
#     print(ele)
#     teacher_name[i] = ele[1]
#     print(ele[1])
# for key, value in teacher_name.items():
#     # if key == 0:
#     #     continue
#     # else:
#     print("%s、%s" % (key, value))

import codecs
import time
import sys

# with codecs.open('aa','r','utf-8') as f:
# 	line=f.readlines()
# sys.stdout.write('')
# for i in line:
# 	for li in i:
# 		time.sleep(0.2)
# 		sys.stdout.write(li)
# 		sys.stdout.flush()
# print(i)
