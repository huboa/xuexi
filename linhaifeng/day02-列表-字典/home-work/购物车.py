
goods = [
    {"name": "电脑", "price": 1999},
    {"name": "鼠标", "price": 10},
    {"name": "游艇", "price": 20},
    {"name": "美女", "price": 998},
]

###总资产
monney=0

###显示
print('==============商品信息===============')
n=0
for good in goods:

    n += 1
    good['id'] = n
    print('商品编号：%d ,商品名称：%s ,商品价格：%d' % (n, good['name'], good['price']))

print('==============商品信息===============')