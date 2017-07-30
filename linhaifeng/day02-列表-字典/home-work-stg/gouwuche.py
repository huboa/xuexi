'''购物车
功能要求：

要求用户输入总资产，例如：2000
显示商品列表，让用户根据序号选择商品，加入购物车
购买，如果商品总额大于总资产，提示账户余额不足，否则，购买成功。
附加：可充值、某商品移除购物车'''
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "娃娃", "price": 3998},
    {"name": "气筒", "price": 99},
]
kong=[]
while True:
    qian = input('请输入您要充值的Q币： ').strip()
    if qian.isdigit():
        qian = int(qian)
    else:
        print('\033[41m不要瞎输入，难道你一毛钱都没有???\033[1m')
        continue
    while True:
        for k,v in enumerate(goods) :
            print(k,'商品: {name}  价格: {price} Q币'.format(price=v['price'],name=v['name']))
        sp=input('请输入购买的商品编号[输入qq充值][输入r删除购物车商品][输入q退出]： ').strip()
        print('\033[41m您还有：%s(Q币)\033[1m ' % qian)
        if sp =='q'and len(sp)!=0:
            exit()
        elif sp == 'r':
            while True:
                if kong==[]:
                     print('======================》没有商品可删了《=====================')
                     break
                print('您以购买的商品： ')
                for k, v in enumerate(kong):     #for循环显示已购买的商品
                    print(k,'商品: {name}  价格: {price} Q币'.format(price=v[1],name=v[0]))
                sc = input('请输入删除的商品编号[输入q退出]： ').strip()
                print('\033[41m您还有：%s(Q币)\033[1m ' % qian)
                if sc == 'q' :
                    break
                if sc.isdigit():
                    if int(sc) < len(kong) and int(sc)>=0 :   #判断输入的数字不能大于列表的下标数字和小于0
                             qian+=int(kong[int(sc)][1])       #计算删除商品后剩余的钱
                             kong.remove(kong[int(sc)])        #删除购物车商品
                    else:
                        print('！！！！！！！！！！！！！！！！无效的输入！！！！！！！！！！！！！！！！！！！')
                else:
                    print('\033[42m请输入要删除的商品编号哦~\033[0m')
        elif sp == 'qq':
            while True:
                x = input('请输入充值金额： ').strip()
                if len(kong)<0:
                    continue
                elif x.isdigit():
                    qian +=int(x)
                    print('\033[41m您还有：%s(Q币)\033[1m ' % qian)
                    break
                else:
                    print('还想不想充Q币了！！！还想不想充Q币了！！！还想不想充Q币了！！！')
        elif sp.isdigit():
            if int(sp) <len(goods) and int(sp) >=0 :
                jiaqian = goods[int(sp)]['price']
                mingzi = goods[int(sp)]['name']
                if  jiaqian <= qian :
                    qian-=jiaqian
                    kong.append((mingzi,jiaqian))
                    print('\033[42m您以购买的商品：=========》%s《========\033[0m' % kong)
                    print(kong)
                else :
                    print('\033[41m《《《《《Q币不够了~还剩%s(Q币)快快输入qq充值去!》》》》》\033[2m'%qian)
            else:
                print('>>>>>>>>>>>>>>>>>不要瞎搞!!!按提示操作!!!不要瞎搞!!!<<<<<<<<<<<<<<<<<<<<<')

        else:
                print('>>>>>>>>>>>>>>>>>不要瞎搞!!!按提示操作!!!不要瞎搞!!!<<<<<<<<<<<<<<<<<<<<<')









