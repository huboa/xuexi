#_*_coding: utf-8_*_

### 解析语句
def sql_parse(sql):
    parse_func={
        'insert':insert_parse,
        'select':select_parse,
        'delete':delete_parse,
        'update':update_parse,
    }

    sql_l=sql.split(' ')
    func=sql_l[0]
    if func in parse_func:
        res=parse_func[func](sql_l)

    print("sql str is %s" %sql)
    return res
def insert_parse(sql_l):
    pass
def delete_parse(sql_l):
    pass
def update_parse(sql_l):
    pass
def select_parse(sql_l):
    '''
      定义select语句的语法结构，执行sql解析操作，返回sql_dic
      :param sql:
      :return:
      '''''
    print('from in the select_parse \033[42;1m%s\033[0m' % sql_l)
    sql_dic = {
        'func': select,
        'select': [],  # 查询字段
        'from': [],  # 数据.表
        'where': [],  # filter条件
        'limit': [],  # limit条件
    }
    return handle_parse(sql_l,sql_dic)
def handle_parse(sql_l,sql_dic):
    print('handle_parse is \033[43;1m%s\033[0m' %sql_dic)


###执行语句

#第一部分：sql执行
def sql_action(sql_dic):
    '''
    从字典sql_dic提取命令，分发给具体的命令执行函数去执行
    :param sql_dic:
    :return:
    '''''
    return sql_dic.get('func')(sql_dic)

def insert(sql_dic):
    pass

def delete(sql_dic):
    pass

def update(sql_dic):
    pass

def select(sql_dic):
    print('from select sql_dic is %s' %sql_dic)
    # #first：from
    # db,table=sql_dic.get('from')[0].split('.')
    #
    # fh=open("%s/%s" %(db,table),'r',encoding='utf-8')
    # #second:where
    # filter_res=where_action(fh,sql_dic.get('where'))
    # # for record in filter_res:
    # #     print('filter res is %s' %record)
    # #third:limit
    # limit_res=limit_action(filter_res,sql_dic.get('limit'))
    # # for record in limit_res:
    # #     print('limit res is %s' %record)
    # #lase:select
    # search_res=search_action(limit_res,sql_dic.get('select'))
    # # for record in search_res[-1]:
    # #     print('limit res is %s' %record)

    # return search_res


if __name__ == "__main__":
    while True:
        sql=input("sql>").strip()
        if sql == "exit":break
        if len(sql) == 0 :continue
        sql_parse(sql)
        # if len(sql_dic) ==0:continue
        # res=sql_action(sql_dic)
