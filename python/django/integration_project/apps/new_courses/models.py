# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User


# Create your models here.
class Course(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    # registered_users = models.PositiveIntegerField(null=True)
    # users = models.ForeignKey(User, related_name="courses")
    # students = models.ManyToManyField(User, related_name="courses")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    registered_users = models.PositiveIntegerField(null=True)