from __future__ import unicode_literals
import re
import bcrypt
from django.db import models


EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

class UserManager(models.Manager):
    def validate_registration(self, post_data):
        errors = []
        if len(post_data['first_name']) < 1:
            errors.append("First name cannot be empty.")
        if len(post_data['last_name']) < 1:
            errors.append("Last name cannot be empty.")
        if len(post_data['email']) < 1:
            errors.append("Email must be provided")
        if len(post_data['description']) < 1:
            errors.append("Must give a brief description about yourself.")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")
        if len(User.objects.filter(email=post_data['email'])) > 0:
            errors.append("email already in use")
        if post_data['password'] != post_data['confirm']:
            errors.append("passwords do not match")

        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
            new_user = self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                email=post_data['email'],
                description=post_data['description'],
                password=hashed
            )
            return new_user
        return errors

    def validate_login(self, post_data):
        errors = []
        if len(self.filter(email=post_data['email'])) > 0:
            # check this user's password
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('email/password incorrect')
        else:
            errors.append('email/password incorrect')

        if errors:
            return errors
        return user

    def validate_profile(self, post_data):
        errors = []
        if len(post_data['first_name']) < 1:
            errors.append("First name cannot be empty.")
        if len(post_data['last_name']) < 1:
            errors.append("Last name cannot be empty.")
        if len(post_data['email']) < 1:
            errors.append("Email must be provided")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append('name fields must be letter characters only')
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("invalid email")

        if errors:
            return errors

    def validate_description(self, post_data):
        errors = []
        if len(post_data['description']) < 1:
            errors.append("Must give a brief description about yourself.")

        if errors:
            return errors
        
    def validate_password(self, post_data):
        errors = []
        if len(post_data['password']) < 8:
            errors.append("password must be at least 8 characters")
        if post_data['password'] != post_data['confirm']:
            errors.append("passwords do not match")

        if errors:
            return errors

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    description = models.CharField(max_length=255, blank=True)
    password = models.CharField(max_length=255)
    admin = models.IntegerField(default=9)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.email