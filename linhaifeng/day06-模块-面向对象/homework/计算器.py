import re

#加减函数 把所有负数 求和到sum1 sum2 为所有正数求和减
def plus_add(res):
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
def times_divide(res):
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

expression='1-2*((60+2*(-3-40.0/0.5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
#主函数
def main1():
    while True:
        content = re.search('\(([\-\+\*\/]*\d+\.?\d*)*\)', expression).group()
        expression_old=content
        content = re.search('[^\(\)]',content)

        print(content)
        if '/'or '*' in content:
            content1=re.search('\d+\.?\d*[\*\/]\d+\.?\d*',content).group()
            content2=times_divide(content1)
            print(content,content1,content2)
            content=content.replace(content1,content2)
        if '-' or '+' in content:
            print(content)
            print(content1,'conten1++++++')
            content2=plus_add(content1)
            content=content.replace(content1,content2)
            print(content, content1, content2)
            print(expression)
        # expression = expression.replace(expression,content)

main1()

