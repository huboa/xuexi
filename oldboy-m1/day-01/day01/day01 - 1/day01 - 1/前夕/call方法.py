class F4(object):
    def __init__(self):
        print('构造方法')

    def __call__(self, *args, **kwargs):
        print('f4')

obj = F4()

obj()