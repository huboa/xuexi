# dic={'name':'alex','age':18}
# ##查寻
# print(dic['name'])
#
# print(dic.get('name3'))
#
#
# ##add
# dic['gender']='female'
# print(dic)    ##无序列 随机
#
# ###moddify
#
# dic['name']='zsc'
# print(dic)
#
# ###del
# del dic['name']
# print(dic)
#
#
# ###key 的定义规则
# ##1、不可变：数字，字符串、元祖
# ##2、可变列表，列表，
# ##元祖：定义符号（），与列表完全一致，元祖不可变

dic={
    "nn":'alex',
    'name':'zsc',
    2:{'age':18},
    (1,2,3):"ttt"
}

print(dic[2])
print(dic['name'])
print(dic[(1,2,3)])

#age=18--int()-->__init__()
#dic={}---dict()--->_init__()
# a=(1,2,3)
# print(a)
# print(dic.get(2))
# print(dic.get(1))
#

# for k in dic:
#     print(k,dic[k])
