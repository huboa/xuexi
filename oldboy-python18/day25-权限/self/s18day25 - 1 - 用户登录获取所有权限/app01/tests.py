from django.test import TestCase
from rbac import models
# Create your tests here.

models.UserInfo.objects.filter(username=21,password=2).first()
