from django.db import models

class UserInfo(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)

    def __str__(self):
        return self.name

class Role(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title


class Group(models.Model):
    title = models.CharField(max_length=32)

    def __str__(self):
        return self.title