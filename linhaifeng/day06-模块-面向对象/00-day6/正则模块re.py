import re
# print(re.findall('\w','hello_ | egon 123'))
# print(re.findall('\W','hello_ | egon 123'))
# print(re.findall('\s','hello_ | egon 123 \n \t'))
# print(re.findall('\S','hello_ | egon 123 \n \t'))
# print(re.findall('\d','hello_ | egon 123 \n \t'))
# print(re.findall('\D','hello_ | egon 123 \n \t'))
# print(re.findall('h','hello_ | hello h egon 123 \n \t'))
# # print(re.findall('\Ahe','hello_ | hello h egon 123 \n \t'))
# print(re.findall('^he','hello_ | hello h egon 123 \n \t'))
# # print(re.findall('123\Z','hello_ | hello h egon 123 \n \t123'))
# print(re.findall('123$','hello_ | hello h egon 123 \n \t123'))
# print(re.findall('\n','hello_ | hello h egon 123 \n \t123'))
# print(re.findall('\t','hello_ | hello h egon 123 \n \t123'))



#. [] [^]

#.本身代表任意一个字符
# print(re.findall('a.c','a a1c a*c a2c abc a c aaaaaac aacc'))
                    #a.c
# print(re.findall('a.c','a a1c a*c a2c abc a\nc',re.DOTALL))
# print(re.findall('a.c','a a1c a*c a2c abc a\nc',re.S))

#[]内部可以有多个字符，但是本身只配多个字符中的一个
# print(re.findall('a[0-9][0-9]c','a a12c a1c a*c a2c a c a\nc',re.S))
# print(re.findall('a[a-zA-Z]c','aac abc aAc a12c a1c a*c a2c a c a\nc',re.S))
# print(re.findall('a[^a-zA-Z]c','aac abc aAc a12c a1c a*c a2c a c a\nc',re.S))
# print(re.findall('a[\+\/\*\-]c','a-c a+c a/c aac abc aAc a12c a1c a*c a2c a c a\nc',re.S))

#\:转义
# print(re.findall(r'a\\c','a\c abc')) #rawstring


#? * + {}：左边有几个字符，如果有的话，贪婪匹配
#?左边那一个字符有0个或者1个
# print(re.findall('ab?','aab a ab aaaa'))
                       #ab?

#*左边那一个字符有0个或者无穷个
# print(re.findall('ab*','a ab abb abbb abbbb bbbbbb'))
# print(re.findall('ab{0,}','a ab abb abbb abbbb bbbbbb'))

#+左边那一个字符有1个或者无穷个
# print(re.findall('ab+','a ab abb abbb abbbb bbbbbb'))
# print(re.findall('ab{1,}','a ab abb abbb abbbb bbbbbb'))

#{n,m}左边的字符有n-m次
# print(re.findall('ab{3}','a ab abb abbb abbbb bbbbbb'))
# print(re.findall('ab{2,3}','a ab abb abbb abbbb bbbbbb'))

# .* .*?
#.*贪婪匹配
# print(re.findall('a.*c','a123c456c'))
#.*?非贪婪匹配
# print(re.findall('a.*?c','a123c456c'))

#|
# print(re.findall('company|companies','Too many companies have gone bankrupt, and the next one is my company'))
                                            #                                                       company|companies

# print(re.findall('compan|companies','Too many companies have gone bankrupt, and the next one is my company'))

#():分组
# print(re.findall('ab+','abababab123'))
# print(re.findall('ab+123','abababab123'))

# print(re.findall('ab','abababab123'))
# print(re.findall('(ab)','abababab123'))
# print(re.findall('(a)b','abababab123'))
# print(re.findall('a(b)','abababab123'))
# print(re.findall('(ab)+','abababab123'))
# print(re.findall('(?:ab)+','abababab123'))


# print(re.findall('(ab)+123','abababab123'))
# print(re.findall('(?:ab)+123','abababab123'))
# print(re.findall('(ab)+(123)','abababab123'))


# print(re.findall('compan(y|ies)','Too many companies have gone bankrupt, and the next one is my company'))
# print(re.findall('compan(?:y|ies)','Too many companies have gone bankrupt, and the next one is my company'))


#re的其他方法
# print(re.findall('ab','abababab123'))
# print(re.search('ab','abababab123').group())
# print(re.search('ab','12aasssdddssssssss3'))
# print(re.search('ab','12aasssdddsssssssab3sssssss').group())


# print(re.search('ab','123ab456'))
#
# print(re.match('ab','123ab456')) #print(re.search('^ab','123ab456'))
#

#
# print(re.split('b','abcde'))
# print(re.split('[ab]','abcde'))

# print(re.sub('alex','SB','alex make love alex alex',1))
# print(re.subn('alex','SB','alex make love alex alex',1))


# print(re.sub('(\w+)(\W+)(\w+)(\W+)(\w+)',r'\5\2\3\4\1','alex make love'))

# print(re.sub('(\w+)( .* )(\w+)',r'\3\2\1','alex make love'))



#
# obj=re.compile('\d{2}')
#
# print(obj.search('abc123eeee').group()) #12
# print(obj.findall('abc123eeee')) #12



print(re.findall('\-?\d+\.?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))
print(re.findall('\-?\d+\.?\d*',"1-12*(60+(-40.35/5)-(-4*0.3))"))


# print(re.findall('\-?\d+\.\d+',"1-12*(60+(-40.35/5)-(-4*3))"))
# print(re.findall('\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))


# print(re.findall('\-?\d+\.\d+|(\-?\d+)',"1-12*(60+(-40.35/5)-(-4*3))"))
# print(re.findall('\-?\d+\.\d+|\-?\d+',"1-12*(60+(-40.35/5)-(-4*3))"))
# print(re.findall('\-?\d+|\-?\d+\.\d+',"1-12*(60+(-40.35/5)-(-4*3))"))









