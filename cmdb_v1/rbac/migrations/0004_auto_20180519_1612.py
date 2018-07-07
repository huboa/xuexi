# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-19 16:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_permissiongroup_menu'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissiongroup',
            name='title',
        ),
        migrations.AddField(
            model_name='permissiongroup',
            name='name',
            field=models.CharField(default='默认组', max_length=32, verbose_name='应用名称'),
        ),
    ]