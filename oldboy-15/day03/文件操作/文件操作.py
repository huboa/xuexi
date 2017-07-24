###全部读取文件

# data=open("file").read()   ###读取全部
# print(data)
#
#
# print(open("file").read()) ###读取全部
#
# print(open("file").readlines())
# print(open("file").readlines())

f = open("file")

print(f.readlines())

for index,line in enumerate(f.readlines()):
    if index <3:
        print(line.split())
    else:
        break

f = open("file")
for i in range(5):
    print(f.readline().strip())

f = open("file")
for line in f:
    print(line.strip())
##默认是加了r读取模式
open("file","r")
####w为创建写覆盖模式w-write
f = open("file","w")
f.write("我爱北京天安门\n")
f.write("我爱北京天安门\n")
####模式a-apend追加
f = open("file","a")
f.write("我爱家乡\n")
f.write("我爱家乡\n")
f.close()

#r+ 读写
#w+ 写读
#a+ 追加读