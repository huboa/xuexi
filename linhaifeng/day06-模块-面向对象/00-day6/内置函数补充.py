#与匿名函数结合使用
#max,min,sorted


salaries={
'egon':3000,
'alex':100000000,
'wupeiqi':10000,
'yuanhao':2000
}


# print(max(salaries))
# print(max(salaries.values()))

# t1=(1,'h',3,4,5,6)
# t2=(1,'y',3)
# print(t1 > t2)

# t1=(10000000,'alex')
# t2=(3000,'egon')
# print(t1 > t2)


# print(max(zip(salaries.values(),salaries.keys()))[1])
# def get_value(name):
#     return salaries[name]



# print(max(salaries,key=get_value))
# l=[]
# for name in salaries:
#     res=get_value(name)
#     l.append(res)
# print(max(l))

# lambda name:salaries[name]

# print(max(salaries,key=lambda name:salaries[name]))
# print(min(salaries,key=lambda name:salaries[name]))


# salaries={
# 'egon':3000,
# 'alex':100000000,
# 'wupeiqi':10000,
# 'yuanhao':2000
# }
# def get_value(name):
#     return salaries[name]
# print(sorted(salaries))
# print(sorted(salaries,key=get_value))
# print(sorted(salaries,key=get_value,reverse=True))



#filter,map,reduce
# names=['alex','wupeiqi','yuanhao','yanglei','egon']
#
#
# res=map(lambda x:x if x == 'egon' else x+'SB',names)
# print(res)
# print(list(res))


# def my_map(func,seq):
#     for item in seq:
#         yield func(item)
#
# res1=my_map(lambda x:x+'_SB',names)
# print(next(res1))
# print(next(res1))
# print(next(res1))


# from functools import reduce
# print(reduce(lambda x,y:x+y,range(101),100))
# print(reduce(lambda x,y:x+y,range(101)))
#
# l=[1,2,'a','b',3,'c','d']






names=['alex_SB','wupeiqi_SB','yuanhao_SB','yanglei_SB','egon']
print(list(filter(lambda name:name.endswith('SB'),names)))


