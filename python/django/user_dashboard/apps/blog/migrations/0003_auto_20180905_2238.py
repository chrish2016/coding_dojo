# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-05 22:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reglogin', '0005_auto_20180905_0440'),
        ('blog', '0002_auto_20180905_2204'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='blog',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='reglogin.User'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='commenter',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='reglogin.User'),
        ),
    ]