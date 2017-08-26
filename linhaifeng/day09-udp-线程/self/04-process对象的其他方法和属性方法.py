from multiprocessing import Process
import time,os

class MyProcess(Process):

    def __init__(self,name):
        super().__init__()
        self.name=name


def work(name):

    print('task %s is running' %name)
    time.sleep(2)
    print('task %s is done' % name)

if __name__ == '__main__':
    p1=Process(target=work,args=('egon',))

    # p=Process(target=work,kwargs={'name':'zsc'})

    p1.start()
    p1.terminate()  ###
    time.sleep(3)
    print(p1.is_alive())  ####存活
    print(p1.name)
    print(p1.pid)
    print('主pid',os.gepid)

    print('主')