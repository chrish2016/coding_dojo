from __future__ import unicode_literals
import re
import bcrypt
from django.db import models

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class UserManager(models.Manager):

    def reg_validator(self, post_data):
        errors = []
        if len(post_data['first_name']) < 1:
            errors.append("First name must be given.")
        if len(post_data['last_name']) < 1:
            errors.append("Last name must be given.")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append("Name fields must contain letters only.")
        if len(post_data['last_name']) < 1:
            errors.append("Email address must be given.")
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Email address must be valid.")
        if len(User.objects.filter(email=post_data)) > 1:
            errors.append("This email is already registered. Please provide a different email address.")
        if len(post_data['password']) < 3:
            errors.append("Password must be atleast 3 characters long.")
        if post_data['password'] != post_data['password_confirm']:
            errors.append("Confirmation didn't match. Please try again.")
        
        if not errors:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
            new_user= self.create(
                first_name=post_data['first_name'],
                last_name=post_data['last_name'],
                email=post_data['email'],
                password=hashed
            )
            return new_user
        return errors

    def login_validator(self, post_data):
        errors = []
        if len(self.filter(email=post_data['email'])) > 0:
            user = self.filter(email=post_data['email'])[0]
            if not bcrypt.checkpw(post_data['password'].encode(), user.password.encode()):
                errors.append('Email/Password do not match. Please try again.')
        else:
            errors.append('Email/Password error. Please try again.')

        if errors:
            return errors
        return user

    def update_validator(self, post_data):
        errors = []
        if len(post_data['first_name']) < 1:
            errors.append("First name must be given.")
        if len(post_data['last_name']) < 1:
            errors.append("Last name must be given.")
        if not re.match(NAME_REGEX, post_data['first_name']) or not re.match(NAME_REGEX, post_data['last_name']):
            errors.append("Name fields must contain letters only.")
        if len(post_data['last_name']) < 1:
            errors.append("Email address must be given.")
        if not re.match(EMAIL_REGEX, post_data['email']):
            errors.append("Email address must be valid.")
        if len(User.objects.filter(email=post_data)) > 1:
            errors.append("This email is already registered. Please provide a different email address.")
        
        if not errors:            
            return new_user
        return errors

class User(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.email

class Opinion(models.Model):
    opinion = models.TextField(max_length=250)
    opinioner = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="opinions")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.opinion

class Remark(models.Model):
    remark = models.TextField(max_length=250)
    remarker = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="remarks")
    # comments = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE, related_name="remarks")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.remark