# res=sum(i for i in range(3))
# print(res)

# with open('db.txt',encoding='utf-8') as f:
#     l=(float(line.split()[1])*int(line.split()[2]) for line in f)
#     print(sum(l))


    # l=[]
    # for line in f:
    #    goods=line.split()
    #    price=float(goods[1])
    #    count=int(goods[2])
    #    cost=price * count
    #    l.append(cost)
    #
    # print(sum(l)) #196060.0

# [{'name': 'apple', 'price': 333, 'count': 3}, ]
with open('db.txt',encoding='utf-8') as f:
    info=[{'name':line.split()[0],
      'price':float(line.split()[1]),
      'count':int(line.split()[2])} for line in f if float(line.split()[1]) >= 30000]
    print(info)
