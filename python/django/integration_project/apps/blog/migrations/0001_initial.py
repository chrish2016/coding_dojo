# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-29 15:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('loginreg', '0002_auto_20180828_1131'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comments', models.TextField(max_length=1000)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('commenter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='loginreg.User')),
            ],
        ),
    ]
