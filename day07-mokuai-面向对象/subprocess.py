import os
import sys
# import subprocess
import subprocess
print(os.system('whoami'))
# os.popen("pwd").read()##会保存执行的结果

# retcode = subprocess.call(["ls", "-l"])
# print(retcode)
subprocess.check_call(["ls", "-l"])