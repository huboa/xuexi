from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32,unique=True)
    password = models.CharField(verbose_name="密码",max_length=64,)
    roles = models.ManyToManyField(verbose_name="角色名",to="Role")
    def __str__(self):
        return self.username

class Role(models.Model):
    """角色表"""
    title =models.CharField(verbose_name="角色名称",max_length=32,unique=True)
    permissions = models.ManyToManyField(verbose_name="权限",max_length=32,to="Permissions")
    def __str__(self):
        return self.title

class menu(models.Model):
    '''
    主菜单
    '''
    name=models.CharField(max_length=32,)

class Permissions(models.Model):
    """权限表"""
    title = models.CharField(verbose_name="权限名称",max_length=32,unique=True)
    url = models.CharField(verbose_name="含正则url",max_length=255)
    code = models.CharField(verbose_name="权限代码", max_length=32,)
    group = models.ForeignKey(verbose_name="权限组",to="PermissionGroup",)
<<<<<<< HEAD
    def __str__(self):
        return self.title
=======
    memu = models.ForeignKey(verbose_name="组内菜单",to='self',null=True,blank=True,related_name='xxx')
>>>>>>> 83bde8805fe9a1d42eefb0cf87baa2c7a160e967

class PermissionGroup(models.Model):
#     """
#     权限组
#     1 用户管理组
#     2 主机管理组
#     3 其它组
#     """
    title = models.CharField(max_length=32,unique=True)
    menu = models.ForeignKey(verbose_name="top菜单",to='menu')