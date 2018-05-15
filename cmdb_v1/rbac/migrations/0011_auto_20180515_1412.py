# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-15 06:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0010_userinfo_session_key'),
    ]

    operations = [
        migrations.AlterField(
            model_name='permissiongroup',
            name='menu',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.Menu', verbose_name='一级菜单'),
        ),
    ]
