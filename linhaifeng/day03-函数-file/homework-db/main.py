#
# ###第一部分 sql 解析 获取字符串
def sql_parse(sql):
    '''
    把字符串切分,提取命令信息,变成字典返回:return:
    '''

    def select_parse(sql_l):
        '''定义 语法结构,执行解析操作,返回 sql_dic'''

        select_fields = []
        from_table = []
        where_fields = []
        limit = []
        print(sql_l)
        for n in sql_l[1].split(","):
            select_fields.append(n)

        for n in sql_l[3].split(","):
            from_table.append(n)
        if sql_l[5] :
            for n in sql_l[5].split(","):
                where_fields.append(n)
        if sql_l[7]:
            for n in sql_l[7].split(","):
                limit.append(n)

        print(sql_l[1:sql_l.index("from")])




        sql_dic = {
            'func': 'select',
            'select': select_fields,  ##查询字段
            'from': from_table,  ##数据库表
            'where': where_fields,  ##filter 条件
            'limit': limit  ##limit 条件
        }
        return sql_dic

######处理接收字符串
    print("接收字符串 %s" % sql)
    sql_l = sql.split()
    print("切割后列表 sql_1 == ", sql_l)
####用功能
    parse_func = {
        # 'insert':print(insert_parse),
        # 'delete':print(delete_parse),
        # 'update':print(update_parse),
        'select': select_parse(sql_l)
    }

    func = sql_l[0]  ##获取 select insert update delet 字符
    if func in parse_func:
        return  parse_func[func]





    #
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
if __name__== '__main__':
    while True:
        sql = input("sql> ").strip()
        if sql == 'exit':
            break
        if len(sql) == 0 :
            continue

        sql_dic = sql_parse(sql)   ###获取语句
        print(sql_dic)
        # if len(sql_dic) == 0:
        #     continue
#        res=sql_activn(sql_dic)



#
# for n in open('db.txt', 'r', encoding='utf-8'):
#     dd=n.split()
#     print(dd)
#
# with open('db.txt', 'a', encoding='utf-8') as f:
#     tt=".".join(dd)
#     f.write((tt+"\n"))