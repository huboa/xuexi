
#可以执行系统命令
import subprocess
import shlex
###subprocess.call
#linux_command
# subprocess.call(["ifconfig"])
# subprocess.call(["ifconfig","en0"])
# subprocess.call(["ls","-l"])

# command_line='ipconfig -a'
# args=shlex.split(command_line)
# subprocess.call(args)
# print("================")
# subprocess.call(args)
# out_bytes = subprocess.check_output(args)
# print(out_bytes.decode(encoding="utf-8"))


###windows

# re=subprocess.call(["ipconfig"])
# subprocess.call(["ipconfig","-a"])
# out_bytes = subprocess.check_output(["ipconfig"],)
# print(out_bytes.decode(encoding='gbk'))




##########subprocess.Popen##执行怀命令
##windows
command_line='ssh admin@10.199.104.63'
args=shlex.split(command_line)

re=subprocess.Popen(args,
                    shell=True,
                    stdout=subprocess.PIPE,
                    stderr=subprocess.PIPE)
print("==========>",re.stdout.read().decode("gbk"))
print("==========>",re.stderr.read().decode("gbk"))
print("==========>",re.stderr.read().decode("gbk"))

###下面是stdin 从stdout 获取

# res1=subprocess.Popen(r'dir',
#                      shell=True,
#                      stdout=subprocess.PIPE,)
#
# # stdin=res1.stout
# res2=subprocess.Popen(r'findstr xml$',
#                      shell=True,
#                      stdin=res1.stdout,
#                      stdout=subprocess.PIPE,)


# print(res2.stdout.read().decode('gbk'))

##linux







import pexpect
####捕获执行
# pexpect.spawn