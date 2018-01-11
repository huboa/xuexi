# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-23 06:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostname', models.CharField(max_length=32)),
                ('ip', models.CharField(max_length=32)),
                ('port', models.IntegerField()),
            ],
        ),
    ]