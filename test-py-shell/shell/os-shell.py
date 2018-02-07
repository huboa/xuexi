import subprocess
import pexpect
# subprocess.call(["ifconfig"])
subprocess.call(["ifconfig","en0"])
subprocess.call(["ls","-l"])


subprocess.call(["ssh","root@192.168.56.202","ip","a"],)
print("================")
subprocess.call(["ssh","root@192.168.56.202","ip","a"],)
out_bytes = subprocess.check_output(["ssh","root@192.168.56.202",'ip','a'])
print(out_bytes)




pexpect.spawn