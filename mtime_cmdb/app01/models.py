from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(max_length=64)
    def __str__(self):
        return self.username

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
