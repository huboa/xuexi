import os
#
# cmd="print('ok')"
# print(cmd,type(cmd))
# eval(cmd)
#
dic='{"name":"alex","password":"alex3714"}'
print(eval(dic),type(eval(dic)))
dic1=eval(dic)
# d=eval(dic)
# print(dic1["name"])
# for n in dic1:
#      print(n,dic1[n])
# print(dic)

with open('db.txt','w',encoding='utf-8') as f:
    f.write(dic+"\n")
    f.writelines(dic+"\n")
with open('db.txt','r',encoding='utf-8') as f:
    print(f.read())
with open('db.txt', 'r', encoding='utf-8') as f:
    for n in f:
        f.readline()

#
# with open('db.txt','w',encoding='utf-8') as f:
#       for i in dic:
#       #    f.writelines(i)
#           print(i)
#      f.writelines(dic)
# with open('db.txt', 'r', encoding='utf-8') as f:
#      for line in f:
#           print(line)

# line     print(f.read())
#      dic=f.read()
# print(lines)
# print(type((lines)))
