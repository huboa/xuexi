import math
# ###递归函数
def fact(n):
    if n==1:
        return 1
    return n * fact(n - 1)

print(fact(7))
##大多数编程语言没有针对尾递归做优化，Python解释器也没有做优化
def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)
print(fact(5))
###汉诺塔游戏
# -*- coding: utf-8 -*-
# 汉诺塔
B=[]
def move_hanoi(n,a='A',b='B',c='C'):
    if n==1:
        print(a,'-->',c)
        B.append(a+'-->'+c)
    else:
        move_hanoi(n-1,a,c,b) #将前n-1个盘子从A移动到B上
        move_hanoi(1,a,b,c) #将最底下的最后一个盘子从A移动到C上
        move_hanoi(n-1,b,a,c) #将B上的n-1个盘子移动到C上
n=int(input('请输入汉诺塔的层数：'))
move_hanoi(n,'A','B','C')
print('总共需要操作'+str(len(B))+'次,\n'+'操作过程为:',B)

if n==1:
    print(a,'-->',c)
    return
move(n-1,a,c,b) # 将A最上面的n -1个盘子移动到B
move(1,a,b,c)#将A上最后一个盘子移动到C
move(n-1,b,a,c) # 将B上面的n-1个盘子移动到C