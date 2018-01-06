###死锁现象
from threading import Thread,Lock,RLock
import time
mutexA=Lock()
mutexB=Lock()
class Mythread(Thread):
    def run(self):
        self.f1()
        self.f2()
    def f1(self):
        mutexA.acquire()
        print("")