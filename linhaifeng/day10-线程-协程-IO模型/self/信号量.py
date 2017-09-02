from threading import Thread,current_thread,Semaphore
import time,random
sm=Semaphore
def work()