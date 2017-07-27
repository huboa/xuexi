import os
import json
#
# cmd="print('ok')"
# print(cmd,type(cmd))
# eval(cmd)
#

##列表的写
ipTable = ['158.59.194.213', '18.9.14.13', '58.59.14.21']

with open('iptables.txt', 'w', encoding='utf-8') as f:
    for ip in ipTable:
        f.write(ip)
        f.write('\n')



###字典的写
dictObj = {
        'andy': {
            'age': 23,
            'city': 'shanghai',
            'skill': 'python'
        },
        'william': {
            'age': 33,
            'city': 'hangzhou',
            'skill': 'js'
        }
    }

jsObj = json.dumps(dictObj)

with open('jsonFile.json', 'w',encoding='utf-8') as f:
    f.write(jsObj)
    f.write("\n")
    f.write(jsObj)

####字典的读
#dic='{"name":"zsc","password":"123"}'
# print(eval(dic),type(eval(dic)))
# dic1=eval(dic)
# # d=eval(dic)
# print(dic1["name"])
# for n in dic1:
#      print(n,dic1[n])
# print(dic)

with open('jsonFile.json','r',encoding='utf-8') as f:
     while True:
         ff=f.readline()

         print(type(ff))

print(ff)

##http://blog.csdn.net/qinglu000/article/details/44981701

# with open('db.txt','r',encoding='utf-8') as f:
#     print(f.read())


#
# with open('db.txt', 'r', encoding='utf-8') as f:
#
#     for line in f.readlines():
#         print(line.strip())
#
