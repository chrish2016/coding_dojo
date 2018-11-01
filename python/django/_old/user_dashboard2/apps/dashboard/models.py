# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your models here.
class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name must be used."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name must be used."
        if len(postData['email']) < 1:
            errors["email"] = "Email must be used."
        if not "email" in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "invalid email"
        if len(postData['password']) < 4:
            errors["password"] = "Password must be longer than 4 characters."
        if postData['password'] != postData['confirmation']:
            errors["password"] = "Please confirm password again."
        
        else:
            if len(self.filter(email=postData['email'])) > 1:
                errors['email'] = "email already in use"

        return errors


    def login_validator(self, postData):
        errors = {}
        # check DB for post_data['email']
        if len(self.filter(email=postData['email'])) > 0:
            user = self.filter(email=postData['email'])[0]
            if not postData['password'] == user.password:
                errors['email'] = "password/email does not match"
        else:
            errors['password'] = "problems matching password with email address."

        return errors

    
    def update_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name must be used."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name must be used."
        if len(postData['email']) < 1:
            errors["email"] = "Email must be used."
        if not "email" in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "invalid email"
        if len(postData['password']) < 4:
            errors["password"] = "Password must be longer than 4 characters."
        if postData['password'] != postData['confirmation']:
            errors["password"] = "Please confirm password again."
        
        return errors


class User(models.Model):
    id = models.IntegerField(primary_key=True)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    admin = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.email
    def __repr__(self):
        return "<User object: {} {}>".format(self.first_name, self.last_name)
    def __str__(self):
        return self.password

class Comment(models.Model):
    id = models.IntegerField(primary_key=True)
    comment = models.CharField(max_length=1255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, default=None, related_name = "comments")
    def __repr__(self):
        return "<Comment object: {} {}>".format(self.comment, self.user)

class Post(models.Model):
    id = models.IntegerField(primary_key=True)
    post = models.CharField(max_length=1255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    user = models.ForeignKey(User, default=None, related_name = "posts")
    def __repr__(self):
        return "<Post object: {} {}>".format(self.post, self.user)