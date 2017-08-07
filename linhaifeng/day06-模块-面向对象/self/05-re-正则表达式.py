import re
# print(re.findall('\w','hello_ | zsc 123'))
# print(re.findall('\W','hello_ | zsc 123'))
# print(re.findall('\s','hello_ | zsc 123 \n \t'))
# print(re.findall('\S','hello_ | zsc 123 \n \t'))
# print(re.findall('\d','hello_ | zsc 123 \n \t'))
# print(re.findall('\D','hello_ | zsc 123 \n \t'))
# print(re.findall('h','hello_ | hello_ h zsc 123 \n \t'))
# print(re.findall('\Ah','hello_ | hello_ h zsc 123 \n \t123'))
# print(re.findall('123\Z','hello_ | hello_ h zsc 123 \n \t123'))
# print(re.findall('^he','hello_ | hello_ h zsc 123 \n \t123'))
# print(re.findall('123$','hello_ | hello_ h zsc 123 \n \t123'))

## . 与 [] [^]
# #. 本身就代表一个字符
# print(re.findall('a.c','a a1c a*c a2c abc a c aaaac'))
# print(re.findall('a.c','a a1c a*c a2c a\nc'))
# print(re.findall('a.c','a a1c a*c a2c a\nc',re.DOTALL))
# print(re.findall('a.c','a a1c a*c a2c a\nc',re.S))
# ##[]内部可以有多个字符，但本身只配多个字符中的一个
# print(re.findall('a[123\n]c','a a1c a*c a2c a\nc',re.S))
# print(re.findall('a[123\n][123]c','a a1c a*c a22c a\nc',re.S))
# print(re.findall('a[a-z]c','a a1c a*c a22c aac a\nc',re.S))
# print(re.findall('a[A-z]c','a a1c a*c a22c aac a\nc a/c a+c ',re.S))
# print(re.findall('a[+/*-]c','a a1c a*c a22c aac a\nc a/c a+c ',re.S))
# print(re.findall('a[^A-z]c','a a1c a*c a22c aac a\nc a/c a+c ',re.S))
#

#\:转义
# print(re.findall(r'a\\c','a\c abc')) #rastring
#
# #? * + {}：左边有几个字符有的话贪婪匹配
# #?左边那一个字符有0个或一个
# #* 左边字符有0个或着无穷个
# print(re.findall('ab?','a ab abb abbb abbbb bbbbb aaa'))
# print(re.findall('ab*','a ab abb abbb abbbb bbbbb aaa'))
# print(re.findall('ab?','a ab abb abbb abbbb bbbbb aaa'))
# print(re.findall('ab+','a ab abb abbb abbbb bbbbb aaa'))
# #{n，m} 左边的字符有n-m 次
# print(re.findall('ab{3}','a ab abb abbb abbbb bbbbb aaa'))
# print(re.findall('ab{2,3}','a ab abb abbb abbbb bbbbb aaa'))
# print(re.findall('ab{1,}','a ab abb abbb abbbb bbbbb aaa'))
# print(re.findall('ab{,}','a ab abb abbb abbbb bbbbb aaa'))
# #.* .*? #贪婪匹配
# #.*
# print(re.findall('a.*c','acadad7asd8adc'))
# #.*?
# print(re.findall('a.*?c','acadacd7asd8adc'))
#

#|

print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company'))
#():分组
print(re.findall('(ab)','abababaabaab123'))
print(re.findall('(ab)+','abababaabaab123'))
print(re.findall('ab+123','abababaabaab123'))
print(re.findall('(ab)+123','abababaabaab123'))


###re的其他方法
print(re.findall('ab','abababaabaab123'))
print(re.search('ab','abababaabaab123'))
print(re.search('ab','abababaabaab123').group())
print(re.search('abad','abababaabaab123'))
print(re.match('ab','123ab456'))
print(re.search('ab','123ab456').group())
print(re.split('b','abcde'))
print(re.split('[ab]','abcde'))
print(re.sub('alex','SB','alex make love for alex',1))
print(re.subn('alex','SB','alex make love for alex'))


print(re.sub('(\w+)(\W+)(\w+)(\W+)(\w+)',r'\3\2\1',"a fu b"))