# -*- coding: utf-8 -*-
from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

class UserManager(models.Manager):
    def validator(self, postData):
        errors = {}

        if len(postData['first_name']) < 1:
            errors["first_name"] = "First name cannot be empty."
        if len(postData['last_name']) < 1:
            errors["last_name"] = "Last name cannot be empty"
        if len(postData['email']) < 1:
            errors["email"] = "Email cannot be empty."
        if not "email" in errors and not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = "invalid email"
        if len(postData['password']) < 1:
            errors["password"] = "Password cannot be empty."
        if postData['confirmation'] != postData['password']:
            errors["confirmation"] = "Please re-confirm password again."
        if len(postData['confirmation']) < 1:
            errors["confirmation"] = "Password confirmation must be completed."
        else:
            if len(self.filter(email=postData['email'])) > 1:
                errors['email'] = "email already in use"
            
        return errors

    def login_validator(self, post_data):
        errors = {}
        # check DB for post_data['email']
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if user.password != post_data['password']:
                errors["password"] = "Password does not match."
        else:
            errors["password"] = "User not in the system."

        return errors

    # def login_validator(self, post_data):
    #     errors = []
    #     # check DB for post_data['email']
    #     if len(self.filter(email=post_data['email'])) > 0:
    #         # check this user's password
    #         user = self.filter(email=post_data['email'])[0]
    #         if user.password != post_data['password']:
    #             errors.append('email/password incorrect')
    #     else:
    #         errors.append('email/password incorrect')

    #     if errors:
    #         return errors
        
    #     return user

    # def login_validator(self, postData):
    #     errors = []
    #     # check DB for post_data['email']
    #     if len(self.filter(email=postData['email'])) > 0:
    #         # calls up 'user'
    #         user = self.filter(email=postData['email'])[0]
    #         # check this user's password
    #         if user.password != postData['password']:
    #             errors['password'] = "email/password doesn't match."
    #     else:
    #         errors['password'] = "email/password doesn't match."
        
    #     return errors


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
 