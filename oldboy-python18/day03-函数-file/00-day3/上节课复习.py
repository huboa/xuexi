#r文本模式的读，在文件不存在，不会创建新文件
# f=open('a.txt','r',encoding='utf-8')
# # print(f.read())
# print(f.readable())
# print(f.writable())
# print(f.readline())
# print(f.readlines())
# f.close()

#w文本模式的写,文件存在则清空，不存在则创建
# f=open('a.txt','w',encoding='utf-8')
# f=open('b.txt','w',encoding='utf-8')
# print(f.writable())
# print(f.readable())
# f.write('哈哈哈哈\n')
# f.write('哈哈哈哈\n')
#
# f.writelines(['1111\n','222\n'])


#a文本模式的追加,文件存在光标跳到文件末尾，文件不存在创建
# f=open('b.txt','a',encoding='utf-8')
# # print(f.writable())
# # print(f.tell())
# f.write('3333\n')
# f.write('44444\n')


#r+,w+,a+







#rb模式即直接从硬盘中读取bytes
# f=open('a.txt','rb')
# print(f.read())


#wb模式
# f=open('a.txt','wb')
# f.write('你好啊'.encode('utf-8'))
# print(f)
# f.close()
# print(f)
# print(f.read)
# print(f.readable)
# f.read()
#ab模式



# with open('file.txt','w',encoding='utf-8') as f:
#     f.write('1111\n')


# f=open('test.jpg','rb')
# print(f.read())
#
# with open('test.jpg','rb') as read_f,open('test1.jpg','wb') as write_f:
#     # write_f.write(read_f.read())
#     for line in read_f:
#         write_f.write(line)







