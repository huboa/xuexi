class school:
    def __init__(self, name, address,city):
        self.name = name
        self.address = address
        self.city=city
class student:
    def __init__(self, name, age, sex='male'):
        self.name = name
        self.age = age
        self.sex = sex
class teacher:
    def __init__(self, name, age, sex='male'):
        self.name = name
        self.age = age
        self.sex = sex
class course:
    def __init__(self,name,period,price):
        self.name=name
        self.period=period
        self.price=price
    def tell_info(self):
        print('<课程名:%s 周期：%s 价格：%s>' %(self.name,self.period,self.price))
class classes:
    def __init__(self,name,semester,course,date,teacher):
        self.name=name
        self.semester=semester
        self.course=course
        self.date=date
        self.teacher=teacher
class classes_record:
    def __init__(self,classes,times,date):
        self.classes=classes
        self.times=times
        self.date=date
class study_record:
   def __init__(self,classes_record,status,date,score):
       self.classes_record=classes_record
       self.status=status
       self.date=date
       self.score=score

#db.txt内容:egon1|egon2|
dic={
    'sudo1':{'password':'123','count':0},
    'sudo2':{'password':'123','count':0},
    'sudo3':{'password':'123','count':0},
}


count=0
while True:
    name=input('请输入用户名 q退出程序 >>: ')
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




