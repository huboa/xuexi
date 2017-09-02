from threading import Thread
def task():
    print('is running')
if __name__ == '__main__':
    t=Thread(target=task,)
    t.start()
    print('主')