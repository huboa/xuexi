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
from utils.server_hardware_info import connect_obj

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


####用户表单form 表单
class UserInfoModelForm(ModelForm):
    xx = fields.CharField()
    class Meta:
        model = models.UserInfo
        fields = "__all__"

###主机表单表单form 表单
class HostModelForm(ModelForm):
        class Meta:
            model = amodels.Host
            fields = "__all__"
            # fields = ["idc", "remoteip", "host_ip"]
            required = True
            labels = {
                "sn": "主机SN号",
                "remoteip": "带外IP",
                'host_ip': '主机IP',
            }
            error_messages = {
                "idc": {
                    "required": "不能为空"
                },
                "sn": {
                    "required": "不能为空"
                },
                "remoteip": {
                    "required": "不能为空"
                }
            }

##用户类#角色类劫持角色配置类
class UserInfoConfig(v1.StarkConfig):   ####可以劫持父类 中的 任何数据 只要添加

    def logout_url(self,is_header=False,row=None):   ###添加显示字段
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
    list_display = ['id', 'username',display_gender,display_status,display_dp,logout_url]
    search_list = ["username__contains",]
    comb_filter = ['gender','status','dp']
    model_form_cls = UserInfoModelForm  ####劫持form 表单
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


###IDC 中心 机柜位c 配置 物理机配置

class HostConfig(v1.StarkConfig):
    ####批量执行功能函数视图
    def pk_del(self, request, action):
        pk_list = request.POST.getlist("pk")
        print(pk_list, "批量删除")
        for n in pk_list:
            amodels.Host.objects.filter(id=n).delete()
            print(n, "批量删除")
    def pk_update(self, request, action):
        pk_list = request.POST.getlist("pk")
        print(pk_list, "批量更新")
        for nid in pk_list:
            self.updatefunc(request,nid)



    def update_url(self, is_header=False, row=None):  ###添加显示字段
        if is_header:
            return '更新主'
        return mark_safe('<a href=/stark/app01/host/%s/updateinfo/>更新</a> ' % (row.id))

    list_display = ['id', 'idc','sn','hostname','host_ip',"Hosys","Hcore",'manufacturer','product_name',"Hcpu","Hmemory","Hdisk",'remoteip',"HotherIp","Hother",update_url]
    search_list = ["sn__contains", 'remoteip__contains','hostname__contains','manufacturer__contains','product_name__contains',"host_ip__contains","Hosys__contains"]
    ####批量执行清单
    action_list = [{"name":"批量删除","func_name":"pk_del"},{"name":"批量更新","func_name":"pk_update"}]
    model_form_cls = HostModelForm ####劫持form 表单


    def extra_url(self):  #######钩子函数配了 会劫持 扩展url
        patterns = [
            url(r'^(\d+)/updateinfo/$', self.updatefunc),
        ]
        return patterns

    def updatefunc(self,request,nid):
        # print(nid, "更新主机信息")
        host=amodels.Host.objects.get(id=nid)
        sys_info_dict = connect_obj.get_sys_info(user='root',host=host.host_ip,)
        sys_os_info_dict = connect_obj.get_os_info(user='root',host=host.host_ip,)
        if sys_info_dict:
            host.manufacturer=sys_info_dict['Manufacturer']
            host.sn=sys_info_dict['Serial Number']
            host.product_name=sys_info_dict['Product Name']
            host.Hmemory=sys_info_dict["mem_info"]
            host.Hcpu = sys_info_dict["cpu_info"]
            host.save()
        if sys_os_info_dict:
            host.Hdisk = sys_os_info_dict["disk_info"]
            host.hostname = sys_os_info_dict["hostname"]
            host.Hosys = sys_os_info_dict["os_info"]
            host.Hcore = sys_os_info_dict["core_info"]
            host.save()
        return redirect(self.get_list_url())

###权限类
class PermissionsConfig(v1.StarkConfig):
    list_display = ['id','title','url','code','group','gmid']
    search_list = ["title__contains",'url__contains', 'code__contains',]
class PermissionGroupConfig(v1.StarkConfig):
    list_display = ['id','name','menu']



 #注册mode表 待生成url
v1.site.registry(models.UserInfo,UserInfoConfig)
v1.site.registry(models.Role)
v1.site.registry(models.Ldap)

v1.site.registry(models.Permissions,PermissionsConfig)
v1.site.registry(models.PermissionGroup,PermissionGroupConfig)
v1.site.registry(models.Menu)

v1.site.registry(amodels.IDC)
v1.site.registry(amodels.Cabinet)
v1.site.registry(amodels.Host,HostConfig)
v1.site.registry(amodels.Vhost)

v1.site.registry(amodels.Zabbix)
v1.site.registry(amodels.ZabbixTemplate)

