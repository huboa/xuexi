# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-28 08:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_auto_20180428_1629'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissiongroup',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='权限组名称'),
        ),
    ]