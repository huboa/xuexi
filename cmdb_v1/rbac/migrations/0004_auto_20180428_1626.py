# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-28 08:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0003_permissions_gmid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissiongroup',
            name='title',
            field=models.CharField(max_length=32, unique=True, verbose_name='组ID'),
        ),
    ]