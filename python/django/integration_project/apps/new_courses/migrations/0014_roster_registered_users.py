# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-28 15:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_courses', '0013_auto_20180828_1459'),
    ]

    operations = [
        migrations.AddField(
            model_name='roster',
            name='registered_users',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
