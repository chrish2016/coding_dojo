# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from .models import User, Course, Student
from django.contrib.messages import error
from django.contrib import messages
from django.views.generic.edit import CreateView

#*************************************************************************
# LOGIN/REG APP
#*************************************************************************
def index(request):
    if 'user_id' in request.session:
        return redirect('/courses')
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
                        return redirect('/courses')
                else:
                    return redirect('/')
        request.session['user_id'] = request.POST['password']

def logout(request):
    if 'user_id' in request.session:
        del request.session['user_id']
    return redirect ('/')

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
        return redirect('/courses')

def success(request):
    return redirect('/courses')


#*************************************************************************
# CATALOG APP
#*************************************************************************
def catalog(request):
    context = {
        'courses': Course.objects.all(),
        'users': User.objects.all()
    }
    return render(request, 'catalog/dashboard.html', context)

def enroll(request):
    Student.objects.create(
        course=request.POST['course_id'],
        user=request.POST['user_id']
    )
    print request.POST
    return redirect ('/courses')

#*************************************************************************
# NEW_COURSES APP
#*************************************************************************
def courses(request):
    context = {
        'courses': Course.objects.all()
    }
    return render(request, 'new_courses/index.html', context)

def add(request):
    Course.objects.create(
        name=request.POST['name'],
        description=request.POST['description']
    )
    print request.POST
    return redirect('/courses/users_courses')

def remove(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'new_courses/remove.html', context) 

def delete(request, course_id):
    course = Course.objects.get(id=course_id).delete()
    return redirect('/courses/users_courses')
