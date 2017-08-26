import requests ###pip3 install requests
respone=requests.get('https://www.baidu.com')
print(respone.status_code)