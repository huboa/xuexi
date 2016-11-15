import os
import sys
import datetime
import time
t=time.localtime()
print(t)
print(time.localtime())##本地时间
print(time.altzone/3600)
print(time.time()) ##时间戳
print(time.time()/(3600*12*365))
print(time.gmtime()) ##utc 时间
print(time.time()/((3600*24*365)+3600*24))

#转换字符串
print(time.strptime("2016-11-11 23:30","%Y-%m-%d %H:%M"))
#print(time.strptime(""))

#转换成时间戳
t2=time.strptime("2016-11-11 23:30","%Y-%m-%d %H:%M")
print(time.mktime(t2))

#转换成字符串
t2_stamp=time.mktime(t2)
t3 = time.localtime(t2_stamp)
t3_str =time.strftime("%Y_%m_%d %H_%M.log",t3)
print(t3_str)
#时间运算
print("datetime".center(60,"_"))
print(datetime.datetime.now()+ datetime.timedelta(days=3))
print(datetime.datetime.now()- datetime.timedelta(days=3))
print(datetime.datetime.now()- datetime.timedelta(hours=3))
print(datetime.datetime.now()- datetime.timedelta(minutes=3))
##时间替换
now =datetime.datetime.now()
print(now.replace(month=1,day=1))

print(os.listdir())