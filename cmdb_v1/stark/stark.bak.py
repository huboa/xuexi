print("加载stark文件")


from stark.service import v1
from rbac import models
from app01 import models as amodels
from django.shortcuts import HttpResponse,render
from django.conf.urls import url
from django.forms import ModelForm
from django.forms import fields
from django.utils.safestring import mark_safe
from django.urls import reverse
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


####劫持用户配置类
class UserInfoModelForm(ModelForm):
    xx = fields.CharField()
    class Meta:
        model = models.UserInfo
        fields = "__all__"

class UserInfoConfig(v1.StarkConfig):   ####可以劫持父类 中的 任何数据 只要添加

    def test(self,is_header=False,row=None):   ###添加显示字段
        if is_header:
            return '表头test'
        return  ('<a href=/stark/rbac/userinfo/%s/change/>编辑</a>  <a href=/stark/rbac/userinfo/%s/delete/>删除</a>'%(row.id,row.id))

####显示列表可以添加函数数据库字段和
    list_display = ['id', 'username',test]
    # def changelist_view(self,request):
    #     print("劫持页面")
    #     return HttpResponse("特殊页面劫持")
    def extra_url(self):  #######钩子函数配了 会劫持 扩展url 用
        patterns=[
            url(r'^xx$', self.xx),
            url(r'^xxxx/$', self.xxxx),
        ]
        return patterns
    def xxxx(self,request):
        return HttpResponse("xxxx劫持或添加")
    def xx(self,request):
        return HttpResponse("xx劫持或添加")

    # model_form_cls = UserInfoModelForm  ####劫持form 表单


####劫持角色配置类
class RoleConfig(v1.StarkConfig):
    list_display = ['id', 'title']
####主机配置类
class HostConfig(v1.StarkConfig):
    list_display = ['id', 'idc','sn','remoteip' ]
###权限类
class Permissions(v1.StarkConfig):
  list_display = ['id','title','url','code','group','gmid']

class PermissionGroup(v1.StarkConfig):
    list_display = ['id','title','menu']
# #注册mode表 待生成url
v1.site.registry(models.UserInfo,UserInfoConfig)
v1.site.registry(models.Role,RoleConfig)
v1.site.registry(amodels.Host,HostConfig)
v1.site.registry(models.Permissions,Permissions)
v1.site.registry(models.PermissionGroup,PermissionGroup)

