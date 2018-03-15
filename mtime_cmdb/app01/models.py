from django.db import models

# Create your models here.
class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)


class Host(models.Model):
    hostname = models.CharField(max_length=32)
    # ip = models.GenericIPAddressField(protocol='ipv4')
    ip = models.CharField(max_length=32)
    port = models.IntegerField()