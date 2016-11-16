import re
import os
import sys

import re
def compute(m,x,y):
    if m == "+":
        return x + y
    elif m == "-":
        return x - y
    elif m == "*":
       return x * y
    elif m == "/" :
        return round(x/y, 2)


    else:
        print("运算符号错误")

a=compute("/",float(10),float(3))

print("a",a)

