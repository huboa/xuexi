from django.db import models
# Create your models here.
class IDC(models.Model):
    Iname=models.CharField(verbose_name="机房名称",max_length=32,unique=True)
    Icity=models.CharField(verbose_name="城市",max_length=32)
    Iaddr=models.CharField(verbose_name="地址",max_length=32)
    Itel=models.CharField(verbose_name="电话",max_length=32)
    Icontact=models.CharField(verbose_name="联系人",max_length=32)
    def __str__(self):
        return self.Iname
class Cabinet(models.Model):
    name = models.CharField(verbose_name="机柜名",max_length=32,)
    postion = models.CharField(verbose_name="机柜位",max_length=32)
    idc = models.ForeignKey(verbose_name="机房", to="IDC", default=1)
class Host(models.Model):
    idc = models.ForeignKey(verbose_name="机房",to="IDC",default=1)
    sn = models.CharField(verbose_name="sn号",max_length=32,)
    remoteip = models.GenericIPAddressField(verbose_name="带外ip",default='0.0.0.0')
    hostname = models.CharField(verbose_name="主机名",max_length=32,default="")
    host_ip = models.CharField(verbose_name="主机ip",max_length=32,default="0.0.0.0")
    manufacturer = models.CharField(verbose_name="品牌",max_length=32,default="")
    product_name = models.CharField(verbose_name="型号",max_length=32,default="")
    Hosys= models.CharField(verbose_name="操作系统",max_length=32,null=True)
    Hcore = models.CharField(verbose_name="内核架构", max_length=32, null=True)
    Hcpu=models.CharField(verbose_name="cpu",max_length=64,default="")
    Hmemory=models.CharField(verbose_name='内存',max_length=32,default="")
    Hdisk=models.CharField(verbose_name="磁盘",max_length=64,default="")
    HotherIp=models.CharField(verbose_name='其它ip',max_length=128,default="")
    Hother = models.CharField(verbose_name='备注', max_length=128, default="")
    def __str__(self):
        return self.hostname
class Vhost(models.Model):
    idc = models.ForeignKey(verbose_name="机房", to="IDC", blank=True, null=True)
    Host = models.ForeignKey(verbose_name="宿主机", to="Host",blank=True, null=True)

class Zabbix(models.Model):
    Zidc = models.ForeignKey(verbose_name="机房", to="IDC", default=1)
    Zname = models.CharField(verbose_name="name",max_length=32)
    Zip=models.CharField(verbose_name="zabbix_ip",max_length=32,default="0.0.0.0")

class ZabbixTemplate(models.Model):
    Zidc = models.ForeignKey(verbose_name="机房", to="IDC", default=1)
    Zname = models.CharField(verbose_name="name",max_length=32)
    Zip=models.CharField(verbose_name="zabbix_ip",max_length=32,default="0.0.0.0")

# class JumpServer(models.Model):
#     pass


