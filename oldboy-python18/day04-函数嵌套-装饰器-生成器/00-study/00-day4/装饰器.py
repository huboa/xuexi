#1 开放封闭原则：对扩展是开放的，对修改是封闭

#2 装饰器：装饰它人的工具，
#装饰器本身可以是任意可调用对象，被装饰的对象本身也可以是任意可调用对象

#2.1 装饰器的遵循的原则：1 不修改被装饰对象的源代码 2 不修改被调用对象的调用方式
#2.2 装饰器的目的是：在遵循1和2原则的前提，为其他新功能函数添加

#@装饰器名，必须写在被装饰对象的正上方，并且是单独一行
import time

def timmer(func):
    # func=index
    def wrapper():
        start=time.time()
        func()
        stop=time.time()
        print('run time is %s' %(stop-start))
    return wrapper


@timmer # index=timmer(index)
def index():
    time.sleep(3)
    print('welcome to index')
@timmer # home=timmer(home)
def home():
    time.sleep(2)
    print('welcome to home page')

index()
home()