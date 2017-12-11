# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-18 03:42
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0002_auto_20171118_1004'),
    ]

    operations = [
        migrations.CreateModel(
            name='AuthorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('addr', models.CharField(max_length=32)),
                ('author', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app01.Author')),
            ],
        ),
        migrations.AlterField(
            model_name='book',
            name='publisher',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bookList', to='app01.Publish'),
        ),
    ]
