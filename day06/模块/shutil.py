import os
import sys
import shutil

#
# ret = shutil.make_archive("ttt", 'gztar', root_dir='./1234')
#

# shutil.copyfile('/Users/ZSC/PycharmProjects/python-s15/day06/模块/1234','/Users/ZSC/PycharmProjects/python-s15/day06/模块/4321')
import shutil
shutil.copyfile('/Users/ZSC/PycharmProjects/python-s15/day06/模块/shutil.py','/Users/ZSC/PycharmProjects/python-s15/day06/模块/111.txt')
# import zipfile
#
# # 压缩
# z = zipfile.ZipFile('up.zip', 'w')
# z.write('a.log')
# z.write('data.data')
# z.close()
#
# # 解压
# z = zipfile.ZipFile('up.zip', 'r')
# z.extractall()
# z.close()
#
#
# close# zipfile 压缩解压