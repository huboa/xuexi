#!/usr/bin/env python
# -*- coding:utf-8 -*-
asset = int(input("You wallet how much money: "))
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998}
]
num = 1
for i in goods:
    print(num, i.get("name"), i.get("price"))
    num += 1
goods_index = input('请选择菜单 ：购物(c) | 余额充值(r)  | 退出(q) : ')
buy_list = []
buy_list_now = {}
tag = True
while tag:
    if goods_index == "c":
        while tag:
            choice = int(input("请输入商品编号: ").strip())
            choice -= 1
            item_price = (goods[choice]['price'])
            if item_price < asset:
                buy_list.append(goods[choice]['name'])
                shopping_list = {goods[choice]['name']: buy_list.count(goods[choice]['name'])}
                asset -= item_price
                print("你的余额还有 %s " % asset)
                buy_list_now.update(shopping_list)
                print(buy_list_now)
                goods_index=input('请选择菜单 ：购物(c) | 余额充值(r) | 退出(q) : ')
                if goods_index == "r":
                    recharge = int(input("输入你想充值的金额："))
                    asset += recharge
                    print("您的账号余额是：", asset)
                    goods_index = input('请选择菜单 ：购物(c)  | 退出(q) : ')
                elif goods_index == "q":
                    print("您购买了这些商品", buy_list_now)
                    break
            if asset <= item_price:
                print("余额不足")
                goods_index = input('请选择菜单 ：购物(c) | 余额充值(r)  | 退出(q) : ')
            # if choose == 1:
                if goods_index == "r":
                    recharge = int(input("输入你想充值的金额："))
                    asset += recharge
                    print("您的账号余额是：", asset)
                    # goods_index = input('请选择菜单 ：购物车(c) : ')
    elif goods_index == "r":
        recharge = int(input("输入你想充值的金额："))
        asset += recharge
        print("您的账号余额是：", asset)
        goods_index = input('请选择菜单 ：购物(c) | 余额充值(r)  | 退出(q) : ')
        # goods_index = "c"
    elif goods_index == "q":
        break
        print("您购买了这些商品", buy_list_now)

    else:
        goods_index = input('请选择菜单 ：购物车(c) | 余额充值(r) | 退出(q) : ')
