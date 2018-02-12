import  requests
import json

#http://lf-zb-rundeck.wandafilm.com/project/Oam-system/job/show/21274346-3898-40a4-bb0a-c3ef257bae9f
server_name='lf-zb-rundeck.wandafilm.com'
job_id='21274346-3898-40a4-bb0a-c3ef257bae9f'
api_token='N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG'
projects = 'projects'

def rundeck(server=None,version=None,item=None,job_id=None,job_ex=None,api_token=None,**kwargs):

    if server == None:
        return "server can not null"
    if version == None:
        return "version can not null"
    if item == None:
        return "item can not null"
    if api_token == None:
        return "api_token can not null"
    if job_id == None:
        job_id=''
    else:
        job_id=(job_id+"/")
    if job_ex == None:
        job_ex = ''

    # http://lf-zb-rundeck.wandafilm.com/api/18/job/21274346-3898-40a4-bb0a-c3ef257bae9f/info?authtoken=N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG
    url=("http://%s/api/%s/%s/%s%s?authtoken=%s"%(server,version,item,job_id,job_ex,api_token))
    headers = {"Accept":"application/json"}
    print(url)
    # try :
    #     req=requests.get(url=url,headers=headers)
    #     req_dict=json.loads(req.text)
    # except:
    #     return
    req = requests.get(url=url,)
    # req_dict = json.loads(req.text)
    return req.text


# ##查看token信息 ##可以在ｗｅｂ界面查看
# req=rundeck(server=server_name,version=version,item='tokens',api_token=api_token,)
# print(req)

##查看系统信息
# req=rundeck(server=server_name,version=version,item='system/info',api_token=api_token,)
# print(req)


##查看项目信息,list-所有job
# req=rundeck(server=server_name,version=version,item='projects',api_token=api_token,)
# # print(req)
# for n in req:
#     print(n['name'],n['url'],n['description'])
#     item='project'+'/'+n['name']+"/jobs"
#     req=rundeck(server=server_name,version=version,item=item,api_token=api_token,)
#     for n in req:
#         print(n['id'],n['href'],n['permalink'],n['name'],)

##查看单个job 信息,运行job
req=rundeck(server=server_name,version="13",item='job',job_id=job_id,job_ex='run',api_token=api_token)
# print(req,req['project'])
# print(req['system']['timestamp'])
print(req)

# req=rundeck(server=server_name,version=version,item='job',job_id=job_id,job_ex='run',api_token=api_token)
# print(req)