# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..reglogin.models import User


class BlogManager(models.Manager):
    def validate_blog(self, post_data):
        errors = []
        if len(post_data['comment']) < 1:
            errors.append("Comment cannot be empty.")

        if errors:
            return errors

# Create your models here.
class Comment(models.Model):
    comment = models.CharField(max_length=1255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    commenter = models.ForeignKey(User, default=None)
    blog = models.ForeignKey(User, default=None, related_name = "comments")
    objects = BlogManager()
    def __repr__(self):
        return "<Comment object: {} {}>".format(self.comment, self.user)