# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 22:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='user',
            new_name='commenter',
        ),
    ]
