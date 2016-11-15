#!/usr/bin/env python
# -*- coding: utf-8 -*-

products =[["Mac",15800],["Ipone",5800],["bike",2000],["Coffee",30]]


salary = input("input you salary >>:")
if salary.isdigit():
    salary = int(salary)
else:
    print("请输入数字")

while True:
    print("您的工资为：",salary)

    print("商品列表为")

    for i,ele in enumerate(products):
        print(i,ele[0],ele[1])

    n = input(" 请输入要购买商品的ID>>:")
    if n.isdigit():
        n = int(n)
    else:
        continue
    if n >= 0 and n < len(products): ##判断数据的数字
        p=products[n]
        print(p)




gou_wu_che = []

