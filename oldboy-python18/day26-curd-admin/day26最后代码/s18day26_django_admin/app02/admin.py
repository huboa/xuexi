from django.contrib import admin
from app02 import models

# 生成URL
# /app02/host/
admin.site.register(models.Host)