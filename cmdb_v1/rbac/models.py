from django.db import models


# Create your models here.
from django.db import models


class DepartMent(models.Model):
    """
    部门
    """
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32,unique=True)
    password = models.CharField(verbose_name="密码",max_length=64,)
    roles = models.ManyToManyField(verbose_name="角色名",to="Role")
    gender_choice = (
        (1, '男'),
        (2, '女'),
    )
    gender = models.IntegerField(verbose_name='性别', choices=gender_choice, default=1)

    status_choice = (
        (1, '在线'),
        (2, '离线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)

    dp = models.ForeignKey(to='DepartMent', default=1)###部门

    def __str__(self):
        return self.username



class Role(models.Model):
    """角色表"""
    title =models.CharField(verbose_name="角色名称",max_length=32,unique=True)
    permissions = models.ManyToManyField(verbose_name="权限",max_length=32,to="Permissions")
    def __str__(self):
        return self.title


class Permissions(models.Model):
    """权限表"""
    title = models.CharField(verbose_name="权限名称",max_length=32,unique=True)
    url = models.CharField(verbose_name="含正则url",max_length=255)
    code = models.CharField(verbose_name="权限代码", max_length=32,)
    group = models.ForeignKey(verbose_name="权限组",to="PermissionGroup",)
    gmid = models.ForeignKey(verbose_name="组内菜单",to='self',null=True,blank=True,related_name='xxx')
    def __str__(self):
        return self.title



class PermissionGroup(models.Model):
#     """
#     权限组
#     1 用户管理组
#     2 主机管理组
#     3 其它组
#     """
    title = models.CharField(verbose_name='权限组名称',max_length=32,unique=True)
    menu = models.ForeignKey(verbose_name="一级菜单",to='menu')


    def __str__(self):
        return self.title


class menu(models.Model):
    '''
    一级菜单左侧展示
    '''
    name=models.CharField(max_length=32,)

    def __str__(self):
        return self.name