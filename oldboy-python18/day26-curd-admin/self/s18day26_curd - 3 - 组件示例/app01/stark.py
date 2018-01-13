from stark.service import v1
from django.conf.urls import url
from app01 import models
from django.shortcuts import HttpResponse,render

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

class UserInfoConfig(v1.StarkConfig):

    def extra_url(self):
        patterns = [
            url(r'^xxxxxx/$', self.xxxxxx),
        ]
        return patterns

    def xxxxxx(self,request):
        return HttpResponse('xxxxx')

    def changelist_view(self,request):
        return render(request,'userinfo_list.html')

v1.site.register(models.UserInfo,UserInfoConfig)


class RoleConfig(v1.StarkConfig):
    def extra_url(self):
        patterns = [
            url(r'^xxxxxx/$', self.xxxxxx),
        ]
        return patterns

    def xxxxxx(self,request):
        return HttpResponse('定制页面')

v1.site.register(models.Role,RoleConfig)


v1.site.register(models.Group)