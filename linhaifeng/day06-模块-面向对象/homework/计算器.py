import re

#加减函数
def plus_add(res):
    print(res, type(res))
    list=re.findall('[\-\+]?\d+\.?\d*',res)
    list1=re.findall('\-\d+\.?\d*',res)

    list2=re.findall('\+?\d+\.?\d*',res)
    print(list)
    print(list1)
    print(list2)
    # for n in list1:
    #     n=float(n)
    #     print(n)
    # return res

#乘除函数
def times_divide(res):
    print(res,type(res))
    if '/' in res:
        res=res.split('/')
        res=float(res[0])/float(res[1])
    else:
        res=float(res[0])*float(res[1])


    return str(res)



expression='1-2*((60+2*(-3-40.0/0.5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
#主函数
def main1():
    # content = re.search('\(([\-\+\*\/]*\d+\.?\d*)*\)', expression).group()
#    content = re.search('\(([\-\+\*\/]*\d+\.?\d*)+\)', expression).group()
#     print(content)
#    pp=re.search('(\d+\.?\d*[\*\/]\-?\d+\.?\d*)',content).group()
    pp = "-2.5-3+3"
    # print(times_divide(pp))
    print(plus_add(pp))
main1()

