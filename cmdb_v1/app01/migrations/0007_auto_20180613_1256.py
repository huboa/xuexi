# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-13 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_auto_20180613_1255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='Hdisk',
            field=models.CharField(default='', max_length=64, verbose_name='磁盘'),
        ),
    ]
