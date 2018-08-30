# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..loginreg.models import User
from ..new_courses.models import Course

# Create your models here.

class Student(models.Model):
    course = models.ForeignKey(Course, default=None, related_name="students")
    user = models.ForeignKey(User, default=None, related_name = "students")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)