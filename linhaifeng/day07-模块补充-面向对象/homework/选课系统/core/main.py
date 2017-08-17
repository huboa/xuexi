import auth

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
def create_id():
    while True:

        goods = [
            {"name": "校区", "class_name": school},
            {"name": "课程", "class_name": course},
            {"name": "班级", "class_name": classes},
        ]
        ##显示商品信息
        print('编号  名称  功能')
        n = 1
        for good in goods:
            print('  %d   %s  %s' % (n, good["name"], good["class_name"]))
            n += 1

        ##输入选项
        good_c = 1
        choice = input("请输入要选择的功能,q 退出 :").strip()
        if len(choice) == 0: continue  ###空则跳过
        if choice == "q": break
        if choice.isdigit():
            choice = int(choice)  ##转换成数字
        else:
            print("请输入数字")
            continue

        good_all_c = range(1, len(goods) + 1)
        if choice not in good_all_c:
            print("编号错误,请重新输入")
            continue

@auth.auth
def main():
    while True:
        create_id()

main()



