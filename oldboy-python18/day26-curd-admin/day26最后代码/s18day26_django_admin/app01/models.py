from django.db import models

class Department(models.Model):
    """
    部门表
    """
    title = models.CharField(max_length=32)
    code = models.CharField(max_length=32,default='1002')
 ####显显示内容title
    def __str__(self):
        return self.title

class UserInfo(models.Model):
    """
    用户表
    """
    name = models.CharField(max_length=32)
    email = models.EmailField(max_length=32)
    dp = models.ForeignKey(to='Department')

class Role(models.Model):
    """
    角色表
    """
    title = models.CharField(max_length=32)
    users = models.ManyToManyField(to='UserInfo')
