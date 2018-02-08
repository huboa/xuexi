from django.db import models

# 方式一
# class Group(models.Model):
#     title = models.CharField(max_length=32)
#
#
# class UserInfo(models.Model):
#     username = models.CharField(max_length=32)
#     password = models.CharField(max_length=32)
#     gp = models.ForeignKey(to="Group")


# 方式二
class Group(models.Model):
    title = models.CharField(max_length=32)


class UserInfo(models.Model):
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    gp = models.ForeignKey(to=Group)

    class Meta:
        abstract = True # 设置为“特殊类”，不再去数据库生成表。奉献精神，

