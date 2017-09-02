from threading import Thread,current_thread,Semaphore
import time,random
sm=Semaphore(5)
def work():
    sm.acquire()
    print('%s 工作'%current_thread().getName())
    time.sleep(random.randint(1,3))
    sm.release()
if __name__ == '__main__':
    for i in range(20):
        t=Thread(target=work())
        t.start()