import time

def timmer(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        res=func(*args,**kwargs)

        stop=time.time()
        print('run time is %s' %(stop-start))
        return res
    return wrapper


@timmer # index=timmer(index)
def index():
    time.sleep(3)
    print('welcome to index')
    return 123

@timmer # home=timmer(home)
def home(name):
    time.sleep(2)
    print('welcome %s to home page' %name)

# res=index() #res=wrapper()
# print(res)

res1=home('egon') #wrapper('egon')
print(res1)