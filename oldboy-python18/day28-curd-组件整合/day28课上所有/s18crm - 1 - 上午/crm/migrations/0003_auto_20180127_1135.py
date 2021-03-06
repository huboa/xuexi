# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-01-27 03:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('crm', '0002_auto_20180127_1131'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classlist',
            name='course',
        ),
        migrations.RemoveField(
            model_name='classlist',
            name='school',
        ),
        migrations.RemoveField(
            model_name='classlist',
            name='teachers',
        ),
        migrations.RemoveField(
            model_name='classlist',
            name='tutor',
        ),
        migrations.RemoveField(
            model_name='consultrecord',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='consultrecord',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='courserecord',
            name='class_obj',
        ),
        migrations.RemoveField(
            model_name='courserecord',
            name='teacher',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='course',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='referral_from',
        ),
        migrations.RemoveField(
            model_name='customerdistribution',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='customerdistribution',
            name='user',
        ),
        migrations.RemoveField(
            model_name='paymentrecord',
            name='class_list',
        ),
        migrations.RemoveField(
            model_name='paymentrecord',
            name='consultant',
        ),
        migrations.RemoveField(
            model_name='paymentrecord',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='salerank',
            name='user',
        ),
        migrations.RemoveField(
            model_name='student',
            name='class_list',
        ),
        migrations.RemoveField(
            model_name='student',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='studyrecord',
            name='course_record',
        ),
        migrations.RemoveField(
            model_name='studyrecord',
            name='student',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='depart',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='roles',
        ),
        migrations.DeleteModel(
            name='ClassList',
        ),
        migrations.DeleteModel(
            name='ConsultRecord',
        ),
        migrations.DeleteModel(
            name='Course',
        ),
        migrations.DeleteModel(
            name='CourseRecord',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='CustomerDistribution',
        ),
        migrations.DeleteModel(
            name='Department',
        ),
        migrations.DeleteModel(
            name='PaymentRecord',
        ),
        migrations.DeleteModel(
            name='SaleRank',
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.DeleteModel(
            name='Student',
        ),
        migrations.DeleteModel(
            name='StudyRecord',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
