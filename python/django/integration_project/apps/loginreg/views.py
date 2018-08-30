# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from ..new_courses.models import Course
from django.contrib.messages import error
from django.contrib import messages
import bcrypt

def index(request):
    if 'user_id' in request.session:
        return redirect ('/courses')
    return render(request, 'loginreg/index.html')

def registration(request):
    result = User.objects.reg_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            print request.POST
        return redirect('/')
    request.session['user_id'] = result.id
    user_id = request.session['user_id']
    # messages.success(request, "Successfully registered!")
    return redirect('/courses')

def login(request):
    result = User.objects.login_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            print request.POST
        return redirect('/')
    request.session['user_id'] = result.id
    user_id = request.session['user_id']
    # messages.success(request, "Successfully Logged in!")
    return redirect('/courses')

def logout(request):
    if not 'user_id' in request.session:
        return redirect('/')
    else:
        del request.session['user_id']
    return redirect ('/')


def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'loginreg/edit_user.html', context)

def update(request, user_id):
    context = {
            'user': User.objects.get(id=user_id)
        }
    result = User.objects.update_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            print request.POST
        return redirect('/user/{}/edit'.format(user_id))
    else:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.email = request.POST['email']
        user_to_update.save()
        return redirect('/user/{}'.format(user_id), context)

def update_password(request, user_id):
    context = {
            'user': User.objects.get(id=user_id)
        }
    result = User.objects.password_validator(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            print request.POST
        return redirect('/user/{}/edit'.format(user_id))
    
    user_to_update = User.objects.get(id=user_id)
    user_to_update.password = bcrypt.hashpw((request.POST['password'].encode()), bcrypt.gensalt(5))
    user_to_update.save()
    return redirect('/user/{}'.format(user_id), context)

def delete_user(request, user_id):
    user = User.objects.get(id=user_id).delete()
    return redirect('/courses')
