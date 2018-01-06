#!/usr/bin/env python
#_*_ coding:utf-8 _*_
# Author: gelujing

import pickle

class Db_handler:
    '''数据库操作类'''

    def __init__(self,db_file):
        self.db_file = db_file

    def read_db(self): #读
        with open(self.db_file,"rb") as f:
            data = pickle.load(f)
        return data

    def write_db(self,data): #写
        with open(self.db_file,"wb") as f:
            pickle.dump(data,f)
