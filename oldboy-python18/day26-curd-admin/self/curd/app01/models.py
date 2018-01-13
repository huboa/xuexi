from django.db import models

# Create your models here.

from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

class Role(models.Model):
    title = models.CharField(max_length=32)

