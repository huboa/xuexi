from multiprocessing import Process,Lock
import time,os
def work(name,*args,**kwargs):
    mutex.acquire()
    print('%s%stask %s is running' %(os.getpid(),os.getppid(),name))
    time.sleep(2)
    print('%s%stask %s is done' %(os.getpid(),os.getppid(),name))
    mutex.release()
if __name__ == '__main__':
    mutex=Lock()
    p=Process(target=work,args=('egon',mutex))
    # p=Process(target=work,kwargs={'name':'zsc'})
    p.start()
    p1=Process(target=work, args=('zsc',mutex))
    p1.start()
    print('主')