# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User, Comment, Post
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
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
       for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
       return redirect('/register')
    else:
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            description=request.POST['description'],
            password=request.POST['password']
        )
        return redirect('/login')

def login(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'dashboard/login.html')

def session(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        if len(errors):
            for tag, error in errors.iteritems():
                messages.error(request, error, extra_tags=tag)
            return redirect('/login')
        else:

            request.session['user_id'] = 'user_id'
            
            print "SUCCESS, SESSION STARTS NOW"
        return redirect('/dashboard')

def logout(request):
    if 'user_id' not in request.session:
        return redirect('/')
    else:
        del request.session['user_id']
        return redirect('/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/')
    request.session['user_id']
    user= User.objects.all()
    context = {
        'users': User.objects.all(),
        'admins': User.objects.filter(admin=1),
        'members': User.objects.filter(admin=0),
    }
    if admin == True:
        print "ADMIN", user
        return redirect('/admin')
    else:
        print "MEMBER", user
        return render(request, 'dashboard/dashboard.html', context)
    
def profile(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'dashboard/user.html', context)

def admin(request):
    if 'user_id' not in request.session:
        return redirect('/')
    context = {
        # 'users': User.objects.all(),
        'users': User.objects.all()
    }
    user= User.objects.all()
    admin = User.objects.filter(admin=1)
    member = User.objects.filter(admin=0)
    if admin == True:
        print "ADMIN", user
        return render(request, 'dashboard/admin.html', context)
    if member == True:
        print "MEMBER", user
        return redirect('/dashboard')

def show(request, user_id):
    Comment.objects.all()
    this_user = User.objects.get(id=user_id)
    context = {
        'user': User.objects.get(id=user_id),
        'this_user': User.objects.get(id=user_id),
        'comments':  Comment.objects.filter(user=this_user).order_by('created_at'),
        'posts': Post.objects.filter(user=this_user).order_by('created_at'),
        'users': User.objects.all(),
        'admin': User.objects.get(admin=1)
    }
    return render(request, 'dashboard/user.html', context)


def edit(request, user_id):
    User.objects.all()
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, 'dashboard/edit.html', context)

def update(request, user_id):
    context = {
            'user': User.objects.get(id=user_id)
        }
    errors = User.objects.update_validator(request.POST)
    if len(errors):
       for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
          return redirect('/user/{}/edit'.format(user_id))
    else:
        user_to_update = User.objects.get(id=user_id)
        user_to_update.first_name = request.POST['first_name']
        user_to_update.last_name = request.POST['last_name']
        user_to_update.email = request.POST['email']
        user_to_update.save()
        
        return redirect('/user/{}'.format(user_id), context)

def delete(request, user_id):
    user = User.objects.get(id=user_id).delete()
    return redirect('/dashboard')

def comment(request, user_id):
    this_user = User.objects.get(id=user_id)    
    my_comment = Comment.objects.create(comment=request.POST['comment'], user=this_user)
    context = {
        'this_user': User.objects.get(id=user_id),
        'comments': Comment.objects.filter(user=this_user)
    }
    print request.POST
    # return redirect('/show', context)
    return redirect('/user/{}/'.format(user_id), context)

def post(request, user_id):
    this_user = User.objects.get(id=user_id)    
    my_post = Post.objects.create(post=request.POST['post'], user=this_user)
    context = {
        'this_user': User.objects.get(id=user_id),
        'posts': Post.objects.filter(user=this_user)
    }
    print request.POST
    # return redirect('/show', context)
    return redirect('/user/{}/'.format(user_id), context)

def new_user(request):
    return render(request, 'dashboard/new_user.html')

def process_user(request):
    errors = User.objects.reg_validator(request.POST)
    if len(errors):
       for tag, error in errors.iteritems():
          messages.error(request, error, extra_tags=tag)
       return redirect('/register')
    else:
        User.objects.create(
            first_name=request.POST['first_name'],
            last_name=request.POST['last_name'],
            email=request.POST['email'],
            description=request.POST['description'],
            password=request.POST['password']
        )
        return redirect('/dashboard')

def delete_comment(request, user_id):
    comment = Comment.objects.get(id=id).delete()
    return redirect('/user/{}/comment/'.format(user_id))
