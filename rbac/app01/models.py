from django.db import models

# Create your models here.


# Create your models here.
class UserInfo(models.Model):
    """用户表"""
    username = models.CharField(verbose_name="用户名",max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    roles = models.ManyToManyField(verbose_name="角色名",to="Role")

class Role(models.Model):
    """角色表"""
    title =models.CharField(verbose_name="角色名称",max_length=32)
    permisions = models.ManyToManyField(verbose_name="权限",to='Permissions')
class Permissions(models.Model):
    """权限表"""
    title = models.CharField(verbose_name="权限名称",max_length=32)
    url = models.CharField(verbose_name="含正则url",max_length=255)

