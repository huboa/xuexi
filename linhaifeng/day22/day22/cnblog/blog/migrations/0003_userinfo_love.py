# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 10:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20171211_1426'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='love',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
