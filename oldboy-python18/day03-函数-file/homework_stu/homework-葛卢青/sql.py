#!/usr/bin/env python
#-*- coding:utf-8 -*-
#Author:glj
import os
def sql_parse(sql):
    parse_func={
        'insert':insert_parse,
        'delete':delete_parse,
        'update':update_parse,
        'select':select_parse,
    }
    sql_l=sql.split(' ')
    func=sql_l[0]
    res=''
    if func in parse_func:
        res=parse_func[func](sql_l)
    return res

def insert_parse(sql_1):
    sql_dic={
        'func':insert,
        'into':[], #查询字段
        'values':[] #数据.表
    }
    return handle_parse(sql_1,sql_dic)

def delete_parse(sql_1):
    sql_dic={
        'func':delete,
        'from':[],
        'where':[]
    }
    return handle_parse(sql_1,sql_dic)

def update_parse(sql_1):
    sql_dic={
        'func':update,
        'update':[],
        'set':[],
        'where':[]
    }
    return handle_parse(sql_1,sql_dic)
def select_parse(sql_1):
    sql_dic={
        'func':select,
        'select':[], #查询字段
        'from':[], #数据.表
        'where':[], #filter条件
        'limit':[], #limit条件
    }
    return handle_parse(sql_1,sql_dic)

def handle_parse(sql_l,sql_dic):
    tag=False
    for item in sql_l:
        if item in sql_dic:
            tag=True
            key=item
        if tag and item not in sql_dic:
            sql_dic[key].append(item)

    if sql_dic.get('where'):
        sql_dic['where']=where_parse(sql_dic.get('where'))
    return sql_dic


def where_parse(where_l):
    res=[]
    key=['and','or','not']
    char=''
    for i in where_l:
        if i not in key:
            char=char+i
        if i in key:
            char=three_parse(char)
            res.append(char)
            res.append(i)
            char=''
    char = three_parse(char)
    res.append(char)
    return res

def three_parse(str):
    key=['>','<','=']
    res=[]
    char=''
    for i in str:
        if i not in key:
            char += i
        if i in key:
            res.append(char)
            res.append(i)
            char=''

    res.append(char)
    if len(res) == 1:
        res=res[0].split('like')
        res.insert(1,'like')

    return res

def sql_action(sql_dic):

    return sql_dic["func"](sql_dic)

def select(sql_dic):

    db=sql_dic["from"][0].strip()
    f=open("%s" %(db),"r",encoding="utf-8")
    where_res=where_action(f,sql_dic["where"])
    f.close()

    limit_res=limit_action(sql_dic["limit"],where_res)

    select_res=select_action(sql_dic["select"],limit_res)

    return select_res

def insert(sql_dic):
    try:
        ph=sql_dic["values"][0].strip("'").split(",")[2]
        ph=sql_dic["values"][0].strip('"').split(",")[2]
    except:
        pass

    sql="select * from staff_table where phone = %s" %ph
    a=sql_action(sql_parse(sql))[1]

    if len(a):
        return "你的手机号%s已存在，更换其他手机号!" %ph
    else:
        id=1
        db=sql_dic["into"][0].strip()
        with open("%s" %db,"ab+") as f ,\
                open("%s"%db,'r', encoding="utf-8") as f1:
            for line in f1:
                id=id+1
            try:
                record=sql_dic["values"][0].strip("'").split(",")
                record=sql_dic["values"][0].strip('"').split(",")
            except:
                pass
            record.insert(0,str(id))
            record_new=",".join(record)+"\n"
            f.write(record_new.encode("utf-8"))
            f.flush()

        return "%s插入成功" %record_new

def delete(sql_dic):
    db=sql_dic["from"][0].strip()
    filename="%s" %(db)
    filename_new=db+"_new"
    file=open(filename,'r',encoding="utf-8")
    where_res=where_action(file,sql_dic["where"])
    file.close()

    if len(where_res)==0:
            return "删除记录不存在！"
    else:
        tmp=[]
        for line in where_res:
                tmp.append(line.strip())
        with open(filename,'r',encoding="utf-8") as f,\
                open(filename_new,'w',encoding="utf-8") as f1:
                id = 0
                for f_line in f:

                    if f_line.strip() in tmp:
                        continue
                    else:
                        id=1+id

                        con = f_line.strip("'").split(",")
                        con = f_line.strip('"').split(",")
                        con[0]=str(id)
                        content=",".join(con)
                        f1.write(content)
                f1.flush()

        os.rename(filename,filename+"b")
        os.rename(filename_new,filename)
        os.remove(filename+"b")
        return "共计删除%s条数据" %len(where_res)

def update(sql_dic):
    db=sql_dic["update"][0].strip()
    name="%s" %(db)
    name_new=db+"_new"
    file=open(name,'r',encoding="utf-8")
    records=where_action(file,sql_dic["where"])
    records_new=[]
    file.close()
    set_tmp=sql_dic["set"]
    data_tmp={}
    for i in set_tmp[0].split(","):
        if len(i):
            s=i.split("=")
            try:
                data_tmp[s[0]]=str(s[1].strip("'"))
                data_tmp[s[0]]=str(s[1].strip('"'))
            except:
                pass

    #"id,name,age,phone,dept,enroll_date"
    if len(records)==0:
            return "要修改的记录不存在！"
    else:
        for line in records:
                dic={}
                dic['id'],dic['name'],dic['age'],dic['phone'],dic['dept'],dic['enroll_date']=line.split(",")
                for data_k in data_tmp:
                    if data_k in dic:
                        dic[data_k]=data_tmp[data_k]
                str_tmp=[]

                for k in dic:
                    str_tmp.append(dic[k])

                records_new.append(str_tmp)
        str_tmp=[]
        for line in records:
            str_tmp.append(line.strip())

        with open(name,'r',encoding="utf-8") as f,\
                open(name_new,'w',encoding="utf-8") as f1:
                for f_line in f:

                    if f_line.strip() in str_tmp:

                        temp=records_new[str_tmp.index(f_line.strip())]
                        temp=",".join(temp)
                        f1.write(temp)
                        continue
                    f1.write(f_line)
                    f1.flush()
        os.rename(name,name+"b")
        os.rename(name_new,name)
        os.remove(name+"b")

        return "共计修改%s条数" %len(records)

def where_action(f,where_sql):
    #"id,name,age,phone,dept,enroll_date"
    res=[]
    if len(where_sql):
        for line in f:
            dic={}
            dic['id'], dic['name'], dic['age'], dic['phone'], dic['dept'], dic['enroll_date'] = line.split(",")

            logic_res=logic_action(dic,where_sql)
            if logic_res:
                res.append(line)
    else:
        res=f.readlines()

    return res

def logic_action(dic,where_l):
    res=[]
    for i in where_l:
        if type(i) is list:
            a,o,b=i
            if i[1] == '=':
                o="%s=" %i[1]
            dic_v=""
            if dic[a].isdigit():
                    dic_v=int(dic[a])
                    b=int(b)
            else:
                    dic_v="'%s'" %dic[a]
            if o != 'like':
                if type(b)==str:
                    try:
                        b= b.strip("'")
                        b= b.strip('"')
                    except:
                        pass
                    b="'%s'" %b
                i=str(eval("%s%s%s" %(dic_v,o,b)))
            else:
                try:
                   b= b.strip("'")
                   b= b.strip('"')
                except:
                    pass
                if b in dic_v:
                    i='True'
                else:
                    i='False'
        res.append(i)

    res=eval(' '.join(res))
    return res

def limit_action(limit_sql,where_res):
    if len(limit_sql)!=0:
        index=int(limit_sql[0])
        res=where_res[0:index]
    else:
        res=where_res
    return res

def select_action(select_sql,limit_res):
    res=[]
    #"id,name,age,phone,dept,enroll_date"
    select_field=select_sql
    if select_sql[0]=="*":
        res=limit_res
        select_field=['id', 'name', 'age', 'phone', 'dept', 'enroll_date']

    else:
        for line in limit_res:
            dic={}
            dic['id'], dic['name'], dic['age'], dic['phone'], dic['dept'], dic['enroll_date'] = line.split(",")

            r=[]
            for field in select_field[0].split(","):
                r.append(dic[field])
            res.append(",".join(r))
    return [select_field,res]


if __name__ == '__main__':
    print("表名：staff_table，字段：id,name,age,phone,dept,enroll_date")
    while True:
        sql=input("sql> ").strip()
        if sql == 'exit':break
        if len(sql) == 0 :continue

        sql_dic=sql_parse(sql)

        if len(sql_dic) == 0:continue

        res=sql_action(sql_dic)
        if type(res)==list:
            for line in res[1]:
                print(line.strip())
            print("\n共计查询出%s条数据" %len(res[1]))
        else:
            print(res)
