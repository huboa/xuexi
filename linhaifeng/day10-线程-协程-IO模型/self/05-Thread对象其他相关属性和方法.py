from threading import Thread,active_count,enumerate,current_thread
# from multiprocessing import Process
import time

def task():
    print('is running')
    time(2)
if __name__ == '__main__':
    t=Thread(target=task,)
    # t=Process(target=task,)
    t.start()
    t.join()
    print(t.is_alive())
    print(t.getName())
    print('主')
    print(active_count())
    # print(enumerate())