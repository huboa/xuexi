print("加载stark文件")


from stark.service import v1
from rbac import models
from app01 import models as amodels
from django.shortcuts import HttpResponse,render
from django.conf.urls import url
##注册说明
# 将models中的UserInfo类注册到【某个地方】
"""
_registry = {
    models.UserInfo: StarkConfig(models.UserInfo),
    models.Role: StarkConfig(models.Role),
}

/stark/app01/userinfo/，执行 StarkConfig(models.UserInfo).changelist_view()
/stark/app01/userinfo/add/，执行 StarkConfig(models.UserInfo).add_view()


/stark/app01/role/，执行 StarkConfig(models.Role).changelist_view()
/stark/app01/role/add/，执行 StarkConfig(models.Role).add_view()




for k,v in _registry.items():
    print(v.mcls)

"""

####劫持说明
"""
_registry = {
    models.UserInfo: UserInfoConfig(models.UserInfo),
    models.Role: StarkConfig(models.UserInfo),
    models.Group: StarkConfig(models.UserInfo),
}

/stark/app01/userinfo/，执行 UserInfoConfig(models.UserInfo).changelist_view()
/stark/app01/userinfo/add/，执行 UserInfoConfig(models.UserInfo).add_view()


/stark/app01/role/，执行 StarkConfig(models.Role).changelist_view()
/stark/app01/role/add/，执行 StarkConfig(models.Role).add_view()



"""


####劫持类
class UserInfoConfig(v1.StarkConfig):
    def changelist_view(self,request):
        print("劫持页面")
        return HttpResponse("特殊页面劫持")
    def extra_url(self):
        patterns=[
            url(r'^xx$', self.xx),
            url(r'^xxxx/$', self.xxxx),
        ]
        return patterns
    def xxxx(self,request):
        return HttpResponse("xxxx劫持或添加")
    def xx(self,request):
        return HttpResponse("xx劫持或添加")



# #注册mode表 待生成url
v1.site.registry(models.UserInfo,UserInfoConfig)
v1.site.registry(models.Role)
v1.site.registry(amodels.Host)

