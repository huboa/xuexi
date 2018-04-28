# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-06 16:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0009_auto_20180406_1627'),
    ]

    operations = [
        migrations.RenameField(
            model_name='permissions',
            old_name='group_memu',
            new_name='memu',
        ),
        migrations.AlterField(
            model_name='permissiongroup',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.menu', verbose_name='top菜单'),
        ),
    ]