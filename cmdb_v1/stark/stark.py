print("加载stark文件")

from stark.service import v1
from rbac import models
from app01 import models as amodels
from django.shortcuts import HttpResponse,render,redirect
from django.conf.urls import url
from django.forms import ModelForm
from django.forms import fields
from django.utils.safestring import mark_safe
from django.urls import reverse
from rbac.service.init_permissions import reset_permission

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


####form 表单
class UserInfoModelForm(ModelForm):
    xx = fields.CharField()
    class Meta:
        model = models.UserInfo
        fields = "__all__"

class UserInfoConfig(v1.StarkConfig):   ####可以劫持父类 中的 任何数据 只要添加

    def logout_html(self,is_header=False,row=None):   ###添加显示字段
        if is_header:
            return '注销'
        return  mark_safe('<a href=/stark/rbac/userinfo/%s/logout/>注销</a> '%(row.id))

    def display_gender(self, is_header=False, row=None):
        if is_header:
            return '性别'
        # if row.gender == 1:
        #     return '男'
        # else:
        #     return '女'
        return row.get_gender_display()

    def display_status(self, is_header=False, row=None):
        if is_header:
            return '状态'
        return row.get_status_display()

    def display_dp(self, is_header=False, row=None):
        if is_header:
            return '部门'
        return row.dp.title

####显示列表可以添加函数数据库字段和
    list_display = ['id', 'username',display_gender,display_status,display_dp,logout_html]
    search_list = ["username__contains",]
    comb_filter = ['gender','status','dp']

    # def changelist_view(self,request):
    #     print("劫持页面")
    #     return HttpResponse("特殊页面劫持")
    def extra_url(self):  #######钩子函数配了 会劫持 扩展url 用
        patterns=[
            url(r'^xx$', self.xx),
            url(r'^(\d+)/logout/$', self.logout),
        ]
        return patterns

    ####注销函数
    def logout(self,request,pk):
        user_obj = self.model_class.objects.filter(id=pk).first()
        if user_obj.session_key:
            reset_permission(user_obj,request)
        else:
            user_obj.session_key = None
            user_obj.status = 2
            user_obj.save()
        return redirect(self.get_list_url())

    def xx(self,request):
        return HttpResponse("xx劫持或添加")


    model_form_cls = UserInfoModelForm  ####劫持form 表单


####劫持角色配置类
class RoleConfig(v1.StarkConfig):
    list_display = ['id', 'title']
####主机配置类
class HostConfig(v1.StarkConfig):
    ####批量执行功能函数视图
    def pk_test(self, request, action):
        pk_list = request.POST.getlist("pk")
        print(pk_list, "测试")

    def pk_test1(self, request, action):
        pk_list = request.POST.getlist("pk")
        print(pk_list, "测试2")

    list_display = ['id', 'idc','sn','remoteip','hostname','host_ip','manufacturer','product_name']
    search_list = ["sn__contains", 'remoteip__contains']
    action_list = [{"name":"测试1","func_name":"pk_test"},{"name":"测试2","func_name":"pk_test1"}]

###权限类
class PermissionsConfig(v1.StarkConfig):
    list_display = ['id','title','url','code','group','gmid']
class PermissionGroupConfig(v1.StarkConfig):
    list_display = ['id','name','menu']

###菜单
class MenuConfig(v1.StarkConfig):
    list_display = ['id','name']

 #注册mode表 待生成url

v1.site.registry(models.UserInfo,UserInfoConfig)
v1.site.registry(models.Role,RoleConfig)

v1.site.registry(models.Permissions,PermissionsConfig)
v1.site.registry(models.PermissionGroup,PermissionGroupConfig)
v1.site.registry(models.Menu,MenuConfig)

v1.site.registry(amodels.Host,HostConfig)

