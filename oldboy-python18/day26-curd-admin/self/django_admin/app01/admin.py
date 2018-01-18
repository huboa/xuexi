from django.contrib import admin
from app01 import models
# Register your models here.



class DepartmentConfig(admin.ModelAdmin):
    list_display =  ['id','title','code',"edit"]
    list_display_links = ['edit']

    def edit(self,obj):
        return '编辑'


admin.site.register(models.Department,DepartmentConfig)

class UserInfoConfig(admin.ModelAdmin):
    list_display = ['title', 'user', "edit"]
    list_display_links = ['edit']

    def edit(self, obj):
        return '编辑'
admin.site.register(models.UserInfo,UserInfoConfig)
