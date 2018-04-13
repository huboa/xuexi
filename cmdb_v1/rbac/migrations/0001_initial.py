# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-04-13 02:49
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='PermissionGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.menu', verbose_name='一级菜单')),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='权限名称')),
                ('url', models.CharField(max_length=255, verbose_name='含正则url')),
                ('code', models.CharField(max_length=32, verbose_name='权限代码')),
                ('group', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rbac.PermissionGroup', verbose_name='权限组')),
                ('memu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='xxx', to='rbac.Permissions', verbose_name='组内菜单')),
            ],
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, unique=True, verbose_name='角色名称')),
                ('permissions', models.ManyToManyField(max_length=32, to='rbac.Permissions', verbose_name='权限')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=32, unique=True, verbose_name='用户名')),
                ('password', models.CharField(max_length=64, verbose_name='密码')),
                ('roles', models.ManyToManyField(to='rbac.Role', verbose_name='角色名')),
            ],
        ),
    ]
