from django.db import models



# Create your models here.

class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=32,default='1002')

    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    dep = models.ForeignKey(to="Department")

    def __str__(self):
        return self.title
class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(max_length=32)
    users = models.ManyToManyField(to="UserInfo")

    def __str__(self):
        return self.title