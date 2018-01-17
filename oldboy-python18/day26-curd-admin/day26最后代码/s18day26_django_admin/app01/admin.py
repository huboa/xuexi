from django.contrib import admin
from django.utils.safestring import mark_safe
from app01 import models

# 生成URL
# /admin//app01/department/           查看列表页面
# /admin/app01/department/add/        添加页面
# /admin/app01/department/1/change/   修改页面
# /admin/app01/department/1/delete/   删除页面
class DepartmentConfig(admin.ModelAdmin):
    list_display = ['title','code','xxxxxx','remove'] # 定制当前列表页面，显示那几列数据
    list_display_links = ['code']   # 定制每一个行数据，那个列表显示 a标签

    def xxxxxx(self,obj):
        return mark_safe("<a href='http://www.oldboyedu.com'>编辑</a>")

    def remove(self,obj):
        return '删除'

admin.site.register(models.Department,DepartmentConfig)


# 生成URL
# /admin//app01/userinfo/           查看列表页面
# /admin/app01/userinfo/add/        添加页面
# /admin/app01/userinfo/1/change/   修改页面
# /admin/app01/userinfo/1/delete/   删除页面
class UserInfoConfig(admin.ModelAdmin):
    list_display = ['name','email','dp']
    list_filter = ['dp']
    list_display_links = ['dp'] # 生成编辑标签
    list_editable = ['name','email'] # 变成input标签

    # sdf
    search_fields = ['name','email']

    save_on_top = True

    # 定制Action行为具体方法
    def func(self, request, queryset):
        # print(self, request, queryset)
        # print(request.POST.getlist('_selected_action'))
        id_list = request.POST.getlist('_selected_action')
        print(id_list)
        # models.UserInfo.objects.filter(id__in=id_list).delete()


    func.short_description = "批量删除"

    actions = [func,]
admin.site.register(models.UserInfo,UserInfoConfig)















# 生成URL
# /admin//app01/role/           查看列表页面
# /admin/app01/role/add/        添加页面
# /admin/app01/role/1/change/   修改页面
# /admin/app01/role/1/delete/   删除页面
admin.site.register(models.Role)

