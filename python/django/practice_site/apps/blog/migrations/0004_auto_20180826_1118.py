# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-26 11:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_remark_reviewer'),
    ]

    operations = [
        migrations.RenameField(
            model_name='remark',
            old_name='reviewer',
            new_name='remarker',
        ),
    ]