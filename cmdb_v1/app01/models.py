from django.db import models

# Create your models here.
class Host(models.Model):
    idc = models.CharField(max_length=32,default="廊坊")
    sn = models.CharField(verbose_name="sn号",max_length=32,default='null',unique=True)
    remoteip = models.GenericIPAddressField(verbose_name="带外ip",protocol='ipv4',default='null')
    hostname = models.CharField(verbose_name="主机名",max_length=32,default='null')
    host_ip = models.CharField(verbose_name="主机ip",max_length=32,default='null')
    manufacturer = models.CharField(verbose_name="品牌",max_length=32,default='null')
    product_name = models.CharField(verbose_name="型号",max_length=32,default='null')

    def __str__(self):
        return self.hostname
