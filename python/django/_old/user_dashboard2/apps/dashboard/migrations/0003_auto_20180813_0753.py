# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-13 07:53
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='comments',
            new_name='comment',
        ),
    ]
