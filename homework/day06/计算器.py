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
       return x / y
    else:
        print("运算符号错误")

print(compute("+",int(2),int(1)))