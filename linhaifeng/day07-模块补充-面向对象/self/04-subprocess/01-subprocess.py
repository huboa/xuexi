import subprocess
res=subprocess.Popen('cat /Users/ZSC/scripts/remote.sh',
                     shell=True,stdout=subprocess.PIPE)
print(res.stdout.read().decode('utf-8'))
res=subprocess.Popen('cat1 /Users/ZSC/scripts/remote.sh',
                     shell=True,
                     stdout=subprocess.PIPE,
                     sterr=subprocess.PIPE)
#print(res.stdout.read().decode('utf-8'))
print(res.stderr.read().decode('utf-8'))