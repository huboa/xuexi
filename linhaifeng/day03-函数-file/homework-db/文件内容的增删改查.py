

#####
#####
#####
##### 行模式的增删改查

####str写入追加文件
# line_str="1,zxx,22,13651054608,IT,2013-04-01"
# line_str.replace("13651054608","13911870720")  ##字符串的替换
# print(line_str.replace("13651054608","13911870720")) ##字符串的替换
# # with open("db.txt","a",encoding='utf-8') as f:
# #     f.write(line_str+'\n')
# #
# #
# ####文件的读取
# i=0
# with open("db.txt","r",encoding='utf-8') as f:
#     for line in f:
#         i=i+1
#         line_list= line.strip().split(',')  ###去掉字符并以,号切分
#         print(line_list,type(line_list))
#         line_str=','.join(line_list)
#         print(line_str,type(line_str))
#

####删除行
# to_delete = "1,zsc,22,13651054608,IT,2013-04-03"
# with open('db.txt', 'r+',encoding='utf-8') as f:
#     t = f.read()
#     f.seek(0)
#     for line in t.split('\n'):
#         if line != to_delete:
#              f.write(line + '\n')
#
#     f.truncate()
#
# i=0
# with open("db.txt","r",encoding='utf-8') as f:
#     for line in f:
#         i=i+1
#         line_list= line.strip().split(',')  ###去掉字符并以,号切分
#         print(line_list,type(line_list))



###文件的修改(行模式)
to_modify_old = "1,zsc,22,13600000000,IT,2013-04-04"
to_modify_new = "1,zsc,22,13600000000,IT,2013-04-05"
with open('db.txt', 'r+',encoding='utf-8') as f:
    t = f.read()
    f.seek(0)
    for line in t.split('\n'):
        if line == to_modify_old:
            line=line.replace(to_modify_old,to_modify_new)
            print(line)
        if line != '':
            f.write(line + '\n')
    f.truncate()




with open("db.txt","r",encoding='utf-8') as f:
    for line in f:
        line_list= line.strip("\n").split(',')  ###去掉字符并以,号切分
        print(line_list,type(line_list))
        line_str=','.join(line_list)
        print(line_str,type(line_str))


####
####
#####  #配置文件全文读写(小的配置文件)

# #将文件读取到内存中
# with open("file.txt","r",encoding="utf-8") as f:
#     lines = f.readlines()
#     print(lines,type(lines))
# #写的方式打开文件
# with open("file.txt","w",encoding="utf-8") as f_w:
#     for line in lines:
#         print(line.strip())
#         if "taste" in line:
#          #替换
#             line = line.replace("taste","tasting")
#         f_w.write(line)



###文件的读
# f = open('file.txt',"r",encoding="utf-8")  # 打开文件
# first_line = f.readline()
# print('first line:', first_line)  # 读一行
# print('我是分隔线'.center(50, '-'))
# data = f.read()  # 读取剩下的所有内容,文件大时不要用
# print(data)  # 打印读取内容
#
# f.close()  # 关闭文件
#
