import os
import sys
import re
import time


##元数据
tt="1 - 2 * ( (60-30 +(-40.5/5*6*5+35) * (9-2*5/3 + 7 /3*99/4*2998 +10 * 568/14 )) - (-4*3)/ (16-3*2) )"
#tt="1 - 2 * ((60-30+  -208            * 173545.881                              )  +1.2              )"
#tt="1 - 2 * ( -36097513.248                                                        +1.2              )"
#tt="1 - 2 * (-36097513.248                                                        +1.2)"
#tt=72195025.096


###判断是不是有括号
def rege1(content):
    regex = re.compile(r'\w*\(\w*|\w\)\w*')
    m = regex.search(content)
    if m:
        return True
    else:
        return False

##判断是不是有乘除符号
def rege2(content):
    regex=re.compile(r'/|\*')
    m=regex.search(content)
    if m:
        return True
    else:
        return False

##判断是不是有加减符号
def rege3(content):
 #    regex=re.compile(r'\w*\+|\-\w*')
    regex=re.compile(r'\w*\+\w*|\w\-\w*')
    m=regex.search(content)
    if m:
        return True
    else:
        return False

##计算具体两个数
def compute(m, x, y):
    if m == "+":
        return x + y
    elif m == "-":
        return x - y
    elif m == "*":
        return x * y
    elif m == "/":
        return x / y
    else:
        print("运算符号错误")

##计算简单公式
def comp(t1):
    ##去除括号,合并符号
    t1 = t1.replace(str("("), str(""))
    t1 = t1.replace(str(")"), str(""))
    t1 = t1.replace(str("+-"), str("-"))
    t1 = t1.replace(str("--"), str("+"))
    print('去除括号的公式',rege1(t1))

    ##乘除计算
    while  rege2(t1):
        print("copute开始循环计算乘除\n")

#        s1 = re.search(r'[-+]?[0-9]*\.?[0-9]*[\*|\/][-+]?[0-9]*\.?[0-9]*', t1).group()
        s1 = re.search(r'[0-9]?[0-9]*\.?[0-9]*[\*|\/][-+]?[0-9]*\.?[0-9]*', t1).group()
        print("获取最近乘除的公式s1:", s1)

        # print(re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\*|\/])(?P<two>[-+]?[0-9]*\.?[0-9]*)',t1).groupdict())
        dic=re.search(r'(?P<one>[-+]?[0-9]*\.?[0-9]*)(?P<mod>[\*|\/])(?P<two>[-+]?[0-9]*\.?[0-9]*)',s1).groupdict()
        print("公式的字典：",dic)
        x=dic["one"]
        y=dic["two"]
        m = dic["mod"]
       # print("x info ",x,type(x),"y info ",y,type(y))

        gg=compute(m,float(x),float(y))
#        print("gg:",gg)
        t1=t1.replace(str(s1),str(gg))
        print("计算完成替换的结果",t1)
        time.sleep(1)

    print('开始计算加减',t1)
    ##加减运算
    print('rege2:',rege2(t1))
    while  rege3(t1):
        print("开始循环计算加减\n",t1)

 #        s1 = re.search(r'[-+]?[0-9]*\.?[0-9]*[\+|\-][-+]?[0-9]*\.?[0-9]*', t1).group()
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
#        print("gg:",gg)
 #       print("t1:", t1)
        t1=t1.replace(str(s1),str(gg))
        print("t1:",t1)
        print("检测要不要继续计算加减",rege2(t1))
        time.sleep(1)
    return t1

###主运行函数
def maim(tt):
    tt = tt.replace(str(" "), str(""))
    while rege1(tt):
        print("######开始#####原始数据###",tt)
        ss = re.search(r'\([^()]+\)', tt).group()
        print("##获取ss:",ss)
        t1=ss
        print("##获取括号最里面的公式T1:", t1)

        t1=comp(t1)
        print("##处理过后T1:", t1)
        tt=tt.replace(str(ss),str(t1))
        print("##替换后的TT:", tt)
        print("第---------次循环")
    tt=comp(tt) ###最后一次简单运算
    tt=round(float(tt),3)
    print(tt)
    print("最后的结果",tt)
maim(tt)