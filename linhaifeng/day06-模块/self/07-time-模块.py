import time
# print(time.time()) ##时间戳
# print(time.strftime('%Y-%m-%d %X'))
#
# print(time.localtime()) ##本地时间
# print(time.gmtime()) #UTC
# print(time.gmtime().tm_mon)
#
# print(time.localtime(1212121212))
# print(time.gmtime(1212121212))
#
#
# print(time.mktime(time.localtime()))
# print(time.strftime('%Y',time.gmtime()))
#
# # print(time.strptime('2017-03-01','%Y-m-%d'))

print(time.ctime(1212141))
print(time.asctime(time.gmtime()))