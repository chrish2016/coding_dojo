# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
import bcrypt
import re
from django.contrib.auth import logout

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'reglogin/index.html')

def registrationform(request):
    return render(request, 'reglogin/register.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return render(request, 'reglogin/register.html')

    request.session['user_id'] = result.id
    # # messages.success(request, "Successfully registered!")
    return redirect('/dashboard')

def loginform(request):
    return render(request, 'reglogin/login.html')
    
def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return render(request, 'reglogin/login.html')
    if User.objects.get(admin=9):
        print "This is an ADMIN."
    else:
        print "This is a MEMBER"
    users = User.objects.all()
    request.session['user_id'] = result.id
    # messages.success(request, "Successfully logged in!")
    return redirect('/dashboard')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def edituser(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'users': User.objects.all()
    }
    return render(request, 'reglogin/edituser.html', context)

def edit_profile(request, user_id):
    context = {
            'user': User.objects.get(id=user_id)
        }
    result = User.objects.validate_profile(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            return redirect('/user/{}/edituser'.format(user_id))
    else:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.email = request.POST['email']
        user_to_update.save()
        return redirect('/user/{}'.format(user_id), context)

def edit_description(request, user_id):
    context = {
            'user': User.objects.get(id=user_id)
        }
    result = User.objects.validate_description(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            return redirect('/user/{}/edituser'.format(user_id))
    else:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.description = request.POST['description']
        user_to_update.save()
        return redirect('/user/{}'.format(user_id), context)

def edit_password(request, user_id):
    context = {
            'user': User.objects.get(id=user_id)
        }
    result = User.objects.validate_password(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
            return redirect('/user/{}/edituser'.format(user_id))
    else:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.password = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user_to_update.save()
        return redirect('/user/{}'.format(user_id), context)

def delete_confirm(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'blog/delete_confirm.html', context)

def delete_user(request, user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/dashboard')

def add_user(request):
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'reglogin/new.html', context)

def process_user(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return render(request, 'reglogin/new.html')
    return redirect('/dashboard')