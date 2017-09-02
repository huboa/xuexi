from threading import Thread,active_count
# from multiprocessing import Process
import time

def task():
    print('is running')
if __name__ == '__main__':
    t=Thread(target=task,)
    # t=Process(target=task,)
    t.start()
    t.join()
    print(t.is_alive())
    print(t.getName())
    print('主')