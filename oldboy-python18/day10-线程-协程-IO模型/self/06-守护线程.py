from multiprocessing  import Process
from threading import Thread
import time
###守护进程
# def task():
#     print('123')
#     time.sleep(2)
#     print('123done')
#
# def task2():
#     print('456')
#     time.sleep(5)
#     print('456done')
#
#
# if __name__ == "__main__":
#     p=Process(target=task)
#     p2=Process(task2())
#     p.daemon=True  ###守护进程开启就忽略
#     p.start()
#     p2.start()
#     print('主')

###守护线程
def task():
    print('123')
    time.sleep(9)
    print('123done')

def task2():
    print('456')
    time.sleep(5)
    print('456done')


if __name__ == "__main__":
    t=Thread(target=task)
    t2=Thread(target=task2)
    t.daemon=True  ###守护线程
    t.start()
    t2.start()
    print('主')