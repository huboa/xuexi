from multiprocessing import process
import time
def work(name):
    print('task %s is running' %name)
    time.sleep(2)
    print('task %s is done' % name)

if __name__ == '__main__':
    # p=process(target=work,args=('egon',))
    process(target=work,kwargs={'name':'zsc'})
    # p.start()
    print('主')