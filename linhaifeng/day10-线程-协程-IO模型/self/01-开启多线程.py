from threading import Thread
from multiprocessing import Process

def task():
    print('is running')
if __name__ == '__main__':
    t=Thread(target=task,)
    t=Process(target=task,)
    t.start()
    print('主')

class MyThread(Thread):
    def run(self):
        print('is running')

