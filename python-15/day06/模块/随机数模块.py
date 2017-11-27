import os
import sys
import random
import string
print(random.random())
print(random.randint(1,2))
print(random.randrange(1,2))  ##不包含最大的
print(random.sample('aabcasdfasz',5))##打印5个随机的

print(string.digits + string.ascii_letters)
str_1=string.digits + string.ascii_letters

print(random.sample(str_1,10))
print("".join(random.sample(str_1,10)))


##另一种方法
checkcode=""
for n in range(6):
    current = random.randrange(0,6)
    if current !=n:
        temp = chr(random.randint(65,90))
    else:
        temp =random.randint(0,9)
    checkcode += str(temp)
print(checkcode)