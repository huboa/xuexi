
from rbac import models
user="zsc"
pwd="123"
user = models.UserInfo.objects.filter(username="zsc", password='123').all()
print(user)