from django.db import models

class UserInfo(models.Model):
    """
    用户表
        1      alex        123
        2      tianle      123
        2      yanglei      123

    """
    username = models.CharField(verbose_name='用户名',max_length=32)
    password = models.CharField(verbose_name='密码',max_length=64)
    roles = models.ManyToManyField(verbose_name='拥有角色',to="Role")

class Role(models.Model):
    """
    角色表
        1    CEO
        2    CTO
        3    UFO
        4    销售主管
        5    销售员
    """
    title = models.CharField(verbose_name='角色名称',max_length=32)
    permissions = models.ManyToManyField(verbose_name='拥有权限',to="Permission")

    def __str__(self):
        return self.title

class PermissionGroup(models.Model):
    """
    权限组
        1    用户权限组
        2    主机权限组
    """
    caption = models.CharField(max_length=32)

class Permission(models.Model):
    """
    权限表
        1     用户列表      /users/                 list               1
        2     添加用户      /users/add/             add                1
        3     删除用户      /users/del/(\d+)/       del                1
        4     修改用户      /users/edit/(\d+)/      edit               1

        1     主机列表      /hosts/                 list               2
        2     添加主机      /hosts/add/             add                2
        3     删除主机      /hosts/del/(\d+)/       del                2
        4     修改主机      /hosts/edit/(\d+)/      edit               2

    以后获取当前用户权限后，数据结构化处理，并放入session
    {
        1: {
            urls: [/users/,/users/add/ ,/users/del/(\d+)/],
            codes: [list,add,del]
        },
        2: {
            urls: [/hosts/,/hosts/add/ ,/hosts/del/(\d+)/],
            codes: [list,add,del]
        }
    }


    """
    title = models.CharField(verbose_name='权限名称',max_length=32)
    url = models.CharField(verbose_name='含正则的URL',max_length=255)
    code = models.CharField(verbose_name="权限代码",max_length=32)
    group = models.ForeignKey(verbose_name='所属权限组',to="PermissionGroup")
    groupid = models.SmallIntegerField(verbose_name="所属权限组id",default=1)


<<<<<<< HEAD

=======
>>>>>>> 895ccca56cdb4136ea39437e4c5c399b441561cd
class test1():
    print("test1")


