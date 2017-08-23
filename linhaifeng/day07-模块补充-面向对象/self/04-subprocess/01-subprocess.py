import subprocess
###mac
# res=subprocess.Popen('cat /Users/ZSC/scripts/remote.sh',
#                      shell=True,stdout=subprocess.PIPE)
# print(res.stdout.read().decode('utf-8'))
# res=subprocess.Popen('cat11 /Users/ZSC/scripts/remote.sh',
#                      shell=True,
#                      stdout=subprocess.PIPE,
#                      sterr=subprocess.PIPE)
# #print(res.stdout.read().decode('utf-8'))
# print(res.stderr.read().decode('utf-8'))

# res=subprocess.Popen('cat11 /Users/ZSC/scripts/remote.sh',
#                      shell=True,
#                      stdout=subprocess.PIPE)
# res.stdout

###windows
# res=subprocess.Popen(r'dir D:\data\git\xuexi\linhaifeng\day07-模块补充-面向对象\self\04-subprocess',
#                      shell=True,stdout=subprocess.PIPE)
# print(res.stdout.read().decode('gbk'))

###区分错误正常输出 stdout,stderr
# res=subprocess.Popen(r'ipconfig',shell=True,
#                      stdout=subprocess.PIPE,
#                      stderr=subprocess.PIPE)
# print('stdout',res.stdout.read().decode('gbk'))
# print('stderr',res.stderr.read().decode('gbk'))


####模拟系统命令过滤后缀名.txt  stdout 输入到下一个 stdin
res=subprocess.Popen('dir',
                     shell=True,
                     stdout=subprocess.PIPE)
# print(res.stdout.read().decode('gbk'))

res1=subprocess.Popen(r'findstr txt$',
                      shell=True,
                      stdin=res.stdout,
                      stdout=subprocess.PIPE)
print(res1.stdout.read().decode('gbk'))