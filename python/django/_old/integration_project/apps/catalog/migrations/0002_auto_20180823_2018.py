# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-23 20:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='user',
            new_name='users',
        ),
    ]