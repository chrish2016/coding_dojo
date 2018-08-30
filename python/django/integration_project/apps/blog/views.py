# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from django.contrib.messages import error
from django.contrib import messages
from ..loginreg.models import User
from .models import Comment

# Create your views here.
def comment(request, user_id):
    result = Comment.objects.blog_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            print request.POST
        return redirect('/user/{}'.format(user_id))
    else:
        this_commenter = User.objects.get(id=request.session['user_id'])
        comments = Comment.objects.filter(commenter=this_commenter)
        my_comment = Comment.objects.create(comment=request.POST['comment'], commenter=this_commenter)
        return redirect('/user/{}'.format(user_id))