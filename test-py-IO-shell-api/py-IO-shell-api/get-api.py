import requests
import json
url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
r=requests.get(url)
print("Status code:",r.status_code,)
response_dic =r.json()

print(response_dic.keys())