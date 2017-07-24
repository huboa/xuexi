import os
#
# cmd="print('ok')"
# print(cmd,type(cmd))
# eval(cmd)
#
dic='{"name":"alex","password":"alex3714"}'
# print(eval(dic),type(eval(dic)))
# d=eval(dic)

with open('db.txt','w',encoding='utf-8') as f:
     f.write(dic)
     f.write(dic)
with open('db.txt', 'r', encoding='utf-8') as f:
     lines=f.readline()

     print(f.read())
     dic=f.read()
print(lines)
print(type((lines)))
