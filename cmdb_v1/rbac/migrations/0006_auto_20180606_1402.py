# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-06 06:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0005_auto_20180521_0948'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissions',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.PermissionGroup', verbose_name='权限组'),
        ),
    ]