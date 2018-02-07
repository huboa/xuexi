import subprocess
subprocess.call(["ls","-l"])
# subprocess.call(["ifconfig"])
subprocess.call(["ifconfig","en0"])
subprocess.call(["ssh","root@192.168.56.152"])