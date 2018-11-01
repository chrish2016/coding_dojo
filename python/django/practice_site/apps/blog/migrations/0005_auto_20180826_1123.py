# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-26 11:23
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20180826_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Opinion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('opinion', models.TextField(max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('opinioner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='opinion', to='blog.User')),
            ],
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.RenameField(
            model_name='remark',
            old_name='remarks',
            new_name='remark',
        ),
    ]