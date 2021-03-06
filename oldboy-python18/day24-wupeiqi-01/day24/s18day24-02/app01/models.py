from django.db import models

class UserInfo(models.Model):
    # nid = models.AutoField(primary_key=True)
    # nid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title

class Host(models.Model):
    hostname = models.CharField(verbose_name='主机名',max_length=32)
    ip = models.CharField(max_length=32)# ip = models.GenericIPAddressField(protocol='both')
    port = models.IntegerField()
    user = models.ForeignKey(to='UserInfo',default=1)
    dp = models.ManyToManyField(to="Department")