# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-20 04:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20180120_1204'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepartMent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32)),
            ],
        ),
    ]
