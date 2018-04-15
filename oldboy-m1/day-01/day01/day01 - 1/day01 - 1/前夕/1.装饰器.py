
def wapper(func):
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner
"""
1. 立即执行wapper函数，并将下面装饰的函数当做参数传递
2. 将wapper函数返回值获取，在index赋值
    index = inner函数
"""
@wapper
def index():
    print('函数内容')

# 实际执行的 inner函数，inner函数内部调用原函数
index()