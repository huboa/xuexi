
def fetch(data):
    backend_data='backend %s'%data
    record_list=[]
    with  open('haproxy.conf','r') as f:
        tag=False
        for line in f:
            if line.strip() == backend_data:  ###取开始
                tag=True
                continue
            if tag and line.startswith('backend'):  ###取结尾
                break
            if tag and line:   ###取列表
                record_list.append(line.strip())
    for line in record_list:
         print(line)
    return record_list

def add(data):
    backend=data['backend']
    record_list=fetch(backend)
    backend_data="backend %s"%backend



def remove(data):
    pass
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
            eval(data)
        menu_dic[choice](data) ##=== fetch(data)
