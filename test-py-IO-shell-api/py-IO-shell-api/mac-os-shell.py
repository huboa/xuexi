

import subprocess
import pexpect

####mac
host = "192.168.86.130"

# subprocess.call(["ifconfig"])
subprocess.call(["ifconfig","en0"])
subprocess.call(["ls","-l"])


subprocess.call(["ssh","root@192.168.56.202","ip","a"],)
print("================")
subprocess.call(["ssh","root@192.168.56.202","ip","a"],)
out_bytes = subprocess.check_output(["ssh","root@192.168.56.202",'ip','a'])
print(out_bytes.decode(encoding="utf-8"))



####捕获执行
pexpect.spawn