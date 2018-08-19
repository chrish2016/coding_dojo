# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import User
from django.contrib.messages import error
from django.contrib import messages
import bcrypt

def index(request):
    if 'user_id' in request.session:
        return redirect('/success')
    context = {
          'users': User.objects.all()
    }
    return render(request, 'loginreg/index.html', context)

def login(request):
    errors = User.objects.login_validator(request.POST)
    users = User.objects.all()
    if request.method == "POST":
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/')
        else:
            for user in users:
                if user.email == request.POST['email']:
                    if user.email == request.POST['email']:
                        request.session['user_id'] = request.POST['password']
                        
                        print "SUCCESS"
                        return redirect('/success')
                else:
                    return redirect('/')
        request.session['user_id'] = request.POST['password']

def register(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            password=request.POST['password']
        )
        return redirect('/success')

def success(request):
    return render(request, 'loginreg/success.html')