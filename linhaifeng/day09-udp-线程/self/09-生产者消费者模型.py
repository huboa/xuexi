from multiprocessing import Process,Queue
import time,os
def producer(q):
    for i in range(10):
        time.sleep(1)
        res='包子%s'%i
        q.put(res)
        print('\33[45m<%s> 生产[%s]\033[20m' % (os.getpid(), res))
def consumer(q):
    while True:
        res = q.get()
        time.sleep(1.5)
        print('\033[34m<%s> 吃了[%s]\033[0m'%(os.getpid(),res))

if __name__ == '__main__':
    q=Queue()
    p1=Process(target=producer,args=(q,))
    c1=Process(target=consumer,args=(q,))
    p1.start()
    c1.start()
    print('主')
