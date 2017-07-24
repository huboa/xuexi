#_*_coding:utf-8_*_
__author__ = 'zzz'

import time
def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
       baozi = yield

       print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子!")
        c.send(i)  ###___next__() 可以传递参数
        c2.send(i)

producer("zsc")

# 通过生成器实现协程并行运算