# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 03:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='nickname',
            field=models.CharField(default=1, max_length=16, verbose_name='员工姓名'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='name',
            field=models.CharField(max_length=32, verbose_name='用户名'),
        ),
    ]
