import copy
# dic={'name':'alex','age':18}
# dic.clear()
# print(dic)
#
# dic1=dic.copy()
# print(dic1)
#
# dic1=dict.fromkeys('abc',1)
# print(dic1)

dic={'name':'alex','age':18}


#dic.get('name')

# print(dic.items('name'))
#
# for i in dic.items():
#     print(i)
#
# for k,v in dic.items():
#     print(k,v)
#
# print(dic.keys())
# for i in dic.keys:
#     print("key is %s ,value is %s" %(i,dic[i]))

dic.popitem()
print(dic)
dic.setdefault('gender','male')
print(dic)
print(dic.setdefault('gender'))