from multiprocessing  import Process
import time
def task():
    print('123')
    time.sleep(2)
    print('123done')

def task2():
    print('456')
    time.sleep(5)
    print('456done')


if __name__ == "__main__":
    p=Process(target=task)
    p2=Process(task2())
    p.daemon=True  ###守护进程开启就忽略
    p.start()
    p2.start()
    print('主')
