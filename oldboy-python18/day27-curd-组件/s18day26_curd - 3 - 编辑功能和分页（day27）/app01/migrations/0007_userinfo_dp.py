# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 04:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0006_department'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='dp',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app01.DepartMent'),
        ),
    ]
