import subprocess

# subprocess.call(["ifconfig"])
subprocess.call(["ifconfig","en0"])
subprocess.call(["ls","-l"])


subprocess.call(["ssh","root@192.168.56.202","ip","a"],)
print("================")
subprocess.getoutput(["ssh","root@192.168.56.202","ip","a"],)
