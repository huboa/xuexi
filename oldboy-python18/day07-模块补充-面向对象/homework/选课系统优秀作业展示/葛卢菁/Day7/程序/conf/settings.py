#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author: gelujing

import os

base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

db_path = "%s/db" % base_path                       #数据库路径
db_file = os.path.join(db_path,"db.pk")   #数据库文件绝对路径
