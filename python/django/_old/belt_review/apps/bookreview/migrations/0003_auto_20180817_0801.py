# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 08:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0002_auto_20180817_0752'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True),
        ),
    ]
