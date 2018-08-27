# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.exceptions import ValidationError
from django.db import models
import re
import bcrypt

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')


def validateLengthGreaterThanTwo(value):
    if len(value) < 3:
        raise ValidationError(
            '{} must be longer than: 2'.format(value)
        )

class UserManager(models.Manager):
    def create_user(self, post_data):
        errors = []
        if errors:
            return errors
        else:
            hashed = bcrypt.hashpw((post_data['password'].encode()), bcrypt.gensalt(5))
            new_user = self.create(
                    first_name=post_data['first_name'],
                    last_name=post_data['last_name'],
                    email=post_data['email'],
                    password=post_data['password']
                )
            return new_user

class User(models.Model):
    first_name = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
    last_name = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
    email = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
    password = models.CharField(max_length=255, validators = [validateLengthGreaterThanTwo])
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = UserManager()
    def __str__(self):
        return self.email

    
