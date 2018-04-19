print("加载stark文件")


from stark.service import v1
from rbac import models
#
# #注册mode表 待生成url
v1.site.registry(models.UserInfo)
v1.site.registry(models.Role)

