import subprocess
res=subprocess.Popen('cat /Users/ZSC/scripts/remote.sh',
                     shell=True,stdout=subprocess.PIPE)
print(res.stdout.read().decode('utf-8'))