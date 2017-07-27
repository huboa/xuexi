#!/usr/bin/env python
# -*- coding: utf-8 -*-

import getpass
name_ori="zsc"
pwd_ori="123456"
lock_state = 0
mistake = 0

for i in range(10):
    if lock_state == 1:
        print("您的账号已经锁定请联系管理员")
        break  # 不往下走了,直接跳出整个loop

    name = input("请输入用户名：")
    pwd = getpass.getpass("请输入密码：")


    if name == name_ori and pwd == pwd_ori:
        print("欢迎，zsc ！登陆成功")
    else:
        print("用户名和密码错误")
        mistake += 1
        print("错误:",mistake,"次")

    if mistake == 3:
        lock_state = 1
        print("错误3次锁定账户")



