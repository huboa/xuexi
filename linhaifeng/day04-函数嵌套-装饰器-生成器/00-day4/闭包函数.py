#大前提：作用域关系，在函数定义时就已经固定
# ，于调用位置无关,在调用函数时，必须必须必须
#回到函数原来定义的位置去找作用域关系


#闭包函数：
#1. 定义在函数内部的函数
#2. 包含对外部作用域名字的引用，而不是对全局作用域名字的引用
#那么该内部函数就称为闭包函数
# x=1
# def  f1():
#     x=11111111111
#     def f2():
#         print(x)
#     return f2
#
# func=f1()


# x=1000
# func()

# def foo():
#     x=12312312312312312312312312312312312313123
#     func()
#
#
# foo()


# def deco():
#     x=123123123123
#     def wrapper():
#         print(x)
#     return wrapper
#
# func=deco()


# func()


#闭包函数的应用:惰性计算
import requests #pip3 install requests

# def get(url):
#     return requests.get(url).text
#
# print(get('https://www.python.org'))
# print(get('https://www.python.org'))
# print(get('https://www.python.org'))
# print(get('https://www.python.org'))

# def index(url):
#     # url='https://www.python.org'
#     def get():
#         # return requests.get(url).text
#         print(requests.get(url).text)
#
#     return get
#
# python_web=index('https://www.python.org')
# baidu_web=index('https://www.baidu.com')

# python_web()
# baidu_web()






name='egon'
def index(url):
    x=1
    y=2
    def wrapper():
        # x
        # y
        # return requests.get(url).text
        print(name)
    return wrapper

python_web=index('https://www.python.org')

# print(python_web.__closure__[0].cell_contents)
print(python_web.__closure__)
# print(python_web.__closure__[0].cell_contents)
# print(python_web.__closure__[1].cell_contents)
# print(python_web.__closure__[2].cell_contents)


