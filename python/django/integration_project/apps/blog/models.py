from __future__ import unicode_literals
import re
from django.db import models
from ..loginreg.models import User

# Create your models here.
class BlogManager(models.Manager):
    def blog_validator(self, post_data):
        errors = []
        if len(post_data['comment']) < 1:
            errors.append("Comment cannot be empty.")        
        if errors:
            return errors
    
class Comment(models.Model):
    comment = models.TextField(max_length=1000)
    commenter = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()
    def __str__(self):
        return self.comment