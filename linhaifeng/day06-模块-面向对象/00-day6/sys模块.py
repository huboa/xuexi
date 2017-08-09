import sys,time

# for i in range(1,100):
#     sys.stdout.write('\r%s' %('#'*i))
#     sys.stdout.flush()
#     time.sleep(0.5)


# for i in range(1,100):
#     print('\r%s' %('#'*i),file=sys.stdout,flush=True,end='')
#     time.sleep(0.01)


#进度条：

# print('<%s>' %'hello')
# print('<%-10s>' %'hello')
# print('<%-10s>' %'helloe')
# print('<%-10s>' %'helloee')
#
# print('<%-10s>' %'#')
# print('<%-10s>' %'##')
# print('<%-10s>' %'###')
# print('<%-10s>' %'####')
# print('<%-10s>' %'#####')


# print('<%-10s>' %'helloee')

# width=20
# print('<%%-%ds>' %width) #<%-10s>

# print(('<%%-%ds>' %width) %('hello'))
# <%-10s> %('hello')






# width=20
#
# print(('[%%-%ds]' %width) %('#'))
# print(('[%%-%ds]' %width) %('##'))
# print(('[%%-%ds]' %width) %('###'))







def progress(percent,width=50): #51
    if percent >= 100:
        # print('\r[%s] 100%%' %(width*'#'))
        percent=100
    show_str=('[%%-%ds]' %width) %(int(width*percent/100)*'#')
    print('\r%s %d%%' %(show_str,percent),file=sys.stdout,flush=True,end='')
#
total_size=1025121
recv_size=0

while recv_size < total_size:
    time.sleep(0.01) #模拟下载的网络延迟
    recv_size+=1024
    recv_per=int(100*recv_size/total_size)
    progress(recv_per,width=10)





