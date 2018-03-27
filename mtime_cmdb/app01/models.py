from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name="密码",max_length=64)
    roles = models.ManyToManyField(verbose_name="角色名",to="Role")
    def __str__(self):
        return self.username

class Role(models.Model):
    """角色表"""
    title =models.CharField(verbose_name="角色名称",max_length=32)
    permisions = models.ManyToManyField(verbose_name="权限",max_length=32,to="Permissions")

class Permissions(models.Model):
    """权限表"""
    title = models.CharField(verbose_name="权限名称",max_length=32)
    url = models.CharField(verbose_name="含正则url",max_length=255)


class Host(models.Model):
    idc = models.CharField(max_length=32,default="廊坊")
    sn = models.CharField(max_length=32,default='000')
    remoteip = models.GenericIPAddressField(protocol='ipv4',default='0.0.0.0.')
    hostname = models.CharField(verbose_name="主机",max_length=32)
    # ip = models.GenericIPAddressField(protocol='ipv4')
    ip = models.CharField(max_length=32)

    user = models.ForeignKey(to='UserInfo',default=1)
    dp = models.ManyToManyField(to='Department')


class Department(models.Model):
    title = models.CharField(max_length=32)
    def __str__(self):
        return self.title



