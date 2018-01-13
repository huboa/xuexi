from stark.service import v1
from app01 import models
##注册类


v1.site.register(models.UserInfo)
v1.site.register(models.Role)