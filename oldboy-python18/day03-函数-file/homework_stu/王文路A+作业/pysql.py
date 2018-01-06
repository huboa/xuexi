# -*- coding:utf-8 -*-
import os
import time
from prettytable import PrettyTable

def pysql_keyword():
    '''
        定义解释器关键字
        :return: 返回字典格式的关键字结果
    '''
    return {
        'insert':[],
        'delete':[],
        'update':[],
        'select':[],
        'into':[],
        'from':[],
        'where':[],
        'limit':[],
        'values':[],
        'set':[]
    }
def my_function():
    '''
        定义解释器关键字
        :param sql_l: sql按照空格分割的列表
        :param sql_dic: 待填充的字典
        :return: 返回字典格式的自定义内置函数地址
    '''
    return {'insert':insert,'delete':delete,'update':update,'select':select}
def cmd_input():
    '''
        接收输入的PySQL语句
        :return: 返回字符串格式的输入语句
    '''
    return input('pysql>').strip().rstrip(';')
def sql_to_list(sql):
    '''
        sql字符串转换成列表
        :param sql: 输入的sql语句
        :return: 返回列表格式的sql解析结果
    '''
    l = sql.split(' ')
    l = [i for i in l if i != '']
    return l
def operator_parse(opera):
    '''
        where条件中运算符格式化
        :param opera: where条件
        :return: 返回列表格式的where解析结果
    '''
    # select age,name,dept from user where id > 2 and id < 10 or name like lucy not id = 3;
    operator = [ '>=', '<=','>', '=', '<'] #
    com_list = []
    for l in opera:
        if type(l) is list:
            char = ''.join(l)
            if 'like' in char:
                com_list.append(l)
            x = 0
            for i in operator:
                if x > 0:continue
                tem_list = [x.strip() for x in char.split(i)]
                if len(tem_list) > 1:
                    x += 1
                    tem_list.insert(1,i)
                    com_list.append(tem_list)
        else:
            com_list.append(l)
    return com_list
def where_parse(where_list):
    '''
        where条件的逻辑运算符格式化
        :param where_list: where条件的列表
        :return: 返回列表格式的where解析结果
    '''
    logic = ['and','or','not']
    where = []
    l = []
    for element in where_list:

        if element in logic:
            if len(l) > 0:
                where.append(l)
                l = []
            where.append(element)
        else:
            l.append(element)
    if len(l) > 0:
        where.append(l)
    return operator_parse(where)
def set_parse(set_list):
    '''
        set关键字的条件解析
        :param set_list: set列表
        :return: 返回列表格式的set解析结果
    '''
    set = []
    for i in set_list[0].split(','):
        l = i.split('=')
        l.insert(1,'=')
        set.append(l)
    return set
def sql_parse(sql_list):
    '''
        sql解析
        :param sql_list: 按照空格分割的sql列表
        :return: 返回字典格式的sql解析结果
    '''
    kewords = pysql_keyword()
    new_keword = {}
    current_key = []
    for key,chars in enumerate(sql_list):
        if chars in kewords:
            current_key.append(chars)
            new_keword[chars] = []
        else:
            new_keword[current_key[-1]].append(chars)
    if new_keword.get('where'):
        new_keword['where'] = where_parse(new_keword['where'])
    return new_keword
def file_exists(filename):
    '''
        判断打开的文件是否存在
        :param filename: .分割的文件路径
        :return: 布尔值
    '''
    if '.' in filename:
        database,tablename = filename.split('.')
    else:
        return False
    try:
        with open('%s/%s' % (database,tablename)):
            return True
    except IOError:
        return False
def open_title(filename):
    '''
        打开表字段所在文件
        :param filename: .分割的文件路径
        :return: 返回文件信息
    '''
    database, tablename = filename.split('.')
    return open('%s/%s.frm' % (database, tablename))
def open_data(filename):
    '''
        打开数据所在文件
        :param filename: .分割的文件路径
        :return: 返回文件信息
    '''
    database, tablename = filename.split('.')
    return open('%s/%s' % (database, tablename),'r',encoding='utf-8')
def write_add(filename,line):
    '''
        文件追加操作
        :param filename: .分割的文件路径
        :param line: 追加的内容
    '''
    database, tablename = filename.split('.')
    with open('%s/%s' % (database, tablename),'a',encoding='utf-8') as f:
        f.write('%s\n'%line)
def write_file(filename,line):
    '''
        文件写入操作
        :param filename: .分割的文件路径
        :param line: 写入的内容
    '''
    database, tablename = filename.split('.')
    with open('%s/%s_new' % (database, tablename),'w',encoding='utf8') as w:
        w.write(line)
    os.remove('%s/%s' % (database, tablename))
    os.rename('%s/%s_new' % (database, tablename),'%s/%s' % (database, tablename))
def input_error():
    '''
        打印错误信息
    '''
    print('ERROR: You have an error in your SQL syntax;')
def increment_id(lines):
    '''
        获取最后一个id
        :param lines: 文件列表
        :return: 返回整型id
    '''
    if len(lines) == 0:
        last_id = 0
    else:
        last_id = int(lines[-1].split(',')[0])
    return last_id
def insert(sql_dic):
    '''
        增加操作
        :param sql_dic: 解析完的sql字典
    '''
    if sql_dic.get('into'):
        path = sql_dic['into'][0]
        if file_exists(path):
            title = open_title(path).readline()
            data = open_data(path).readlines()
            if len(sql_dic['into']) == 1: # insert into data.user values (nobody,35,18888888888,C++,2017-07-19);
                # 判断插入的值是否存在
                if sql_dic.get('values'):
                    title_list = title.split(',')
                    tag = []
                    for line in data:
                        dic = dict(zip(title_list,line.split(',')))
                        if dic['phone'] in sql_dic.get('values')[0]:
                            tag.append(dic['phone'])
                    if len(tag) == 0:
                        insert_datas = [i.strip('"').strip(",").strip("'").strip('(')\
                                        for i in sql_dic.get('values')[0].split(')') if i != '']
                        num = 0
                        flag = {}
                        for insert_data in insert_datas:
                            num += 1
                            insert_data = [i.strip("'").strip('"') for i in insert_data.split(',')]
                        # 判断字段是否对应
                            if len(title_list)-1 == len(insert_data):
                                last_id = increment_id(data)+int(num)
                                insert_data.insert(0,str(last_id))
                                insert_str = ','.join(insert_data)
                                write_add(path,insert_str)
                                flag['True'] = 1
                            else:
                                flag['False'] = 1
                                input_error()
                        if not flag.get('False'):
                            print("Query OK, %s row affected (%s sec)" % \
                                  (len(insert_datas),round(time.time() - start_time, 3)))
                    else:
                        print("ERROR: Duplicate entry '%s' for key 'UNIQUE'" % tag[0])
                else:
                    input_error()
            else: # insert into data.user (id,name) values (1,asa);
                input_error()
        else:
            print("ERROR: Table '%s' doesn't exist" % path)
    else:
        input_error()
def delete(sql_dic):
    '''
        删除操作
        :param sql_dic: 解析完的sql字典
    '''
    if sql_dic.get('from'):
        path = sql_dic['from'][0]
        if file_exists(path): # data.user
            title = open_title(path).readline()
            data = open_data(path).readlines()
            # where条件过滤
            where = sql_dic.get('where')
            where_data = []
            for line in data:
                combine_dic = dict(zip(title.split(','), line.split(',')))
                if where:
                    if not eval(data_compare(where,combine_dic)):
                        where_data.append(line)
                else:
                    where_data = []
            del_data= ''.join(where_data)
            write_file(path,del_data)
            print("Query OK, %s row affected (%s sec)" % (len(data)-len(where_data),round(time.time()-start_time,3)))
        else:
            print("ERROR: Table '%s' doesn't exist" % path)
    else:
        input_error()
def update(sql_dic):
    '''
         修改操作
        :param sql_dic: 解析完的sql字典
    '''
    set = sql_dic.get('set')
    sql_dic['set'] = set_parse(set)
    if sql_dic.get('update'):
        path = sql_dic['update'][0]
        if file_exists(path): # data.user
            title = open_title(path).readline()
            data = open_data(path).readlines()
            # where条件过滤
            where = sql_dic.get('where')
            where_data = []
            flag = []
            count = 0
            for line in data:
                combine_dic = dict(zip(title.split(','), line.split(',')))
                if where:
                    if eval(data_compare(where,combine_dic)):
                        count += 1
                        item = line.strip().split(',')
                        for set_con in sql_dic.get('set'):
                            # print(line.strip().split(','))
                            # print(set_con)
                            if set_con[0] in title:
                                set_index = title.split(',').index(set_con[0])
                                item[set_index] = set_con[2]
                            else:
                                flag.append(set_con[0])
                        where_data.append('%s\n' % ','.join(item))
                    else:
                        where_data.append(line)
                else:
                    where_data = []
            if len(flag) > 0:
                print("ERROR: Unknown column '%s' in 'field list'" % flag[0])
            else:
                update_data= ''.join(where_data)
                write_file(path,update_data)
                print("Query OK, %s row affected (%s sec)" % (count,round(time.time()-start_time,3)))
        else:
            print("ERROR: Table '%s' doesn't exist" % path)
    else:
        input_error()
def select(sql_dic):
    '''
        查询操作
        :param sql_dic: 解析完的sql字典
    '''
    if sql_dic.get('from'):
        path = sql_dic['from'][0]
        if file_exists(path): # data.user
            title = open_title(path).readline()
            data = open_data(path).readlines()
            # where条件过滤
            where = sql_dic.get('where')
            where_data = []
            for line in data:
                combine_dic = dict(zip(title.split(','), line.split(',')))
                if where:
                    if eval(data_compare(where,combine_dic)):
                        where_data.append(line)
                else:
                    where_data = data
            # limit条件过滤
            limit = sql_dic.get('limit')
            if limit:
                limit_data = where_data[0:int(limit[0])]
            else:
                limit_data = where_data
            # 字段条件过滤
            fields = sql_dic.get('select')
            if (set(fields[0].split(',')) <= set(title.split(','))) or fields[0] == '*':
                fields_data = []
                if fields[0] == '*':
                    fields_data = []
                    for line in limit_data:
                        fields_data.append(line.split(','))
                    fields_list = title.split(',')
                else:
                    fields_list = fields[0].split(',')
                    for item in limit_data:
                        dic = dict(zip(title.split(','), item.split(',')))
                        l = []
                        for field in fields_list:
                            if field in dic:
                                l.append(dic[field].strip())
                        fields_data.append(l)
                return format_output(fields_list,fields_data)
            else:
                print("ERROR: Unknown column '%s' in 'field list'" % fields[0].split(',')[0])
        else:
            print("ERROR: Table '%s' doesn't exist" % path)
    else:
        input_error()
def data_compare(where,line):
    '''
        where 条件的比较操作
        :param where: 格式化后的where列表
        :param line: 格式化后的数据字典
        :return: 返回字符串类型
    '''
    res = []
    for condition in where:
        if type(condition) is list: # ['id', '>', '2']    # if id > 2 and id < 6 or lucy in name:   a.append()
            key,con,value = condition
            if line[key].isdigit():
                line_v = int(line[key])
                value = int(value)
            else:
                line_v = "'%s'" % line[key].strip()
                value = "'%s'" % value.strip("'").strip('"')
            if con == '=':
                con = '=='
            if con == 'like':
                res.append(str(eval('%s %s %s'%(value,"in",line_v))))
            else:
                res.append(str(eval('%s %s %s'%(line_v,con,value))))
        else:
            res.append(condition)
    conditions = ' '.join(res)
    return conditions
def format_output(fields,data):
    '''
        格式化输出查询结果
        :param fields: 查询的字段
        :param data: 查询返回的数据
    '''
    line = PrettyTable(fields)
    line.align = "l"
    line.padding_width = 1
    for single in data:
        l = []
        for i in single:
            l.append(i.strip())
        line.add_row(l)
    print(line)
    print("%s rows in set (%s sec)\n"%(len(data),round(time.time()-start_time,3)))
def main():
    print('Welcome to the PySQL monitor.')
    flag = True
    while flag:
        sql = cmd_input() # 用户输入sql语句
        global start_time
        start_time = time.time()
        if sql == 'exit':
            print('Bye')
            break
        if not sql:continue
        sql_list = sql_to_list(sql)
        cmd = sql_list[0]
        if cmd in my_function():
            action = my_function()[cmd]
        else:
            print('ERROR: You have an error in your SQL syntax;')
            continue
        keywords_dic = sql_parse(sql_list) # 关键字格式化字典
        action(keywords_dic)
if __name__ == '__main__':
    main()