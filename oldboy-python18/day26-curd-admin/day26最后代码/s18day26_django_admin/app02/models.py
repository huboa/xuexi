from django.db import models


class Host(models.Model):
    """
    主机表
    """
    hostname = models.CharField(max_length=32)