from threading import Thread

msg_l=[]
format_l=[]
def talk():
    while True:
        msg=input('>>:').strip()
        msg_l.append(msg)
def format():
    while True:
        if  msg_l:
            data=msg_l.pop()
            format_l.append(data.upper())
def save():
    while True:
        if  format_l:
            data=format_l.pop()
            with open('db.txt','a') as f:
                f.write('%s\n'%data)


if __name__ == '__main__':
    t1=Thread(target=talk)
    t2=Thread(target=format)
    t3=Thread(target=save)

    t1.start()
    t2.start()
    t3.start()