# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        # check all fields for emptyness
        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name cannot be empty."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name cannot be empty"
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty."
        if not "email" in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "invalid email"
        if len(postData['password']) < 1:
            errors["password"] = "password cannot be empty."
        else:
            if len(self.filter(email=postData['email'])) > 1:
                errors['email'] = "email already in use"

        return errors
        
    def login_validator(self, postData):
        errors = {}
        # check all fields for emptyness
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty."
        if not "email" in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "invalid email"
        if len(postData['password']) < 1:
            errors["password"] = "password cannot be empty."
        if len(self.filter(password=postData['password'])) < 1:
                errors['password'] = "Password not in the system"
        if len(self.filter(email=postData['email'])) < 1:
            errors['password'] = 'password not in the system'
        if len(self.filter(email=postData['email'])) < 1:
            errors['email'] = "email not found in the system"
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.email

