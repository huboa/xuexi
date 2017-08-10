import re,time,sys

#加减函数 把所有负数 求和到sum1 sum2 为所有正数求和减
def plus_minus(res):
    res=res.replace('--','+')
    res=res.replace('+-','-')
    list=re.findall('[\-\+]?\d+\.?\d*',res)
    list1=re.findall('\-\d+\.?\d*',res)
    sum1=sum2=0
    for n in list1:
        list.remove(n)
        n=re.search('\d+\.?\d*',n).group()
        sum1=sum1+float(n)
    for n in list:
        n = re.search('\d+\.?\d*', n).group()
        sum2 = sum2 + float(n)
    return str(sum2-sum1)   ###返回加减后的值

#乘除函数
def multiply(res):
    list = re.findall('\/?\-?\d+\.?\d*', res)
    list1 = re.findall('\/\-?\d+\.?\d*', res)
    sum1 = sum2 = 1
    for n in list1:
        list.remove(n)
        n = re.search('\-?\d+\.?\d*', n).group()
        sum1 = sum1 * float(n)
    for n in list:
        n = re.search('\-?\d+\.?\d*', n).group()
        sum2 = sum2 * float(n)
    # print(list)
    return str(sum2/sum1)

# expression='1-2*((60+2*(-3-40.0/0.5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

expression1='1-2*(60+2*(-3-40.0/0.5))'
expression1='1-2*(60+2*-3)'
#主函数

while True:

    print('express1',expression1)
    if '(' or ')' in expression1:
        content = re.search('\(([\-\+\*\/]*\d+\.?\d*)*\)',expression1).group()
        expression_old = content
        content = content.strip('()')
    else:
        content=expression1


    # print(('expression_old %s content %s') % (expression_old, content))


    if '/'or '*' in content:

        content1=re.search('\d+\.?\d*[\*\/][\-]?\d+\.?\d*',content).group()
        print('//////////////',content1)
        content=content.replace(content1,multiply(content1))
    if '-' or '+' in content:
        content=plus_minus(content)


    print(content,'replace',expression_old)
    expression1=expression1.replace(expression_old,content)
    print(expression1,'=====')
    time.sleep(1)



