from stark.service import v1
from django.conf.urls import url
from app01 import models
from django.shortcuts import HttpResponse,render,redirect
from django.utils.safestring import mark_safe
from django.urls import reverse
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

from django.forms import ModelForm
from django.forms import fields

"""
stark/app01/userinfo/,     先找自己的changelist_view,没有就找基类
stark/app01/userinfo/add/,  先找自己的add_view,没有就找基类
stark/app01/userinfo/1/change/,  先找自己的change_view,没有就找基类
stark/app01/userinfo/1/delete/,  先找自己的delete_view,没有就找基类
    
"""
class UserInfoConfig(v1.StarkConfig):

    def xxxx(self,is_header=False,row=None):
        if is_header:
            return '表头'

        return "%s-%s" %(row.name,row.email)

    def display_gender(self,is_header=False,row=None):
        if is_header:
            return '性别'
        # if row.gender == 1:
        #     return '男'
        # else:
        #     return '女'
        return row.get_gender_display()

    def display_status(self,is_header=False,row=None):
        if is_header:
            return '状态'
        return row.get_status_display()

    def display_dp(self,is_header=False,row=None):
        if is_header:
            return '部门'
        return row.dp.title

    list_display = ['id', 'name', 'email',display_dp,display_gender,display_status, xxxx]


v1.site.register(models.UserInfo,UserInfoConfig)


class RoleConfig(v1.StarkConfig):
    list_display = ['id','title']

v1.site.register(models.Role,RoleConfig)


class GroupConfig(v1.StarkConfig):
    list_display = ['title']

v1.site.register(models.Group,GroupConfig)