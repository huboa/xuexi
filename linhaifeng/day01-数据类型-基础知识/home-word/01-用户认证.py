#db.txt内容:egon1|egon2|
dic={
    'sudo1':{'password':'123','count':0},
    'sudo2':{'password':'123','count':0},
    'sudo3':{'password':'123','count':0},
}

count=0
while True:
    name=input('q退出 u >>: ')
    if name == 'q':break
    if name not in dic:
        print('用户不存在')
        continue

    with open('db.txt','r') as f:
        lock_users=f.read().split('|')
        if name  in lock_users:
            print('用户%s已经被锁定' %name)
            break


    while True:
        if dic[name]['count'] > 2:
            print('尝试次数过多,锁定')
            with open('db.txt', 'a') as f:
                f.write('%s|' % name)
            break

        password=input('p >>: ')
        if password == dic[name]['password']:
            print('登录成功')
            break
        else:
            print('用户名或密码错误')
            dic[name]['count']+=1