# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User
from .models import Course


# Create your models here.
class Roster(models.Model):
    course = models.ManyToManyField(Course, blank=True)
    user = models.ManyToManyField(User, blank=True)
    registered_users = models.PositiveIntegerField(null=True)