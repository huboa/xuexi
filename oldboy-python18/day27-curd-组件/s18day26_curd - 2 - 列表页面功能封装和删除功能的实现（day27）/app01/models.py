from django.db import models

class DepartMent(models.Model):
    """
    部门
    """
    title = models.CharField(max_length=32)

class UserInfo(models.Model):
    name = models.CharField(verbose_name='用户名',max_length=32)
    email = models.CharField(verbose_name='邮箱',max_length=32)

    gender_choice = (
        (1,'男'),
        (2,'女'),
    )
    gender = models.IntegerField(verbose_name='性别',choices=gender_choice,default=1)

    status_choice = (
        (1, '在线'),
        (2, '离线'),
    )
    status = models.IntegerField(verbose_name='状态', choices=status_choice, default=1)

    dp = models.ForeignKey(to='DepartMent',default=1)

    def __str__(self):
        return self.name

class Role(models.Model):
    title = models.CharField(verbose_name='角色名称',max_length=32)

    def __str__(self):
        return self.title


class Group(models.Model):
    title = models.CharField(verbose_name='组名称',max_length=32)

    def __str__(self):
        return self.title