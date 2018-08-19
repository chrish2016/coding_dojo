# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-08-17 12:38
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bookreview', '0005_auto_20180817_1057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('author', models.CharField(max_length=50)),
                ('review', models.TextField(max_length=1000)),
                ('rating', models.IntegerField(default=1)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('reviewer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='books', to='bookreview.User')),
            ],
        ),
    ]