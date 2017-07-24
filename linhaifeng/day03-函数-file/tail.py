#python3 tail.py -f access.log

import time
import sys
with open(r'%s' % sys.argv[2],'rb') as f:
    f.seek(0,2)
    while True:
        line = f.readline()
        if line:
            print(line.decode('utf-8'))
    #        print(line.decode('utf-8'), end='')
        else:
            time.sleep(0.2)