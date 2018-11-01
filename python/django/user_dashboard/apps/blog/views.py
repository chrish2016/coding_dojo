# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..reglogin.models import User
from .models import Comment
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    
    
    context = {
        'this_user': User.objects.get(id=request.session['user_id']),
        'user': User.objects.get(id=request.session['user_id']),
        'users': User.objects.all(),
        'admins': User.objects.filter(admin=9),
        'members': User.objects.filter(admin=0)
    }
    return render(request, 'blog/dashboard.html', context)

def user(request, user_id):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'this_user': User.objects.get(id=request.session['user_id']),
        'user': User.objects.get(id=user_id),
        'users': User.objects.all(),
        'comments': Comment.objects.all()
    }
    return render(request, 'blog/user.html', context)

def comment(request, user_id):
    result = Comment.objects.validate_blog(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/user/{}'.format(user_id))
    else:
        Comment.objects.create(
            comment=request.POST['comment'],
            commenter=User.objects.get(id=request.session['user_id']),
            blog=User.objects.get(id=user_id)
            )
        return redirect('/user/{}'.format(user_id))