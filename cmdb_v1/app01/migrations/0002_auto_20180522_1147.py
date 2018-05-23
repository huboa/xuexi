# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-05-22 03:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='host',
            name='ip',
        ),
        migrations.AddField(
            model_name='host',
            name='host_ip',
            field=models.CharField(default='null', max_length=32, verbose_name='主机ip'),
        ),
        migrations.AddField(
            model_name='host',
            name='manufacturer',
            field=models.CharField(default='null', max_length=32, verbose_name='品牌'),
        ),
        migrations.AddField(
            model_name='host',
            name='product_name',
            field=models.CharField(default='null', max_length=32, verbose_name='型号'),
        ),
        migrations.AlterField(
            model_name='host',
            name='hostname',
            field=models.CharField(default='null', max_length=32, verbose_name='主机名'),
        ),
        migrations.AlterField(
            model_name='host',
            name='remoteip',
            field=models.GenericIPAddressField(default='null', protocol='ipv4'),
        ),
        migrations.AlterField(
            model_name='host',
            name='sn',
            field=models.CharField(default='null', max_length=32, unique=True, verbose_name='sn号'),
        ),
    ]
