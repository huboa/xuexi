# f=open('a.txt','r',encoding='utf-8')
# print(f.read(3))


# f=open('a.txt','rb')
# print(f.read(6).decode('utf-8'))
# print(f.read(3).decode('utf-8'))


# f=open('a.txt','rb')
# print(f.read(3))
# print(f.tell())
# f.seek(3,0)
# print(f.tell())
# print(f.read(3).decode('utf-8'))


#
# f=open('a.txt','rb')
# print(f.read(3))
# print(f.tell())
# f.seek(3,1)
# print(f.tell())
# print(f.read().decode('utf-8'))



#
# f=open('a.txt','rb')
# f.seek(0,2)
# print(f.tell())
# print(f.read())











#python3 tail.py -f access.log
# import time
# import sys
#
#
# with open(r'%s' %sys.argv[2],'rb') as f:
#     f.seek(0,2)
#
#     while True:
#         line=f.readline()
#         if line:
#             print(line)
#         else:
#             time.sleep(0.2)



# with open('acess.log','a') as f:
#     f.write('1111\n')

#
# with open('a.txt','r+',encoding='utf-8') as f:
#     f.truncate(2)

#
with open('a.txt','r',encoding='utf-8') as f:
    # l=f.readlines()
    # print(l)
    # for line in l:
    #     print(line,end='')
    # res=f.read()
    # print(type(res))
    for line in f.read():
        print(line)


# l=[1,2,3,4,5]
# # for index in range(len(l)):
# #     # print(index)
# #     print(l[index])
#
# for item in l:
#     # print(index)
#     print(item)