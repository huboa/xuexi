user_status =False

def login(auth_type):
    def outer(*args,**kwargs):


        def inner():
            print("-->", func, auth_type, args, kwargs)
            _username = "zsc"
            _password = "123456"
            global user_status

            if user_status == False:
                username = input("user:")
                password = input("password:")

                if username == _username and password == _password:
                    print("welcome login...")
                    user_status =True
                else:
                    print("wrong username or password!")

                if user_status == True:
                    func()##只要验证通过就 调用相应功能
            else:
                print("only support qq...")
        return inner

    return outer()

def home():
    print("首页")

@login("qq")
def america():
    print("-----欧美————————")
def japan():
    print("-----日韩------")
def beijing():
    print("---北京")

america()