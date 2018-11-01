from __future__ import unicode_literals
from django.db import models
from ..reglogin.models import User

class  BookManager(models.Manager):
    def validate_book(self, post_data):
        errors = []
        if len(post_data['title']) < 1:
            errors.append("A title must be given.")
        if len(Book.objects.filter(title=post_data['title'])) > 0:
            errors.append("This book is already registered. Please use another title.")
        if len(post_data['author']) < 1:
            errors.append("Enter a new one.")               
        # if len(post_data['author']) < 1 or len(post_data['new_author']) < 1:
        #     errors.append("Either pick an author from the dropdown or enter a new one.")
        if len(post_data['review']) < 1:
            errors.append("A review must be given.")
        if len(post_data['rating']) < 1:
            errors.append("A rating must be given.")

        if errors:
            return errors

    
    def validate_review(self, post_data):
        errors = []
        if len(post_data['review']) < 1:
            errors.append("A review must be given.")
        if len(post_data['rating']) < 1:
            errors.append("A rating must be given.")

        if errors:
            return errors

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
    def __str__(self):
        return self.title

class Review(models.Model):
    review = models.CharField(max_length=100)
    rating = models.IntegerField(default=1)
    reviewer = models.ForeignKey(User, related_name="reviews")
    book = models.ForeignKey(Book, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BookManager()
    def __str__(self):
        return self.review