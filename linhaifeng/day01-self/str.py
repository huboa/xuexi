# #strip
# name='*egon**'
# print(name.strip('*'))
# print(name.lstrip('*'))
# print(name.rstrip('*'))
#
# #startswith,endswith
# name='alex_SB'
# print(name.endswith('SB'))
# print(name.startswith('alex'))
#
# #replace
# name='alex say :i have one tesla,my name is alex'
# print(name.replace('alex','SB',1))
#
# #format的三种玩法
# res='{} {} {}'.format('egon',18,'male')
# print(res,type(res))
# res='{1} {0} {1}'.format('egon',18,'male')
# print(res,type(res))
# res='{name} {age} {sex}'.format(sex='male',name='egon',age=18)
# print(res)
# #
# #find,rfind,index,rindex,count
# name='egon say hello'
# print(name.find('o',1,3)) #顾头不顾尾,找不到则返回-1不会报错,找到了则显示索引
# # print(name.index('e',2,4)) #同上,但是找不到会报错
# print(name.count('o',1,10)) #顾头不顾尾,如果不指定范围则查找所有

#
# #split
# name='root:x:0:0::/root:/bin/bash'
# print(name.split(':')) #默认分隔符为空格
# name='C:/a/b/c/d.txt' #只想拿到顶级目录
# print(name.split('/',1))
#
# name='a|b|c'
# print(name.rsplit('|',1)) #从右开始切分
#
# #
# #join
# tag=' '
# print(tag.join(['egon','say','hello','world'])) #可迭代对象必须都是字符串
#
# #center,ljust,rjust,zfill
# name='egon'
# print(name.center(30,'-'))
# print(name.ljust(30,'*'))
# print(name.rjust(30,'*'))
# print(name.zfill(50)) #用0填充
#
#
#expandtabs
# name='egon\thello'
# print(name)
# print(name.expandtabs(4))

# #lower,upper
name='egon'
print(name.lower())
print(name.upper())

#
# #captalize,swapcase,title
print(name.capitalize()) #首字母大写
print(name.swapcase()) #大小写翻转
msg='egon say hi'
print(msg.title()) #每个单词的首字母大写
#
# #is数字系列
#在python3中
num1=b'4' #bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3='四' #中文数字
num4='Ⅳ' #罗马数字

#isdigt:bytes,unicode
print(num1.isdigit()) #True
print(num2.isdigit()) #True
print(num3.isdigit()) #False
print(num4.isdigit()) #False

#
#isdecimal:uncicode
#bytes类型无isdecimal方法
print(num2.isdecimal()) #True
print(num3.isdecimal()) #False
print(num4.isdecimal()) #False

#isnumberic:unicode,中文数字,罗马数字
#bytes类型无isnumberic方法
print(num2.isnumeric()) #True
print(num3.isnumeric()) #True
print(num4.isnumeric()) #True

#
# #三者不能判断浮点数
num5='4.3'
print(num5.isdigit())
print(num5.isdecimal())
print(num5.isnumeric())
# '''
# 总结:
#     最常用的是isdigit,可以判断bytes和unicode类型,这也是最常见的数字应用场景
#     如果要判断中文数字或罗马数字,则需要用到isnumeric
# '''
#
# #is其他
print('===>')
name='egon123'
print(name.isalnum()) #字符串由字母和数字组成
print(name.isalpha()) #字符串只由字母组成

print(name.isidentifier())
print(name.islower())
print(name.isupper())
print(name.isspace())
print(name.istitle())