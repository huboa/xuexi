#!/usr/bin/env python3
#__author__:"shengchong.zhao"

import os
import sys
import json

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)
base_dir = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(base_dir)

from core import auth
from core import main
# from core import login
from db    import DBOpt



def user_auth(func):
    def inner():
        global user_status
        while True:
            print(__name__)
            _user_id = input("请输入id号>>:")
            #判断用户是否存在
            if _user_id.isdigit():
                _user_id = int(_user_id)
                if os.path.isfile('../db/%s' %_user_id):
                    user_id = DBOpt.readDB(_user_id)
                    # print("get:", user_id['id'], type(user_id['id']))
                    # print("input:", _user_id, type(_user_id))

                    if user_id['id'] == _user_id:
                        ###判断密码
                        _passwd = input("请输入密码>>:")
                        passwd = DBOpt.readDB(_user_id)
                        print(passwd['password'])
                        passwd = passwd['password']
                        # print("获取的",type(passwd),passwd)
                        # print("输入的pass",type(_passwd),_passwd)
                        if _passwd == passwd:
                            print("welcome login...")

                            user_status = True
                            if user_status == True:
                                func()
                            return False
                        else:
                            print("密码错误")

                    else:
                        print("密码不存在")
                else:
                    print("用户不存在")
            else:
                print("请输入id")

    return inner



