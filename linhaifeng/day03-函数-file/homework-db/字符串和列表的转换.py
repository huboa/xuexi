
####list写入追加文件
list=["1","zsc","22","13651054608","IT","2013-04-01"]
with open("db.txt","a",encoding='utf-8') as f:
    w_line=','.join(list)
    f.write(w_line+'\n')


####文件的读取
i=0
for line in open("db.txt","r",encoding='utf-8'):
    i=i+1
    line_list= line.strip().split(',')  ###去掉字符并以,号切分
    print(line_list,type(line_list),i)
    line_str=','.join(line_list)
    print(type(line_str),line_str)


#
# theList = ['a','b','c']
# if 'a' in theList:
#     print 'a in the list'
#
# if 'd' not in theList:
#     print 'd is not in the list'
