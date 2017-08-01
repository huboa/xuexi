#coding:utf-8

goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

shopping_car=[]
while True:
    # 获取总资产
    total_assets = input('请输入你的总资产:').strip()
    if len(total_assets) == 0:
        continue
    else:
        if total_assets.isdigit():
            total_assets = int(total_assets)
            print('您的总资产：%d' % total_assets)
            break
        else:
            print('您输入的不符合标准:')
            continue

while True:

    #显示商品信息
    n=1
    print('-----------商品信息-----------')
    for good in goods:
        good['id']=n

        print('商品编号：%d ,商品名称：%s ,商品价格：%d' %(n,good['name'],good['price']))
        n+=1
    print('-----------------------------')
    #
    #



    while True:
        choice = input('请选择商品：').strip()
        if len(choice) == 0:
            continue
        else:
            if choice.isdigit():
                n=0
                for good in goods:
                    if int(choice) == good['id']:
                        #加入到购物车
                        shopping_car.append((good['name'],good['price']))
                        n=1
                if n == 0:
                    print('你选择的商品不存在：')
                else:

                    #显示购物车
                    print('-----------购物车信息-----------')
                    if len(shopping_car) == 0:
                        print('购物车为空')
                    else:
                        for value in shopping_car:
                            print('商品名称：%s ,商品价格：%d' % (value[0], value[1]))
                    print('-----------------------------')
                    break





    # 结算
    while True:
        is_buy=input('结算请输入y，继续选择商品按任意键').strip()
        if len(is_buy) != 0 and is_buy == 'y':
            total_price=0
            for i in shopping_car:
                total_price+=i[1]
            print('您购买的商品总价格为：%d' %total_price)
            if total_price > total_assets:
                print('余额不足。您的余额为%d' %total_assets)
                break
            else:
                total_assets=total_assets-total_price
                print('购买成功,余额为%d' %total_assets)
                shopping_car.clear()
                break

        else:
            break

