from django.db import models

# Create your models here.
class Host(models.Model):
    idc = models.CharField(max_length=32,default="廊坊")
    sn = models.CharField(max_length=32,default='000',unique=True)
    remoteip = models.GenericIPAddressField(protocol='ipv4',default='0.0.0.0.')
    hostname = models.CharField(verbose_name="主机",max_length=32)
    ip = models.CharField(max_length=32)
    def __str__(self):
        return self.hostname
