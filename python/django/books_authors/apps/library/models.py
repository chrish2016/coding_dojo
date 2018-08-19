from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Dojo(models.Model):
    id = models.IntegerField(primary_key=True)
    dojo_name = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    desc = models.TextField(default=0)
    state = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

class Ninja(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    dojo = models.ForeignKey(Dojo, related_name="ninjas")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)