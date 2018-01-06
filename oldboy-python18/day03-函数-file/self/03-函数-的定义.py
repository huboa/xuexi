'''
**********************
hello ZSC
**********************
'''

# def print_star():
#     print('*'*2)
#
# def print_msg():
#     print('hello egon')
#
#
# print_star()
# print_star()
# print_msg()
# print_star()
# print_star()


'''
函数的使用：
	1 先定义
	2 再调用
'''

#函数的定义与变量的定义类似，没有事先定义变量，而直接引用变量，会报错
#没有事先定义函数，而直接调用，就相当于在引用一个不存在的变量名



# #定义阶段
# def foo():
#     print('from foo')
#     bar()
# # print(foo)
# def bar():
#     print('from bar')


# #调用阶段
# foo()


#函数在定义阶段发生了什么事情？？？
#只检测语法，不执行代码
# def func():
#     asdf #asdf=111111
#
#
# func()



#函数的定义语法
'''
def 函数名(arg1,arg2,arg3):
    "注释"
    函数体
    return 返回值

函数名一般是动词
参数、、、
return:函数内部可以有多个return，但只能执行一次，函数就结束调用，
        并且会把return后的值作为函数执行的结果返回
'''


#定义的三种形式
'''
无参：应用场景仅仅只是执行一些操作，比如与用户交互，打印
有参：需要根据外部传进来的参数，才能执行相应的逻辑，比如统计长度，求最大值最小值
空函数：设计代码结构

'''

# def my_max(x,y):
#     if x > y:
#         # print(x)
#         return x
#     else:
#         # print(y)
#         return y
#
# res=my_max(1,2)
# print(res)
#
# res=max(1,2)
# print(res)

# def foo():
#     print('-=----')
#     return 123
#     print('-=----')
#     print('-=----')
#     print('-=----')
# foo()



def select(sql):
    '''select function'''
    print(sql)
    #sql=['select', '*', 'from', 'mysql.user;']


def insert(sql):
    '''insert function'''
    pass

def update(sql):
    '''update function'''
    pass

def delete(sql):
    '''delete function'''
    pass


#select  * from mysql.user;
def main():
    while True:
        sql=input('>>: ').strip()
        if not sql:continue
        cmd_info=sql.split()
        cmd=cmd_info[0]

        if cmd == 'select':
            select(cmd_info)


main()



