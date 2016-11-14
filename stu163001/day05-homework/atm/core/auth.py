user_status =False

def login(func):
    def inner():
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
    return inner



