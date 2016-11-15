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



tt="1 - 2 * ( (60-30 +(-40.5/5*6*5+35) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
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

##判断是不是有乘除符号
def rege(content):
    regex=re.compile(r'/|\*')
    m=regex.search(content)
    if m:
        return True
    else:
        return False
##判断是不是有加减符号
def rege2(content):
    regex=re.compile(r'\w*\+\w*')
    m=regex.search(content)
    if m:
        return True
    else:
        return False

##计算没有括号的加减乘除
def comp(t1):
    ##去除括号
    t1 = t1.replace(str("("), str(""))
    t1 = t1.replace(str(")"), str(""))
    print('去除括号的公式',rege(t1))

    ##乘除计算
    while  rege(t1):
        print("开始循环计算\n")

        s1 = re.search(r'[-+]?[0-9]*\.?[0-9]*[\*|\/][-+]?[0-9]*\.?[0-9]*', t1).group()

        print("获取最近乘除的公式s1:", s1)
        # print(re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\*|\/])(?P<two>[-+]?[0-9]*\.?[0-9]*)',t1).groupdict())
        dic=re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\*|\/])(?P<two>[-+]?[0-9]*\.?[0-9]*)',s1).groupdict()
        print("公式的字典：",dic)
        x=dic["one"]
        y=dic["two"]
        m = dic["mod"]
       # print("x info ",x,type(x),"y info ",y,type(y))

        gg=compute(m,float(x),float(y))
        print("gg:",gg)
        t1=t1.replace(str(s1),str(gg))
    #    print("t1:",t1)

 #       print("结束后判断是不是计算完成",func(t1))

        time.sleep(3)

    print('开始计算加减',t1)
    ##加减运算
    print('rege2:',rege2(t1))
    while  rege2(t1):
        print("开始循环计算加减\n",t1)

        s1 = re.search(r'[-+]?[0-9]*\.?[0-9]*[\+|\-][-+]?[0-9]*\.?[0-9]*', t1).group()

        print("获取最前面加减的公式:", s1)
        # print(re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\*|\/])(?P<two>[-+]?[0-9]*\.?[0-9]*)',t1).groupdict())
        dic=re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\+|\-])(?P<two>[-+]?[0-9]*\.?[0-9]*)',s1).groupdict()
        print("公式的字典：",dic)
        x=dic["one"]
        y=dic["two"]
        m=dic["mod"]
        print("x info ",x,type(x),"y info",y,type(y))

        gg=compute(m,float(x),float(y))
        print("gg:",gg)
        print("t1:", t1)
        t1=t1.replace(str(s1),str(gg))
        print("t1:",t1)
        print("检测要不要继续计算加减",rege2(t1))
        time.sleep(3)
    return t1


print(comp(t1))