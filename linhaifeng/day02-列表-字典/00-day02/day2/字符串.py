# name='egon' #name=str('egon')
# name=str('egon')
# print(type(name))
# print(name)

#优先掌握
#索引
# name='egon' #name=str('egon')
# print(name[0])
# print(name[1000])


#移除空白
# name=input('username: ')
# # print(name)
#
# name=name.strip()
# print(name)


# name=input('username: ').strip()
# print(name)


# name=input('username: ')
# print(name.strip())


# name='***egon********'
# # print(name.strip('*'))
#
# print(name.lstrip('*'))
# print(name.rstrip('*'))


#切分
# user_info='root:x:0:0::/root:/bin/bash'
# print(user_info.split(':')[5])

# cmd_info='get|a.txt|333333333'
# # print(cmd_info.split('|')[0])
# print(cmd_info.split('|',1)[0])

# msg='name         egon age 18'
# print(msg.split())


#取长度
# name='egon'
# # print(name.__len__())
# print(len(name)) #name.__len__()


#切出子字符串
# name='hello world'
# # print(name[1])
# # print(name[2])
# # print(name[3])
# print(name[1:7:2])



#字符的其他方法（掌握）
# name='alex_SB'
# print(name.endswith('SB'))
# print(name.startswith('alex'))

# name='alex say :i have one tesla,my name is alex'
# print(name.replace('alex','SB',1))


# print('{} {} {}'.format('egon',18,'male'))
# print('{0} {1} {0}'.format('egon',18,'male'))
# print('NAME:{name} AGE:{age} SEX:{sex}'.format(age=18,sex='male',name='egon'))

# num='123'
# print(num.isdigit())

# oldboy_age=73
# while True:
#     age=input('>>: ').strip()
#     if len(age) == 0:continue
#     if age.isdigit():
#         age=int(age)
#         print(age,type(age))






#字符其他需要了解的方法

name='egon hello'
# print(name.find('o'))
# print(name.find('x'))
# print(name.find('o',3,6))

# print(name.index('o'))
# print(name.index('x'))


# print(name.count('o',1,3))
#
# l=['egon','say','hello','world'] #类别内容必须都是字符串
# print(':'.join(l))

# name='egon'
# print(name.center(30,'*'))
# print(name.ljust(30,'*'))
# print(name.rjust(30,'*'))
# print(name.zfill(30))



# name='egon\thello'
# print(name)
# print(name.expandtabs(1))

# name='EGON'
# print(name.lower())
#
# name='eg'
# print(name.upper())


# name='egon say'
#
# print(name.capitalize()) #首字母大写
# print(name.swapcase()) #大小写翻转
# msg='egon say hi'
# print(msg.title()) #每个单词的首字母大写

# name='egon123'
# print(name.isalnum()) #字符串由字母和数字组成
# name='egon'
# print(name.isalpha()) #字符串只由字母组成



num1=b'4' #Bytes
num2=u'4' #unicode,python3中无需加u就是unicode
num3='四' #中文数字
num4='Ⅳ' #罗马数字

#bytes,unicode
# print(num1.isdigit())
# print(num2.isdigit())
# print(num3.isdigit())
# print(num4.isdigit())


#isdecimal:unicode
# print(num2.isdecimal())
# print(num3.isdecimal())
# print(num4.isdecimal())


#isnumberic:unicode,汉字，罗马
# print(num2.isnumeric())
# print(num3.isnumeric())
# print(num4.isnumeric())
