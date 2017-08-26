import json,os,time
def search():
    dic=json.load(open('db.txt'))
    print('%s票数%s'%(os.getpid(),dic[count]))

def get_ticket():
    dic =json.load(open('db.txt'))
    time.sleep(0.5) ##模拟读取数据库网络延迟
    if dic['count'] >0:
        dic['count']-=1
        json.dump(dic,open('db.txt','w'))
        time.sleep(0.5) ##模拟写数据库网络延时
        print('')
def task():
    search()
    #