import re,time,sys

#加减函数 把所有负数 求和到sum1 sum2 为所有正数求和减
def plus_minus(res):
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
    list = re.findall('[\/]?\d+\.?\d*', res)
    list1 = re.findall('\/\d+\.?\d*', res)
    sum1 = sum2 = 1
    for n in list1:
        list.remove(n)
        n = re.search('\d+\.?\d*', n).group()
        sum1 = sum1 * float(n)
    for n in list:
        n = re.search('\d+\.?\d*', n).group()
        sum2 = sum2 * float(n)
    # print(list)
    return str(sum2/sum1)

# expression='1-2*((60+2*(-3-40.0/0.5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'

expression1='1-2*(60+2*(-3-40.0/0.5))'
expression1='1-2*(60+2*-3))'
#主函数

while True:
    if '*-' in expression1:
        print(re.sub('(\w+)( .* )(\w+)', r'\3\2\1', '60+2*-3'))

    print('express1',expression1)
    content = re.search('\(([\-\+\*\/]*\d+\.?\d*)*\)',expression1).group()
    expression_old=content
    content = content.strip('()')

    print('expression_old',expression_old)
    if '/'or '*' in content:
        content1=re.search('\d+\.?\d*[\*\/][\-]?\d+\.?\d*',content).group()

        print(content1,multiply(content1))
        content=content.replace(content1,multiply(content1))
    if '-' or '+' in content:
        content=plus_minus(content)


    # print(expression_old,type(expression_old),content,type(content),'\n')
    # expression1=expression1.replace(expression_old,content)
    time.sleep(1)



