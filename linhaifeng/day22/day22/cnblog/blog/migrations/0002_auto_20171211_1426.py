# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-11 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfo',
            name='avatar',
            field=models.FileField(default='avatar/default.png', upload_to='avatarDir/', verbose_name='头像'),
        ),
    ]
