from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    roles = models.ManyToManyField(verbose_name="角色名",to="Roles")
    def __str__(self):
        return self.username

class Roles(models.Model):
    """角色表"""
    title =models.CharField(verbose_name="角色名称",max_length=32)
    permisions = models.ManyToManyField(verbose_name="权限",max_length=32,to="Permissions")

class Permissions(models.Model):
    """权限表"""
    title = models.CharField(verbose_name="权限名称",max_length=32)
    url = models.CharField(verbose_name="含正则url",max_length=255)
    code = models.CharField(verbose_name="权限代码", max_length=32,)
    group = models.ForeignKey(verbose_name="权限组",to="PermissionGroup",)


class PermissionGroup(models.Model):
#     """
#     权限组
#     1 用户管理组
#     2 主机管理组
#     3 其它组
#     """
    title = models.CharField(max_length=32)