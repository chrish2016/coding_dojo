# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 03:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reglogin', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='user_level',
            field=models.IntegerField(default=9),
        ),
    ]