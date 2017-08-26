from multiprocessing import Pool
import os,time

def work(n):
    print('task %s is running' %os.getpid())
    time.sleep(2)
    print('task %s is done' %os.getpid())
    return n**2

if __name__ == '__main__':
    p=Pool(8)
###同步
# print(os.cpu_count())
#     for i in range(10):
#         res=p.apply(work,args=(i,))
#         print(res)

###异步
    res_list=[]
    for i in range(10):
            res=p.apply_async(work,args=(i,))
            res_list.append(res)
            print(res)
    p.close() ###不允许提交新任务
    p.join()

    for res in res_list:
        print(res.get())