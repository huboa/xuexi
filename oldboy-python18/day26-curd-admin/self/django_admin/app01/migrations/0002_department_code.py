# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-17 11:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='department',
            name='code',
            field=models.CharField(default='1002', max_length=32),
        ),
    ]