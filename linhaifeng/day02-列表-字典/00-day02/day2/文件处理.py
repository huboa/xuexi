# f=open('a.txt','r',encoding='utf-8')
# res=f.read()
# print(res)
# print('第二次',f.read())

# print(f.readline(),end='')
# print(f.readline(),end='')

# print(f.readlines())
# print(f)
# f.close()
# print(f)
# f.read()



# with open('a.txt','r',encoding='utf-8') as f,open('b.txt') as f1:
#     pass


# f=open('a.txt','w',encoding='utf-8')
#
# f.write('11111\n')
# f.write('2222\n')
# f.write('3333\n4444\n')
#
# f.writelines(['a\n','b\n','c\n'])
#
# f.close()




# import os
# with open('old.txt','r',encoding='utf-8') as read_f,\
#     open('.old.txt.swap','w',encoding='utf-8') as write_f:
#     msg=read_f.read()
#     # print(msg,type(msg))
#     msg=msg.replace('alex','SB')
#     # print(msg)
#     write_f.write(msg)
#
# os.remove('old.txt')
# os.rename('.old.txt.swap','old.txt')




import os
with open('old.txt','r',encoding='utf-8') as read_f,\
    open('.old.txt.swap','w',encoding='utf-8') as write_f:
    for line in read_f:
        if 'SB' in line:
            line=line.replace('SB','alex')
        write_f.write(line)
os.remove('old.txt')
os.rename('.old.txt.swap','old.txt')












