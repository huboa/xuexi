import sys

#python3 copy.py source.file target.file
if len(sys.argv) < 3:
    print('Usage:python3 copy.py source.file target.file')
    sys.exit()

#r'C:\Users\Administrator\PycharmProjects\python18期周末班\day3\test.jpg'
with open(r'%s' %sys.argv[1],'rb') as read_f,\
        open(r'%s' %sys.argv[2],'wb') as write_f:

    for line in read_f:
        write_f.write(line)