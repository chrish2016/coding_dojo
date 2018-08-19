# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from .models import User, UserManager
from django.contrib.messages import error
from django.contrib import messages
from django.views.generic.edit import CreateView

def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'dashboard/index.html')    

def register(request):
    return render(request, 'dashboard/register.html')

def process(request):
    errors = User.objects.validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/register')
    else:
        User.objects.create(
            email=request.POST["email"],
            first_name=request.POST["first_name"],
            last_name=request.POST["last_name"],
            description=request.POST["description"],
            password=request.POST["password"]
        )
    print request.POST
    return redirect('/dashboard')

def login(request):
    if request.session == True:
        return redirect('/dashboard')
    return render(request, 'dashboard/login.html')

def logging(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/login')
    else:
        messages.success(request, "Successfully logged in!")
        return redirect('/dashboard')
    
    return redirect('/login')

# def session(request):
#     result = User.objects.login_validator(request.POST)
#     if type(result) == list:
#         for err in result:
#             messages.error(request, err)
#         return redirect('/')
#     request.session['user_id'] = result.id
#     messages.success(request, "Successfully logged in!")
#     return redirect('/dashboard')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'restful/user.html', context)

def dashboard(request):
    context = {
        'users': User.objects.all()
    }
    return render(request, 'dashboard/dashboard.html', context)

def edit(request):
    context = {
        'users': User.objects.get(id=user_id)
    }
    return render(request, 'dashboard/user.html', context)

def update(request):
    context = {
        'users': User.objects.get(id=user_id)
    }
    return render(request, 'dashboard/user.html', context)

def delete(request):
    user = User.objects.get(id=user_id).delete()
    return redirect('/dashboard')

def new(request):
    return render(request, 'dashboard/new.html')

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        return redirect('/dashboard')
    return redirect('/')
