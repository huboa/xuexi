import sys,time
#
# for i in range(1,10):
#     sys.stdout.write('\r%s' %('#'*i))
#     sys.stdout.flush()
#     time.sleep(0.5)
#
# for i in range(1,10):
#     print('\r%s' %('#'*i),file=sys.stdout,flush=True,end='')
#     time.sleep(0.5)

#
# for i in range(1,100):
#     print('\r%s' %('#'*i),flush=True,end='')
#     time.sleep(0.5)
#
#
###进度条：
width=30
print('<%-10s>' %'hello ')
print(('<%%-%ds>' %width) %('hello'))
def progress(percent,width=50):
    show_str=('[%%-%ds]' %width) %(int(width*percent/100)*'#')
    print('\r%s %d%%' %(show_str),flush=True,end='')

totol_size=10241
recv_size=0
while recv_size < totol_size:
    time.sleep(0.01)###模拟下载网络延迟
    recv_size+=1024
    recv_per=int(100*recv_size/totol_size)