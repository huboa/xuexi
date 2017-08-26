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
    p1=Process(target=work,args=('egon',))
    p2=Process(target=work, args=('zsc',))
    p3 = Process(target=work, args=('zxx',))
    # p=Process(target=work,kwargs={'name':'zsc'})

    # p1.start()
    # p2.start()
    # p3.start()
    # p1.join() ##主进程等，等待p1运行结束
    # p2.join()  ##主进程等，等待p2运行结束
    # p3.join()
###循环写法 
    p_l=[p1,p2,p3]
    for p in p_l:
        p.start()

    for p in p_l:
        p.join()

    print('主')