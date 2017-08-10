import re
res='2*-3*4*5/5/-5/-4/-1'
def multiply(res):
    list = re.findall('[\-\/]?\d+\.?\d*', res)
    list1 = re.findall('\/\-?\d+\.?\d*', res)
    print(list,'list')
    print(list1, 'list1')
    sum1 = sum2 = 1
    # for n in list1:
    #     list.remove(n)
    #     n = re.search('\d+\.?\d*', n).group()
    #     sum1 = sum1 * float(n)
    # for n in list:
    #     n = re.search('\d+\.?\d*', n).group()
    #     sum2 = sum2 * float(n)
    # # print(list)
    return str(sum2/sum1)

print(multiply(res))