##闭包函数：定义在函数内部的函数，包含对外部作用域名字的引用
##而不是对全局作用域名字的引用
#那么内部函数就是闭包函数
x=1
def f1():
    x=1111
    def f2():
        print(x)
    return f2
func=f1()
func()


# def deco():
#     x=123
#     def wrapper():
#         d
#
###闭包函数的应用

# import requests ##pip3 install requests
# # def get(url):
# #     return requests.get(url).text
# # print(get('https://www.python.org'))
# def index(url):
#     #url='https://www.python.org'
#     def get():
#         print(requests.get(url).text)
#         return requests.get(url).text
#     return get
# python_web=index('https://www.python.org')
# baidu_web=index('https://www.baidu.com')
#
# python_web()
# baidu_web()

import requests  ##pip3 install requests
####查看封闭的变量
def index(url):
    x=1
    y=2
    def wrapper():
        # return requests.get(url).text
        print(x,y,url)
    return wrapper
python_web=index('https://www.python.org')
print(python_web)
# print(python_web.__closure__[0].cell_contents)
print(python_web.__closure__)
print(python_web.__closure__[0].cell_contents)
print(python_web.__closure__[1].cell_contents)
print(python_web.__closure__[2].cell_contents)