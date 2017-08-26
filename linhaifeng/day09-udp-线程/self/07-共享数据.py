from multiprocessing import Process,Manager,Lock


def task(dic,mutex):
    with mutex:
        dic['count']-=1
if __name__ == '__main__':
    mutex=Lock
    m=Manager()
    dic=m.dict({'count':100})
    p_l=[]
    for i in range(100):
        p=Process(target=task,args=(dic,mutex))
        p_l.append(p)
        p.start()
    for p in p_l:
        p.join()
    print(dic)