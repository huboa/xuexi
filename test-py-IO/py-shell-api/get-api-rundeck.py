import  requests
import json
import time

#http://lf-zb-rundeck.wandafilm.com/project/Oam-system/job/show/21274346-3898-40a4-bb0a-c3ef257bae9f
server_name='lf-zb-rundeck.wandafilm.com'
job_id='21274346-3898-40a4-bb0a-c3ef257bae9f'
api_token='N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG'
projects = 'projects'

def rundeck_request(url=None,method=None,data=None):


    if method == "get":
        headers = {"Accept":"application/json"}
        print(url)
        try :
            req=requests.get(url=url,headers=headers)
            req_dict=json.loads(req.text)
        except:
            return "get 错误"
    elif method == "post":
        headers = {"Content-type": "application/json","Accept":"application/json"}

        try:
            print(data,type(data))
            req = requests.post(url=url,headers=headers,data=data)

            req_dict = json.loads(req.text)
            return req_dict
        except:
            return "post 错误"


    else:
        return


def rundeck(server=None,version=None,item=None,job_id=None,job_ex=None,api_token=None,method=None,data=None,**kwargs):

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
        job_id=("/"+str(job_id)+"/")
    if job_ex == None:
        job_ex = ''

    if method == "get":
        data = ""
    elif method == "post":
        data = data
    else:
        return "method can not null"

    # http://lf-zb-rundeck.wandafilm.com/api/18/job/21274346-3898-40a4-bb0a-c3ef257bae9f/info?authtoken=N7TbMjcsoP5UTxcdb8UVaLYTTuDpKtFG
    url=("http://%s/api/%s/%s%s%s?authtoken=%s"%(server,version,item,job_id,job_ex,api_token,))

    return rundeck_request(url=url,method=method,data=data)


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

data={
    "options": {
        "op1":"value4",
    }
}

data_json = json.dumps(data)

req=rundeck(server=server_name,version="18",item='job',job_id=job_id,job_ex='run',api_token=api_token,method="post",data=data_json)
# print(req,req['project'])
# print(req['system']['timestamp'])
print(req['id'],req['href'])
# for n in req:
#     print(n)
# item='execution/'+str(req['id'])
time.sleep(5)
# execution=rundeck(server=server_name,version='18',item=item,api_token=api_token,method='get')
# print(execution)

# req=rundeck(server=server_name,version=version,item='job',job_id=job_id,job_ex='run',api_token=api_token)
# print(req)


####测试execution
url= req['href']+'/state?authtoken='+api_token
print(url)
req=requests.get(url)
print(req.text)