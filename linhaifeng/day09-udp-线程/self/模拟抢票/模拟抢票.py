import json,os,time
from multiprocessing import Process,Lock
def search():
    dic=json.load(open('db.txt'))
    print('%s看到票数%s'%(os.getpid(),dic['count']))

def get_ticket():
    dic =json.load(open('db.txt'))
    time.sleep(0.5) ##模拟读取数据库网络延迟
    if dic['count'] >0:
        dic['count']-=1
        time.sleep(0.5)  ##模拟写数据库网络延时
        json.dump(dic,open('db.txt','w'))

        print('购票成功%s' %os.getpid())
def task(mutex):
    search()
    mutex.acquire()
    get_ticket()
    mutex.release()

if __name__ == '__main__':
    mutex=Lock()
    for i in range(10):
        p=Process(target=task,args=(mutex,))
        p.start()

    #