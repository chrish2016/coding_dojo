# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-31 16:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0007_auto_20180831_1556'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tourist',
            name='tourist_destination',
        ),
        migrations.RemoveField(
            model_name='tourist',
            name='tourists',
        ),
        migrations.RemoveField(
            model_name='trip',
            name='travelers',
        ),
        migrations.DeleteModel(
            name='Tourist',
        ),
    ]
