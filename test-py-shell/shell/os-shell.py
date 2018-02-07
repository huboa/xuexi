import subprocess

# subprocess.call(["ifconfig"])
subprocess.call(["ifconfig","en0"])
subprocess.call(["ls","-l"])


subprocess.call(["ssh","root@192.168.56.202","ip","a"],)
print("================")
subprocess.call(["ssh","root@192.168.56.202","ip","a"],)
subprocess.call(["ip","a"],)

# (status,output)=subprocess.getstatusoutput(["ssh","root@192.168.56.202","ip","a"],)
# print(status,output)