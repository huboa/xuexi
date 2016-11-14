##不带参数的运行
#
# def sayHi():
#     print("Hello, I'm chongchong")
#
# sayHi()
#
# print(sayHi) ###内存地址
# print(sayHi())
#
# #####带参数的
# def sayHe(name,age):
#     print("Hello, I'm %s" % name)
#
# sayHe("chongchong",22)
# sayHe("xx",22)
###默认参数
# def main(name,age,sex="F",nationality="CN"):
#     ####name,age 位置参数，指定的为关键参数
#     print("----注册学生信息------")
#     print("姓名:",name)
#     print("age:", age)
#     print("国籍:", sex)
#     print("课程:", nationality)
# main("zsc","22","F","JP")
#

###非固定参数

# def main1(name,age,sex="F",nationality="CN",*args,**kwargs):
#     ####name,age 位置参数，指定的为关键参数
#     print("----注册学生信息------")
#     print("姓名:",name)
#     print("age:", age)
#     print("性别:", sex)
#     print("国家:", nationality)
#     print("other arguments:",args,kwargs)
# main1("zsc","22","F","JP")
#
# main1("zsc","22","F","JP",sex1="Male",province="HEBEI")
# main1("ZXX","22",sex="Male",province="HEBEI")

###返回值
# def auth(username,password):
#     #get data from db
#     _username = "alex"
#     _password = "alex3714"
#
#
# user = input("username:").strip()
# passwd = input("password:").strip()


###局部变量
login_status = False

def auth():
    _username = "zsc"
    _password = "123"
    user = input("username:").strip()
    passwd = input("password:").strip()

    if user == _username and passwd == _password:
        global login_status
        login_status = True
        print("-->",login_status)

auth()
print("global-->",login_status)
###返回值
#函数执行，函数外部不会影响内部，是调取函数结束后返回的状态，
#1.return 结束函数
#2.return 可以返回任何数据类型
#3.return 可以返回1个值


