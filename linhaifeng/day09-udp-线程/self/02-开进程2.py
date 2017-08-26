from multiprocessing import Process
import time

class MyProcess(Process):

    def __init__(self,name):
        super().__init__()
        self.name=name


def work(name):
    print('task %s is running' %name)
    time.sleep(2)
    print('task %s is done' % name)

if __name__ == '__main__':
    p=Process(target=work,args=('egon',))
    # p=Process(target=work,kwargs={'name':'zsc'})
    p.start()
    p1=Process(target=work, args=('zsc',))
    p1.start()
    print('主')