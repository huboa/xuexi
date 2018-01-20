# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0004_auto_20180120_1159'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=models.IntegerField(choices=[(1, '在线'), (2, '离线')], default=1, verbose_name='状态'),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='gender',
            field=models.IntegerField(choices=[(1, '男'), (2, '女')], default=1, verbose_name='性别'),
        ),
    ]
