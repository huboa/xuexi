from django.db import models

class UserInfo(models.Model):
    # nid = models.AutoField(primary_key=True)
    # nid = models.BigAutoField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=64)
