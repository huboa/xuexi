
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]
goods_list=[{0:0}] ##保持编号对齐
###总资产
monney=0

###显示并制作新列表加入id 号
n=0
for good in goods:
    n += 1
    good_dic={n:good}
    goods_list.append(good_dic)
print(goods_list)



dic={1: "123"}
print(dic[1])

# goods_list=[{1: {'name': '电脑', 'price': 1999}}, {2: {'name': '鼠标', 'price': 10}}, {3: {'name': '游艇', 'price': 20}}, {4: {'name': '美女', 'price': 998}}]
###购物车
cart_list=[]
while True:
    print('==============商品信息===============')
    print('编号  名称  价格')
    n=0
    for key in goods_list:
        print(key[n])
        n += 1
        # print('  %d   %s  %s' % (n, good[n]["name"], good[n]["price"]))
    print('==============商品信息===============')

#
    choice=input("请输入商品编号:").strip()
    print(goods_list[1][int(choice)])

