
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

###资产的初始化

cart_dic={}
cart_cost = 0   #cost 需要花的钱
money=0
while True:
    print("you money ", money)
    key1 = input('请输入要充值金额,q去购物]：').strip()
    if key1 == 'q':
        break
    if key1.isdigit():
        money = int(key1)+money

while True:

##显示商品信息
    print('===商品信息start===')
    print('编号  名称  价格')
    n=1
    for good in goods:
        print('  %d   %s  %s' % (n, good["name"], good["price"]))
        n += 1
    print('===商品信息end===')


##输入选项
    good_c=1
    print('您的余额是%s'% money)
    choice=input("请输入商品编号加入购物车,q 退出 :").strip()
    if choice == '':continue    ###空则跳过
    if choice =="q":break
    if choice.isdigit():
         choice = int(choice)  ##转换成数字
    else:
        print("请输入数字")
        continue

    good_all_c=range(1,len(goods)+1)
    if choice not in good_all_c:
        print("编号错误,请重新输入")
        continue

###购物车相关
    if money >= cart_cost + goods[choice-1]["price"]:     ##钱够不够.
        if choice not in cart_dic.keys(): cart_dic[choice] = 0  # 字典key不存在,初始化0
        cart_dic[choice]= cart_dic[choice] +1   #添加购物车
    else:
        print('您的余额是%s,不能购买' % money)
        continue
    print('=======购物车start =======')


    print('编号  名称   单格      数量 合计')


    for n in cart_dic:    ###显示购物车
        print('  %d   %s   %d    %d  %d '% (n,goods[n-1]["name"],goods[n-1]["price"], cart_dic[n],goods[n-1]["price"]*cart_dic[n]))
        cart_cost=cart_cost+goods[n-1]["price"]*cart_dic[n]

    print("                       总计:  ", cart_cost)
    print('=======购物车 end =======',"\n")


