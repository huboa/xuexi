# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-02 12:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0004_auto_20180402_1208'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Roles',
            new_name='Role',
        ),
    ]
