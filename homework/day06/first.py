import os
import sys
import re
import time

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
 #print(compute("/",2,1))



tt="1 - 2 * ( (60-30 +(-40.5/5*6*5) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
###获取括号最里面的公式
t1=re.search(r'\([^()]+\)',tt).group()
print("##获取括号最里面的公式T1:",t1)
# print(re.search(r'[\d]+[\*|\/][\d]+',t1).group())
# print(re.search(r'\d+',t1).group())
# print(re.search(r'[-+]?[0-9]*\.?[0-9]*[\*|\/][-+]?[0-9]*\.?[0-9]*',t1).group())

def func(ff):
    try:
        ff=float(ff)
        return isinstance(ff,float)
    except ValueError:
        return False
def comp(t1):
    while True:
        print("开始循环计算\n")


        s1 = re.search(r'[-+]?[0-9]*\.?[0-9]*[\*|\/][-+]?[0-9]*\.?[0-9]*', t1).group()

        print("获取最近乘除的公式s1:", s1)
        # print(re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\*|\/])(?P<two>[-+]?[0-9]*\.?[0-9]*)',t1).groupdict())
        dic=re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\*|\/])(?P<two>[-+]?[0-9]*\.?[0-9]*)',s1).groupdict()
        print("公式的字典：",dic)
        x=dic["one"]
        y=dic["two"]

       # print("x info ",x,type(x),"y info ",y,type(y))
        m=dic["mod"]

        gg=compute(m,float(x),float(y))
        print("gg:",gg)
        t1=t1.replace(str(s1),str(gg))
    #    print("t1:",t1)
        t1 = t1.replace(str("("), str(""))
        t1 = t1.replace(str(")"), str(""))
        print("去括号的操作t1", t1)
        print("结束后判断是不是计算完成",func(t1))


        if func(t1) == True:
            return t1
        time.sleep(3)



comp(t1)



print(comp("1.22*23/23*5*666+4"))