# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Opinion, Remark
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect ('/dashboard')
    return render(request, 'blog/index.html')

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
    return redirect('/user/{}'.format(user_id))

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
    return redirect('/user/{}'.format(user_id))

def logout(request):
    del request.session['user_id']
    return redirect('/')

def user(request, user_id):
    if not 'user_id' in request.session:
        return redirect ('/')
    context ={
        'user': User.objects.get(id=user_id),
        'users': User.objects.filter(id=user_id),
        'opinions': Opinion.objects.all(),
        # 'opinions': Opinion.objects.filter(opinioner_id=user_id)
    }
    return render(request, 'blog/user.html', context)

def dashboard(request):
    if not 'user_id' in request.session:
        return redirect ('/')
    user_id = request.session['user_id']
    context = {
        'users': User.objects.all(),
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'blog/dashboard.html', context)

def opinion(request, user_id):
    Opinion.objects.create(
        opinion=request.POST['opinion'],
        opinioner=User.objects.get(id=request.session['user_id'])
    )
    context = {
        'user': User.objects.get(id=user_id)
    }
    return redirect('/user/{}'.format(user_id), context)

# def opinion(request, user_id):
#     Opinion.objects.create(
#         opinion=request.POST['opinion'],
#         opinioner=User.objects.get(id=request.session['user_id'])
#     )
#     return redirect('/user/{}'.format(user_id))

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'blog/edit_user.html', context)

def update(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    user_to_update = User.objects.get(id=user_id)
    user_to_update.first_name = request.POST['first_name']
    user_to_update.last_name = request.POST['last_name']
    user_to_update.email = request.POST['email']
    user_to_update.save()
    # errors = User.objects.update_validator(request.POST)
    # if len(errors):
    #    for tag, error in errors.iteritems():
    #       messages.error(request, error, extra_tags=tag)
    #       return redirect('/user/{}/edit'.format(user_id))
    # #    return redirect('/blog/edit/'+id)
    # else:
    #     user_to_update = User.objects.get(id=user_id)
    #     user_to_update.first_name = request.POST['first_name']
    #     user_to_update.last_name = request.POST['last_name']
    #     user_to_update.email = request.POST['email']
    #     user_to_update.save()
        
    #     return redirect('/dashboard', context)
    return redirect('/user/{}'.format(user_id), context)

def delete(request, user_id):
    user = User.objects.get(id=user_id).delete()
    return redirect('/dashboard')
