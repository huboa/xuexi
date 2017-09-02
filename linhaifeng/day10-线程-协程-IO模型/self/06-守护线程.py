from multiprocessing  import Process
import time
def task():
    print('123')
    time.sleep(2)
    print('123done')

if __name__ == "__main__":
    p=Process(target=task)
    p.daemon=True
    p.start()
    print('主')
    