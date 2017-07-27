#
# ###第一部分 sql 解析 获取字符串
# def sql_parse(sql):  ##insert delete update select
#     '''
#     把字符串切分,提取命令信息,分发给具体函数去执行
#     :return:
#     '''
#     print("接收字符串 %s" % sql)
#     parse_func={
#         'insert':print(insert_parse),
#         'delete':print(delete_parse),
#         'update':print(update_parse),
#         'select':print(select_parse),
#     }
#
#     sql_l=sql.split()
#     print("切割后列表 sql_1 == ",type(sql_l),sql_l)
#     func=sql_l[0]
#     res=''
#     if func in parse_func:
#         res=parse_func[func](sql_l)
#         print(parse_func[func](sql_l))
#     return res
#
#
#
# def insert_parse(sql_l):
#     '''定义insert 语法结构,执行解析操作,返回 sql_dic'''
#     pass
# def delete_parse(sql_l):
#     '''定义insert 语法结构,执行解析操作,返回 sql_dic'''
#     pass
# def update_parse(sql_l):
#     '''定义insert 语法结构,执行解析操作,返回 sql_dic'''
#     pass
# def select_parse(sql_l):
#     '''定义insert 语法结构,执行解析操作,返回 sql_dic'''
#     sql_dic={
#         'func':select,
#         'select':[1],##查询字段
#         'from':[2], ##数据库表
#         'where':[3], ##filter 条件
#         'limit':[4]  ##limit 条件
#     }
#     return handle_parse(sql_l,sql_dic)
#
# def handle_parse(sql_l,sql_dic):
#     return  'handle_parse'
#
#
#
# ###第二部分执行操作
# def sql_activn():
#     '''从字典sql_dic 提取命令'''
#     pass
# def insert(sql_dic):
#     pass
# def insert(sql_dic):
#     pass
# def update(sql_dic):
#     pass
# def delete(sql_dic):
#     pass
# def select():
#     pass
#
# ###主函数
# if __name__== '__main__':
#     while True:
#         sql = input("sql> ").strip()
#         if sql == 'exit':
#             break
#         if len(sql) == 0 :
#             continue
#
#         sql_dic = sql_parse(sql)
#
#         print(sql_dic)
#         if len(sql_dic) == 0:
#             continue
#         res=sql_activn(sql_dic)



with open('db.txt', 'r', encoding='utf-8') as f:
    for n in f:
        print(f.readline())
