from __future__ import unicode_literals
from django.db import models
from ..blog.models import User

class PostManager(models.Manager):
    def comment_validator(self, post_data):
        errors = []
        # check length of name fields
        if len(post_data['comment']) < 1:
            errors.append("Comment cannot be blank.")

        if not errors:
            new_comment = self.create(
                comment=post_data['comment']
            )
            return new_comment
        return errors
    
    def post_validator(self, post_data):
        errors = []
        # check length of name fields
        if len(post_data['post']) < 1:
            errors.append("Post cannot be blank.")

        if not errors:
            new_post = self.create(
                post=post_data['post']
            )
            return new_post
        return errors

class Comment(models.Model):
    comment = models.TextField(max_length=250)
    commenter = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="comments")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PostManager()
    def __str__(self):
        return self.comment

class Post(models.Model):
    post = models.TextField(max_length=250)
    poster = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="posts")
    comments = models.ForeignKey(Comment, null=True, on_delete=models.CASCADE, related_name="posts")
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = PostManager()
    def __str__(self):
        return self.reply