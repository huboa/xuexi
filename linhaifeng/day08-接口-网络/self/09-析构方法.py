class Foo:
    def __init__(self,x):
        self.x=x

    def __del__(self):
        print('del-------')

f=Foo(100)
print('===========')