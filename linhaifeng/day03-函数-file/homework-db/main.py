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
        if len(sql_l) > 5 and sql_l[4] == "where":      ####判断有没有where
            for n in sql_l[5].split(","):
                where_fields.append(n)


        print(sql_l[1:sql_l.index("from")])



        sql_dic = {
            'func': 'select',
            'select': select_fields,  ##查询字段
            'from': from_table,  ##数据库表
            'where': where_fields,  ##filter 条件
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

# ###第二部分执行操作
def sql_activn(sql_dic):
    action_func = {
        'select':  select(sql_dic)
      #  'insert': select(sql_dic)
    }

    func=sql_dic["func"]
    if  func in action_func:
        return action_func[func]

def select(sql_dic):
    print(sql_dic["select"])
    print(sql_dic["from"])
    field_list = sql_dic["select"]
    fields=["*","id","name","age","phone","dept","date"]
    filed_indexs=[]
    for n in field_list:
        filed_indexs.append(fields.index(n))
    return read_db(filed_indexs)

def read_db(filed_indexs):
    res=[]
    i = 0
    for line in open("db.txt", "r", encoding='utf-8'):
        i = i + 1
        line_list = line.strip().split(',')  ###去掉字符并以,号切分
        res1=[]
        for n in filed_indexs:
            res1.append(line_list[n])
        res.append(res1)
    return  res

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
        if len(sql_dic) == 0:
            continue
        res=sql_activn(sql_dic)
        print(res)



#
# for n in open('db.txt', 'r', encoding='utf-8'):
#     dd=n.split()
#     print(dd)
#
# with open('db.txt', 'a', encoding='utf-8') as f:
#     tt=".".join(dd)
#     f.write((tt+"\n"))