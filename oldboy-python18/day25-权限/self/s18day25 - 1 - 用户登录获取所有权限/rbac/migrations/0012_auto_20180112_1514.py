# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 07:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0011_remove_permission_group_menu'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissiongroup',
            name='caption',
            field=models.CharField(max_length=32, null=True),
        ),
    ]
