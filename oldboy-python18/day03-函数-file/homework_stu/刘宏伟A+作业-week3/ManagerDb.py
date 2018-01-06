#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017/7/16 0009 12:01
# @Author  : LiuHongWei
# @Site    :
# @File    : ManagerDb.py
# @Software: PyCharm
import linecache
import os

# 判断语句中的表名是否正确
def exits_db(sql):
    db_name = 'staff_table'
    if 'from' in sql:
        if str(sql[int(sql.index('from')) + 1]) == db_name:
            return True
        print("您输入的表名有误")
        return False
    elif 'into' in sql:
        if str(sql[int(sql.index('into')) + 1]) == db_name:
            return True
        print("您输入的表名有误")
        return False
    elif 'update' in sql:
        if str(sql[int(sql.index('update')) + 1]) == db_name:
            return True
        print("您输入的表名有误")
        return False
# 判断字段属于那类
def filedsClassify(fileld):
    # 数字类型
    table_field_digit = ['staff_id', 'age',]
    # 字符串类型
    table_field_str = ['name', 'phone', 'dept', 'enroll_date']

    if fileld in table_field_digit:
        return 'field_digit'
    elif fileld in table_field_str:
        return 'field_str'
    else:
        return False
# 字段是否为表中字段
def isExitsField(field):
    table_field_all = ['name', 'phone', 'dept', 'enroll_date', 'staff_id', 'age']
    # 判断字段是否存在
    if field in table_field_all:
        return True
    else:
        return False
# 把行内容转为字典类型
def lineContentDic(line):
    line_info = {}
    line_info['staff_id'] = line[0]
    line_info['name'] = line[1]
    line_info['age'] = line[2]
    line_info['phone'] = line[3]
    line_info['dept'] = line[4]
    line_info['enroll_date'] = line[5].strip('\n')
    return line_info
# 把行内容字典类型转为字符串
def lineString(line_dic):
    line_string = list(line_dic.values())
    line_string = ','.join(line_string)
    return line_string
''' 
#输入一行根据字段为*全部还是部分字段，字段传入为列表类型
#line为一整行内容为字典类型
#fields默认为*输出全部，传入值为列表类型'''
def outLine(line,fields = '*'):
    content = ''
    if fields == '*':
        print(' '.join(line.values()))
    else:
        for i in fields:
            content += str(line[i])+' '
        print(content)

# 去除字段左右两边单引号
def removeQuotes(field):
    return str(field).replace("'","")

# 查询方法
def SelectDb(sql):
    #读取文件
    with open(r'%s'%'db.txt','r',encoding='utf-8') as dbread:
        # 查询条数
        count = 0
        # 判断查询是否为*但又没有where的操作
        if sql[1] == '*' and 'where' not in sql:
            for line in dbread:
                print(line.replace(',',' ').strip('\n'))
                count +=1
            print('共打印',count,'条')

        #判断查询字段为*且有where操作，并且条件后的参数只有一个的情况下
        elif (sql[1] == '*') and ('where' in sql) and (sql.__len__() - sql.index('where')<5):
            # 条件字段位置
            where_fields_index = int(sql.index('where')) + 1
            # where操作符的位置
            where_operator_index = where_fields_index + 1
            # where条件要比较值的位置
            operator_value_index = where_operator_index + 1
            for line in dbread:
                line_list = line.split(',')
                line_dic = lineContentDic(line_list)
                # 判断查询条件的字段为数字类型
                if filedsClassify(sql[where_fields_index]) == 'field_digit':
                    # 如果操作符为=
                    if sql[where_operator_index] == '=':
                        # 判断执行sql中表中数据是否与条件语句的值相匹配
                        # 匹配则打印出行信息
                        if line_dic[sql[where_fields_index]] == removeQuotes(sql[operator_value_index]):
                            # 数量加1
                            count +=1
                            # 输出行
                            outLine(line_dic)
                            #继续下一循环
                            continue
                    # 如果操作符为<
                    elif sql[where_operator_index] == '<':
                        if line_dic[sql[where_fields_index]] < removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic)
                            continue
                    # 如果操作符为>
                    elif sql[where_operator_index] == '>':
                        if line_dic[sql[where_fields_index]] > removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic)
                            continue
                    # 如果操作符为!=
                    elif sql[where_operator_index] == '!=':
                        if line_dic[sql[where_fields_index]] != removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic)
                            continue
                    # 如果操作符为like
                    elif sql[where_operator_index] == 'like':
                        if removeQuotes(sql[operator_value_index]) in line_dic[sql[where_fields_index]]:
                            count +=1
                            outLine(line_dic)
                            continue
                    else:
                        print("您输入的有问题,请重新输入")
                        return True
                elif filedsClassify(sql[where_fields_index]) == 'field_str':
                    # 如果操作符为=
                    if sql[where_operator_index] == '=':
                        if line_dic[sql[where_fields_index]] == removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic)
                            continue
                    # 如果操作符为!=
                    elif sql[where_operator_index] == '!=':
                        if line_dic[sql[where_fields_index]] != removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic)
                            continue
                    # 如果操作符为like
                    elif sql[where_operator_index] == 'like':
                        if removeQuotes(sql[operator_value_index]) in line_dic[sql[where_fields_index]]:
                            count +=1
                            outLine(line_dic)
                            continue
                    else:
                        print("您输入的有问题,请重新输入")
                        return True
                else:
                    print("您输入的有问题请重新输入")
                    return True
            else:
                print("共打印", count, "条")
        # 判断select 语句中查询字段为多字段且有where条件，并且条件参数只有一个
        elif (sql[1] != '*') and len(sql[1].split(','))>0 and ('where' in sql) and (sql.__len__() - sql.index('where')<5):
            content_fields = sql[1].split(',')
            table_field_all = ['name', 'phone', 'dept', 'enroll_date', 'staff_id', 'age']
            # 条件字段位置
            where_fields_index = int(sql.index('where')) + 1
            # where操作符的位置
            where_operator_index = where_fields_index + 1
            # where条件要比较值的位置
            operator_value_index = where_operator_index + 1
            for fields in content_fields:
                if fields not in table_field_all:
                    print("您输入的查询字段有误请重新输入")
                    return True
            for line in dbread:
                line_list = line.split(',')
                line_dic = lineContentDic(line_list)
                if filedsClassify(sql[where_fields_index]) == 'field_digit':
                    # 如果操作符为=
                    if sql[where_operator_index] == '=':
                        if line_dic[sql[where_fields_index]] == removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic,content_fields)
                            continue
                    # 如果操作符为<
                    elif sql[where_operator_index] == '<':
                        if line_dic[sql[where_fields_index]] < removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic,content_fields)
                            continue
                    # 如果操作符为>
                    elif sql[where_operator_index] == '>':
                        if line_dic[sql[where_fields_index]] > removeQuotes(sql[operator_value_index]):
                            outLine(line_dic,content_fields)
                            count += 1
                            continue
                    # 如果操作符为!=
                    elif sql[where_operator_index] == '!=':
                        if line_dic[sql[where_fields_index]] != removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic,content_fields)
                            continue
                    # 如果操作符为like
                    elif sql[where_operator_index] == 'like':
                        if removeQuotes(sql[operator_value_index]) in line_dic[sql[where_fields_index]]:
                            count +=1
                            outLine(line_dic,content_fields)
                            continue
                    else:
                        print("您输入的条件符号有问题,请重新输入")
                        return True
                # 判断字段为字符
                elif filedsClassify(sql[where_fields_index]) == 'field_str':
                    # 如果操作符为=
                    if sql[where_operator_index] == '=':
                        if line_dic[sql[where_fields_index]] == removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic,content_fields)
                            continue
                    # 如果操作符为!=
                    elif sql[where_operator_index] == '!=':
                        if line_dic[sql[where_fields_index]] != removeQuotes(sql[operator_value_index]):
                            count +=1
                            outLine(line_dic,content_fields)
                            continue
                    # 如果操作符为like
                    elif sql[where_operator_index] == 'like':
                        if removeQuotes(sql[operator_value_index]) in line_dic[sql[where_fields_index]]:
                            count +=1
                            outLine(line_dic,content_fields)
                            continue
                    else:
                        print("您输入的条件符号有问题,请重新输入")
                        return True
                else:
                    print("您输入的条件字段有问题,请重新输入")
                    return True
            else:
                print("共打印",count,"条")
# 插入函数
def InsertDb(sql):
    # 先以左括号拆分列表的第三个位置的值
    sql = sql[3].split('(')
    # 拆分后判断是values是否正确为第一位
    if sql[0] != 'values':
        print("输入有误请重新输入")
    # 如果values语法正确
    else:
        #拆分(括号的后，再以)号进行拆分取出values后（）中的值
        sql=sql[1].split(')')
        #拆分（）的值为列表
        sql = sql[0].split(',')
        #判断要插入的值是否与表中字段的数量相等
        if int(len(sql)) < 5:
            print("您输入有误请重新输入")
            return True
        else:
            # 判断插入的字段顺序以及age和phone字段是否类型一致
            if sql[1].isdigit() and sql[2].isdigit():
                # 打开要插入的文件和要读取的文件
                with open(r'%s'%"db.txt", "a+", encoding='utf-8') as db_insert, open(r'%s'%"db.txt", "r",encoding='utf-8') as db_read:
                    # 读取行
                    for line_value in db_read.readlines():
                        # 判断手机号是否被注册过
                        if (line_value.split(','))[3] == sql[2]:
                            print("您输入的电话号码已经被注册过了,请重新输入")
                            return True
                    # 把文件指针倒回开头
                    db_read.seek(0)
                    # 获取文件数据的行数
                    lines = len(db_read.readlines())
                    # 用linecache获取文件最后一行的内容
                    last_line_content = lineContentDic(linecache.getline('db.txt',lines).split(','))
                    # 根据最后一行的staff_id自增+1插入要新增的行里
                    sql.insert(0,str(int(last_line_content['staff_id'])+1))
                    # 把列表转为字符串
                    new_line_content=','.join(sql)
                    #去除里边的单引号
                    new_line_content = removeQuotes(new_line_content)
                    #写入到文件中
                    db_insert.writelines(new_line_content+'\n')
                    print("插入成功")
            else:
                print("您输入的字段类型不对,请重新输入")
                return True
'''
# 删除函数
# 删除函数目前只支持单条件,且都以空格格开,语句支持 =,<,>,!=,like,示例如下
# delete from staff_table where staff_id = 1
'''
def DeleteData(sql):
    # 判断语句是否正确
    if 'from' not in sql or 'where'not in sql:
        print("您输入的有误请重新输入")
    # 如果语句正确
    else:
        # 条件字段位置
        field_index = int(sql.index('where')) + 1
        # 条件操作符位置
        operator_index = field_index + 1
        # 条件操作值的位置
        compare_value_index = operator_index + 1
        # 判断字段是否合法
        if isExitsField(sql[field_index]) == False:
            print('您输入的有误，请重新输入')
            return True
        # 合法
        else:
            # 打开读取文件和写临时文件
            with open(r'%s' % "db_temp.txt", "a", encoding='utf-8') as db_write, \
                    open(r'%s' % "db.txt", "r",encoding='utf-8') as db_read:
                # 读取行行
                for line in db_read.readlines():
                    # 把行拆分成列表
                    line_list = line.split(',')
                    # 把列表转为字典
                    line_dic = lineContentDic(line_list)
                    # 判断条件字段是否属于数字类
                    if filedsClassify(sql[field_index]) == 'field_digit':
                        # 如果操作符为=
                        if sql[operator_index] == '=':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            # 匹配则返回
                            if line_dic[sql[field_index]] == removeQuotes(sql[compare_value_index]):
                                continue
                            #不匹配则写入临时文件
                            else:
                                db_write.write(line)
                        # 如果操作符为<
                        elif sql[operator_index] == '<':
                            if line_dic[sql[field_index]] < removeQuotes(sql[compare_value_index]):
                                continue
                            else:
                                db_write.write(line)
                        # 如果操作符为>
                        elif sql[operator_index] == '>':
                            if line_dic[sql[field_index]] > removeQuotes(sql[compare_value_index]):
                                continue
                            else:
                                db_write.write(line)
                        # 如果操作符为!=
                        elif sql[operator_index] == '!=':
                            if line_dic[sql[field_index]] != removeQuotes(sql[compare_value_index]):
                                continue
                            else:
                                db_write.write(line)
                        # 如果操作符为like
                        elif removeQuotes(sql[operator_index]) == 'like':
                            if sql[compare_value_index] in line_dic[sql[field_index]]:
                                continue
                            else:
                                db_write.write(line)
                        else:
                            print("您输入的有问题,请重新输入")
                            return True
                    # 判断条件字段是否属于字符串类
                    elif filedsClassify(sql[field_index]) == 'field_str':
                        # 如果操作符为=
                        if sql[operator_index] == '=':
                            if line_dic[sql[field_index]] == removeQuotes(sql[compare_value_index]):
                                continue
                            else:
                                db_write.write(line)
                        # 如果操作符为!=
                        elif sql[operator_index] == '!=':
                            if line_dic[sql[field_index]] != removeQuotes(sql[compare_value_index]):
                                continue
                            else:
                                db_write.write(line)
                        # 如果操作符为like
                        elif sql[operator_index] == 'like':
                            if removeQuotes(sql[compare_value_index]) in line_dic[sql[field_index]]:
                                continue
                            else:
                                db_write.write(line)
                        else:
                            print("您输入的有问题,请重新输入")
                            return True
                    else:
                        print("您输入的有问题请重新输入")
                        return True
                else:
                    db_read.close()
                    db_write.close()
                    #用os删除以前的旧表
                    os.remove('db.txt')
                    #用os把临时文件名改为正式的
                    os.renames('db_temp.txt','db.txt')
                    print("删除成功")
'''
# 更新函数
# 目前更新函数只适应普通的更新语句,且都以空格格开,并且set值只能是一个,条件语句支持 =,<,>,!=,like,示例如下
# update staff_table set dept = 'IT' where age = 30
'''
def UpdateData(sql):
    # 判断更新语句的是否正确
    if 'update' not in sql or 'where'not in sql or 'set' not in sql:
        print("您输入的有误请重新输入")
        return True
    # 如果正确
    else:
        # where位置
        where_index = sql.index('where')
        # set位置
        set_index = sql.index('set')
        # where条件字段的位置
        where_field_index = int(where_index) + 1
        # set字段的位置
        set_field_index = int(set_index) + 1
        # set操作符的位置
        set_operator_index = set_field_index + 1
        # where操作符的位置
        where_operator_index = where_field_index + 1
        # where条件要比较值的位置
        operator_value_index = where_operator_index + 1
        # set要设置字段值的位置
        set_field__value_index = set_operator_index + 1
        # 判断where字段和set 字段是否合法
        if isExitsField(sql[where_field_index]) == False or isExitsField(sql[set_field_index]) == False:
            print("您输入的字段有误，请重新输入")
            return True
        # 如果合法
        else:
            # 打开读取表名件和打开写入临时文件
            with open(r'%s' % "db_temp.txt", "a", encoding='utf-8') as db_write, \
                    open(r'%s' % "db.txt", "r",encoding='utf-8') as db_read:
                # 读取行
                for line in db_read.readlines():
                    # 把行拆分成列表
                    line_list = line.split(',')
                    #把列表转为字典
                    line_dic = lineContentDic(line_list)
                    #判断条件字段是否属于数字类
                    if filedsClassify(sql[where_field_index]) == 'field_digit':
                        # 判断条件操作符是否为=
                        if sql[where_operator_index] == '=':
                                # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if line_dic[sql[where_field_index]] == removeQuotes(sql[operator_value_index]):
                                # 判断set操作符是否为=
                                if sql[set_operator_index] == '=':
                                    # 给要set的字段设置值
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    # 把字段转为字符
                                    line_new_content = lineString(line_dic)
                                    # 存入临时表中
                                    db_write.writelines(line_new_content + '\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        # 判断条件操作符是否为<
                        elif sql[where_operator_index] == '<':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if line_dic[sql[where_field_index]] < removeQuotes(sql[operator_value_index]):
                                if sql[set_operator_index] == '=':
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    line_new_content = lineString(line_dic)
                                    db_write.writelines(line_new_content+'\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        # 判断条件操作符是否为>
                        elif sql[where_operator_index] == '>':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if line_dic[sql[where_field_index]] > removeQuotes(sql[operator_value_index]):
                                if sql[set_operator_index] == '=':
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    line_new_content = lineString(line_dic)
                                    db_write.writelines(line_new_content+'\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        # 判断条件操作符是否为!=
                        elif sql[where_operator_index] == '!=':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if line_dic[sql[where_field_index]] != removeQuotes(sql[operator_value_index]):
                                if sql[set_operator_index] == '=':
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    line_new_content = lineString(line_dic)
                                    db_write.writelines(line_new_content+'\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        # 判断条件操作符是否为like
                        elif sql[where_operator_index] == 'like':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if removeQuotes(sql[operator_value_index]) in line_dic[sql[where_field_index]]:
                                if sql[set_operator_index] == '=':
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    line_new_content = lineString(line_dic)
                                    db_write.writelines(line_new_content+'\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        else:
                            print("您输入的有问题,请重新输入")
                            return True
                    # 判断条件字段如果属于字符类
                    elif filedsClassify(sql[where_field_index]) == 'field_str':
                        if sql[where_operator_index] == '=':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if line_dic[sql[where_field_index]] == removeQuotes(sql[operator_value_index]):
                                # 判断set操作符是否为=
                                if sql[set_operator_index] == '=':
                                    # 给要set的字段设置值并把值的左右单引号去掉
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    #把值由字典转为字符串
                                    line_new_content = lineString(line_dic)
                                    # 写入临时表
                                    db_write.writelines(line_new_content+'\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        # 判断条件操作符是否为!=
                        elif sql[where_operator_index] == '!=':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if line_dic[sql[where_field_index]] != removeQuotes(sql[operator_value_index]):
                                if sql[set_operator_index] == '=':
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    line_new_content = lineString(line_dic)
                                    db_write.writelines(line_new_content+'\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        # 判断条件操作符是否为like
                        elif sql[where_operator_index] == 'like':
                            # 判断执行sql中表中数据是否与条件语句的值相匹配
                            if removeQuotes(sql[operator_value_index]) in line_dic[sql[where_field_index]]:
                                if sql[set_operator_index] == '=':
                                    line_dic[sql[set_field_index]] = removeQuotes(sql[set_field__value_index])
                                    line_new_content = lineString(line_dic)
                                    db_write.writelines(line_new_content+'\n')
                                else:
                                    print("输入有误请重新输入")
                                    return True
                            else:
                                db_write.write(line)
                        else:
                            print("您输入的有问题,请重新输入")
                            return True
                    else:
                        print("您输入的有问题请重新输入")
                        return True
                else:
                    db_read.close()
                    db_write.close()
                    #用os删除以前的旧表
                    os.remove('db.txt')
                    #用os把临时表改名为
                    os.renames('db_temp.txt','db.txt')
                    print("修改成功")

def ManagerDb():
    while True:
        print("请输入正确的mysql语句")
        sql=input(">>>:")
        sql = (sql.strip()).split()
        if exits_db(sql):
            print("输入表名正确")
            if len(sql) < 4:
                print("您输入的有误,请重新输入")
                continue
            elif sql[0] == 'select':
                if SelectDb(sql) == True:
                    continue
            elif sql[0] == 'insert':
                if len(sql)>5:
                    print("您输入的有误,请重新输入")
                    continue
                else:
                    if InsertDb(sql) == True:
                        continue
            elif sql[0] == 'update':
                UpdateData(sql)
            elif sql[0] == 'delete':
                if len(sql) > 10:
                    print("您输入的有误,请重新输入")
                    continue
                else:
                    DeleteData(sql)
            else:
                print("输入有误，请重新输入")
                continue
            break
        else:
            print("您输入的有误,请重新输入")
ManagerDb()

