from multiprocessing import Process,Queue
import time,os
def producer(q):
    for i in range(10):
        time.sleep(1)
        res='包子%s'%i
        q.put('<%s>生产了<>%s'%(os.getpid(),res))

def consumer(q):
    while True:
        res = q.get()
        time.sleep(1)

if __name__ == '__main__':
    q=Queue()
    