#函数是第一类的对象：指的是函数可以被当做数据传递


def foo():
    print('from foo')
#1 被赋值
# f=foo
# print(f)
# f()

#2 可以当做参数传入
# def wrapper(func):
#     # print(func)
#     func()
# wrapper(foo)

#3 可以当做函数的返回
def wrapper(func):
    return func
# res=wrapper(foo)
# print(res)

#4 可以当做容器类型的元素

# cmd_dic={
#     'func':foo
# }
#
# print(cmd_dic)
#
# cmd_dic['func']()






def select(sql):
    '''select function'''
    print('select----->',sql)
    #sql=['select', '*', 'from', 'mysql.user;']


def insert(sql):
    '''insert function'''
    print('insert---->',sql)

def update(sql):
    '''update function'''
    print('update----->',sql)

def delete(sql):
    '''delete function'''
    print('delete---->',sql)

def alter(sql):
    print('alter===>',sql)

cmd_dic = {
    'insert': insert,
    'update': update,
    'delete': delete,
    'select': select,
    'alter':alter,
}



#select  * from mysql.user;
def main():
    while True:
        sql=input('>>: ').strip()
        if not sql:continue
        cmd_info=sql.split()
        cmd=cmd_info[0]

        if cmd in cmd_dic:
            cmd_dic[cmd](cmd_info)
        else:
            print('cmd not exists')


main()