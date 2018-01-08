
from rbac import models
user="zsc"
pwd="123"
user = models.UserInfo.objects.filter(username=user, password=pwd)
print(user)