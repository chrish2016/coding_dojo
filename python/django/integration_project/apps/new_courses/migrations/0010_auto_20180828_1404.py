# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 14:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('new_courses', '0009_auto_20180828_1355'),
    ]

    operations = [
        migrations.RenameField(
            model_name='roster',
            old_name='enrolled_students',
            new_name='registered_users',
        ),
    ]
