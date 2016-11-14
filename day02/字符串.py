msg = "Hello world"
# print(msg[4])
# print(msg.capitalize())
# print(msg.center(20,'*'))
# print(msg.count('d',0,-1))
# print(msg.endswith('5'))
# print(msg[6])
# print(msg.expandtabs(9))
# print(msg.find('o'))
# print('{},{},{}'.format('name','age','other'))
# print('{0},{1},{0}'.format('name','age','other'))
# print('{name}'.format(name='zsc'))

# ##字符的格式
# msg3="Hello"
# print(msg.index('e'))  ###索引位置
# print(msg.isalnum())    ###字母或数字
# print(msg.isalpha())    ##纯字母
# print(msg.isdecimal())  ##10进制字符
# print(msg.isdigit())    ##整形字符
# print(msg.isidentifier()) ##是否有关键字
# print(msg.islower())    ##是否是纯小写
# print(msg.isupper())    ##是否纯大写
# print(msg.isspace())    ##是否为空格（tab,换行）
# print(msg.istitle())    ##是否只有首字母大写
#
# ##位置的编辑
# print(msg.ljust(20),'*')  ###左对齐
# print(msg.rjust(20),'*')  ###右对齐
# print(msg.center(20),'*') ###中间对齐
# print(msg.lower())        ##更改全大写
# print(msg.upper())        ##更改全小写
#
# ##
# print(msg.find('w'))
# print(msg.index('w'))

# ##
# msg='    dfasdf   '
# print(msg.strip())
# print(msg.lstrip())
# print(msg.rsplit())
#
# ##
# msg='my name is abcd'
# table=str.maketrans('a','1')
# print(msg.translate(table))
#
# ##填充
#
# msg = 'abc'
# print(msg.zfill(20))
# print(msg.ljust(20,'*'))
# print(msg.rjust(20,'0'))

#留出空白
msg='  mysql oo '
print(msg.strip())

##分割
msg="keep moving"
print(msg[1])
print(msg[6:8])   ##要头不要尾
print(msg[:])
print(msg[0:])
print(msg[0:3])
print(msg[2:7:2])  ##头尾，步长

###运算符：


