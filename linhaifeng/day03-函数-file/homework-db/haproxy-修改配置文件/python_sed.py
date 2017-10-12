

###查询
def fetch(data):
    #backend www.oldboy.com
    backend_data='backend %s'%data
    record_list=[]
    with  open('haproxy.conf','r') as f:
        tag=False
        for line in f:
            if line.strip() == backend_data:  ###取开始跳过本次取后面内容
                tag=True
                continue
            if tag and line.startswith('backend'):  ###遇到结尾跳出循环
                break
            if tag and line:   ###池子加入列表
                record_list.append(line.strip())

    for line in record_list:
         print(line)
    return record_list
###添加
def add(data):
    # data={'backend':'www.oldboy.com','record':{'server':'1.1.1.11','weight':22,'maxconn':33}}
    # data={'backend':'www.huboa.com','record':{'server':'1.1.1.11','weight':22,'maxconn':33}}

    backend=data['backend']   ####获取域名
    record_list=fetch(backend)     ####查询域名backend存在不存在

    ####需要录入的域名
    backend_data = "backend %s" % backend
    ####backend的池子内容
    current_record='server %s %s weight %s maxconn %s' %(data['record']['server'], \
                                                             data['record']['server'], \
                                                             data['record']['weight'],\
                                                             data['record']['maxconn'])


    if record_list:  ###修改已经存在的backend
        print("record_list--修改已经存在的", record_list)
        record_list.insert(0, backend_data)
        if current_record not in record_list:
            record_list.append(current_record)
        print("record_list--修改后的", record_list)

        with  open('haproxy.conf', 'r') as read_file, \
                open('haproxy_new.conf', 'w') as write_file:
            tag = False
            tag_s = False
            for r_line in read_file:
                if r_line.strip() == backend_data:  #给backend 打标签
                    tag = True
                    tag_s = True
                    continue
                if tag and r_line.startswith('backend'):
                    continue

                if tag :  ###如过遇到backend 执行更新
                    for new_line in record_list:
                        if new_line.startswith('backend'):
                            write_file.write('\n' + new_line + '\n')
                        else:
                            write_file.write('%s%s\n' % (' ' * 8, new_line))


                else:###复制其它数据
                    write_file.write(r_line)
    else: ###新建backend
        record_list.append(backend_data)
        record_list.append(current_record)
        with  open('haproxy.conf', 'r') as read_file, \
               open('haproxy_new.conf', 'w') as write_file:
            for r_line in read_file:
                write_file.write(r_line)
            for new_line in record_list:
                if new_line.startswith('backend'):
                    write_file.write('\n'+new_line+'\n')
                else:
                    write_file.write('%s%s\n'%(' '*8,new_line))


##删除
def remove(data):
    pass
    # backend = data['backend']  ####获取域名
    # record_list = fetch(backend)  ####查询域名存在不存在
    #
    # ####域名
    # backend_data = "backend %s" % backend
    # ####池子内容
    # current_record = 'server %s %s weight %s maxconn %s' % (data['record']['server'], \
    #                                                         data['record']['server'], \
    #                                                         data['record']['weight'], \
    #                                                         data['record']['maxconn'])
    # if not record_list or current_record not in record_list:
    #     print('\033[33:1m 无此记录\033[0m')
    #     return
    # else:
    #     record_list.append(backend_data)
    #     record_list.append(current_record)
    #     with  open('haproxy.conf', 'r') as read_file, \
    #             open('haproxy_new.conf', 'w') as write_file:
    #         for r_line in read_file:
    #             write_file.write(r_line)
##主函数
if __name__ == '__main__':
    msg='''
    1：查询
    2：添加
    3：删除
    4：退出
    '''
    menu_dic={
        '1':fetch,
        '2':add,
        '3':remove,
        '4':exit,
        }
    while True:
        print(msg)
        choice=input('操作：').strip()
        if len(choice) == 0 or choice not in menu_dic:continue
        if choice == '4' :break

        data=input('数据：').strip()
        print(data)
        if choice != '1':
            data=eval(data)
        menu_dic[choice](data) ##=== fetch(data)
