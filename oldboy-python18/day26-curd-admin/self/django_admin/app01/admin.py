from django.contrib import admin
from app01 import models
# Register your models here.
admin.site.register(models.Department)


class DepartmentConfig(admin.ModelAdmin):
    list_display =  ["title","code"]