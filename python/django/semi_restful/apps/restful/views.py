# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import User, UserManager
from django.contrib.messages import error
from django.contrib import messages
from django.views.generic.edit import CreateView

def index(request):
    context = {
          'users': User.objects.all()
    }
    return render(request, 'restful/index.html', context)

def new(request):
    return render(request, 'restful/new_user.html')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'restful/edit.html', context)

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'restful/user.html', context)

def create(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/new')
    else:
        User.objects.create(
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            email=request.POST["email"],
        )
    return redirect('/users')

def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/users')

def update(request, user_id):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/users/{}/edit'.format(user_id))
    else:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.email = request.POST['email']
        user_to_update.save()
        context = {
            'user': User.objects.get(id=user_id)
        }
        return render(request, 'restful/user.html', context)

