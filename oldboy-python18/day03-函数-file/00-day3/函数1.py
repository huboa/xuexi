#函数的返回值
def func():
    print('from func')
    return [1,2,3],'a',1,{'a':3}
#
# res=func()
# print(res)

'''
大前提：return的返回值没有类型限制
    1. 没有return：返回None，等同于return None
    2. return 一个值：返回该值
    3. return val1,val2,val3:返回(val1,val2,val3)
'''

def my_max(x,y):
    if x > y:
        return x
    else:
        return y

my_max(1,2) #语句形式

res=my_max(1,2)*10 #表达式形式

# res1=my_max(1,2)
# res2=my_max(res1,3)

res2=my_max(my_max(1,2),3) #函数调用可以当做另外一个函数的参数
print(res2)


