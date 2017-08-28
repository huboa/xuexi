import requests ###pip3 install requests
import os
def get_page(url):
    print('<%s> get:%s'%(os.getpid(),url))
    respone = requests.get(url)
    if respone.status_code ==200:
        return {'url':url,'test':respone.text}


if __name__ == '__main__':
    p=Pool(4)
urls=[]

r
print(respone.status_code)

