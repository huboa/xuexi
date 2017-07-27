# info={'name':'egon','age':18,'sex':'male'}
# #本质info=dict({'name':'egon','age':18,'sex':'male'})
#
# print(info['age'])
# info['height']=1.80
#
# print(info)
#
# for key in info:
#     print(key)


#字典的key必须是不可变类型，也成为可hash类型
# info={(1,2):'a'}
# print(info[(1,2)])

#字典常用的方法(优先掌握)
# info={'name':'egon','age':18,'sex':'male'}
# print(info.pop('name'))
# print(info)
# print(info.pop('asdfsadfasdfasfasdfasdfasdf',None))
#
#
#
# print(info['name'])
# print(info.get('name1'))
# print(info.get('nameasdfasdfasdfasdf','not key'))


#字典其他的方法
info={'name':'egon','age':18,'sex':'male'}
# print(info.popitem())
# print(info.popitem())
# print(info)
# #
# print(info.keys(),type(info.keys()))
# print(info.values())

# for key in info.keys():
#     print(key)

# for key in info.values():
#     print(key)
#
for key in info:
    print(key,info[key])

# print(info.items())
# for key,value in info.items(): # key,value=('name','egon')
#     print(key,value)


# msg_dic={
# 'apple':10,
# 'tesla':100000,
# 'mac':3000,
# 'lenovo':30000,
# 'chicken':10,
# }
# for key,value in msg_dic.items():
#     print(key,value)


# info={'name':'egon','age':18,'sex':'male'}
# info.clear()
# print(info)

# print(info.items())
# dic=info.fromkeys(['name','age','sex'],11111111)
# print(dic)
#
# dic=info.fromkeys(['name','age','sex'],None)
# print(dic)

#
# dic=dict(a=1,b=2,c=3)
# print(dic)

# print(info.items())

# print(dict([('name', 'egon'), ('age', 18), ('sex', 'male')]))


# dic=dict.fromkeys(['name','age','sex'],11111111)
# print(dic)
# print(info)





# print(info)
# dic={'a':1,'b':2,'name':'SHUAI'}
# info.update(dic)
# print(info)


# d=dict.setdefault(['a','b','c'],[])
# print(d)
#
# d={}
# print(d)
# d['name']='egon'
# d['age']=18
# d['sex']='male'
# # d['hobby']=[]
# # d['hobby'].append('play basketball')
# # d['hobby'].append('play football')
#
# d.setdefault('hobby',[]).append('play1') #d['hobby']
# d.setdefault('hobby',[]).append('play2') #d['hobby']
# d.setdefault('hobby',[]).append('play3') #d['hobby']
# print(d)