from django.db import models
from app02 import models as app02_models
# 方式一
# class UserInfo(models.Model):
#     user = models.OneToOneField(to=app02_models.UserInfo)
#     email = models.CharField(max_length=32)

# 方式二
class User(app02_models.UserInfo):
    email = models.CharField(max_length=32)
