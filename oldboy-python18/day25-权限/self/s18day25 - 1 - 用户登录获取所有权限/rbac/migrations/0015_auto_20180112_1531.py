# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-12 07:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0014_auto_20180112_1524'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissiongroup',
            name='menu',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
    ]
