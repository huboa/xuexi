###与匿名函数结合使用
##max,min,sorted
##filter,map,reduce
salaries={
    'zsc':3000000,
    'zxx':10000,
    'zz':20000,
    'wht':3000
}

# print(max(salaries.values()))
# t1=(1,'y',33)
# t2=(2,'z',33)
# t1=(300000,'zsc')
# t2=(1000,'zxx')
#
# print(t1>t2)
# print(list(zip(salaries.values(),salaries.keys())))
# print(max(list(zip(salaries.values(),salaries.keys())))[1])

#简单写法

def get_value(name):
    return salaries[name]
#lambda name:salaries[name]

print(max(salaries,key=lambda name:salaries[name]))
print(min(salaries,key=lambda name:salaries[name]))
print(sorted(salaries,key=lambda name:salaries[name]))
print(sorted(salaries,key=lambda name:salaries[name],reverse=True))
print(sorted(salaries,key=get_value,reverse=True))

##filter,map,reduce
names=['alex','wupeiqi','laonanhai','egon']
print(map(lambda x:x+"_SB",names))
res=map(lambda x:x+"_SB",names)
print(list(res))
res=map(lambda x:x if x == 'egon'else x+"_sb",names)
print(list(res))

from functools import reduce
print(reduce(lambda x,y:x+y,range(101)))
print(reduce(lambda x,y:x+y,range(101),100))

names=['alex_SB','wupeiqi_SB','laonanhai_DB','egon']
print(filter(lambda name:name.endswith('SB'),names))


