class Foo:
    def __init__(self,x):
        self.x=x

    def __del__(self):    ###在对象资源被释放的时候触发
        print('del-------')
        print(self)

f=Foo(100)
del f
print('===========》')