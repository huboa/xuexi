import re

#加减函数
def plus_add():
    pass

#乘除函数
def times_divide():
    pass



expression='1-2*((60+2*(-3-40.0/0.5)*(9-2*5/3+7/3*99/4*2998+10*568/14))-(-4*3)/(16-3*2))'
#主函数
def main1():
    content = re.search('\(([\-\+\*\/]*\d+\.?\d*)*\)', expression).group()
#    content = re.search('\(([\-\+\*\/]*\d+\.?\d*)+\)', expression).group()
    print(content)
    pp=re.search('(\-?\d+\.?\d*[\*\/]\-?\d+\.?\d*)',content).group()
    print(pp)

main1()

###[+-]
