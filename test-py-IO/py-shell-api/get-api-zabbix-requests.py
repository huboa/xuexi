import requests
import json
# url = "https://api.github.com/search/repositories?q=language:python&sort=starts"
# r=requests.get(url)
# print("Status code:",r.status_code,)
# response_dic =r.json()
#
# print(response_dic.keys)
# print(response_dic["total_count"])


####测试zabbix-获取认证token
# class Zabbix(object):
#     def __init__(self,hostname,user,password):
#         self.hostname =hostname
#         self.user= user
#         self.password=password


def zabbix_api():
    url = "http://10.199.89.13/api_jsonrpc.php"
    headers =  {"Content-type": "application/json"}
    data={"jsonrpc":"2.0",
          "method":"user.login",
          "params":{"user":"admin",
                    "password":"zabbix",
                    },
          # "auth":"null",
          "id":0
          }
    req=requests.post(url=url,headers=headers,data=json.dumps(data))
    req_dic = json.loads(req.text)

    print(type(req_dic),req_dic["result"])

    zabbix_token = req_dic["result"]
    # print(json.loads(requests_josn))

    ####获取主机列表
    data = {
        "jsonrpc": "2.0",
        "method": "host.get",
        "params": {
            "output": [
                "hostid",
                "host"
            ],
            "selectInterfaces": [
                "interfaceid",
                "ip"
            ]
        },
        "id": 0,
        "auth": zabbix_token
    }

    req=requests.post(url=url,headers=headers,data=json.dumps(data))
    req_dic = json.loads(req.text)
    for n in req_dic["result"]:
        print(n)
###执行函数
zabbix_api()