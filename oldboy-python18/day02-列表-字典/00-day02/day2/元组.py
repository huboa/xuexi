age=(11,22,33,44,55,33)# 本质age=tuple((11,22,33,44,55))

# print(age[2])
# print(age[1:4])
# print(len(age))
#
# print(11 in age)


# print(age.index(33))
# print(age.count(33))


#元组练习
msg_dic={
'apple':10,
'tesla':100000,
'mac':3000,
'lenovo':30000,
'chicken':10,
}
goods_l=[]

while True:
    for key in msg_dic:
        # print('Goods Name:%s Price:%s' %(key,msg_dic[key]))
        print('\033[43mName:{name} Price:{price}\033[0m'.format(price=msg_dic[key],name=key))
    choice=input('your goods name>>: ').strip()
    if len(choice) == 0 or choice not in msg_dic:continue
    count=input('your count>>: ').strip()
    if count.isdigit():
        goods_l.append((choice,msg_dic[choice],int(count)))
    print(goods_l)
