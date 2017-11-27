#!/usr/bin/env python3
#_*_conding:utf-8_*_

#sys模块用于传递参数，os模块用于与系统交互.
import sys,os
old_file = sys.argv[1]
new_file = sys.argv[2]
file_path = sys.argv[3]

f = open(file_path,"r")
f1 = open("back","a+")
for i in f:
    if old_file in i:
        i = i.replace(old_file,new_file)
    f1.write(i)
    f1.flush()
f.close()
f1.close()
os.remove(file_path)
os.rename("back",file_path)