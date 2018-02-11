import  requests
import json

#http://lf-zb-rundeck.wandafilm.com/project/Oam-system/job/show/21274346-3898-40a4-bb0a-c3ef257bae9f
server_name='lf-zb-rundeck.wandafilm.com'
job_id='21274346-3898-40a4-bb0a-c3ef257bae9f'
api_token='N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG'
version="12"
# file='system/info'
projects='projects'
file="/job/"+job_id

###查看项目
# url=("http://%s/api/%s/%s?authtoken=%s"%(server_name,version,projects,api_token))
#
# headers = {"Accept":"application/json"}
# print(url)
# req=requests.get(url=url,headers=headers)
# # req=requests.get(url=url)
# req_dict=json.loads(req.text)
#
# for n in req_dict:
#     print(n['url'],type(n))

#####runjob 运行job

url=("http://%s/api/%s%s/run?authtoken=%s"%(server_name,version,file,api_token))
# headers = {"Accept":"application/json"}
print(url)
req=requests.get(url=url,)
print(req,req.text,type(req.text))
# req_dict=json.loads(req.text)
# for n in req_dict:
#     print(n,type(n))