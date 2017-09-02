from threading import Thread
from multiprocessing import Process
import time

def task():
    print('is running')
if __name__ == '__main__':
    t=Thread(target=task,)
    t=Process(target=task,)
    t.start()
    print('主')

###方式一
def sayhi(name):
    time.sleep(2)
    print('%s say hello' %name)

if __name__ == '__main__':
    t=Thread(target=sayhi,args=('egon',))
    t.start()
    print('主线程')

# 方式二


class Sayhi(Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        time.sleep(2)
        print('%s say hello' % self.name)


if __name__ == '__main__':
    t = Sayhi('egon')
    t.start()
    print('主线程')
