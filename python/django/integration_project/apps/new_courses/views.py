# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Course
from rosters import Roster
from ..loginreg.models import User
from ..blog.models import Comment

def index(request):
    if not 'user_id' in request.session:
        return redirect ('/')
    user_id = request.session['user_id']
    context = {
        'courses': Course.objects.all(),
        'users': User.objects.all(),
        'user': User.objects.get(id=user_id),
        'rosters': Roster.objects.all()
    }
    return render(request, 'new_courses/index.html', context)

def add(request):
    Course.objects.create(
        name=request.POST['name'],
        description=request.POST['description']
        # student=Course.objects.get(id=request.session['user_id'])
    )
    print request.POST
    return redirect('/courses')

def remove(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'new_courses/remove.html', context) 

def delete(request, course_id):
    course = Course.objects.get(id=course_id).delete()
    return redirect('/courses')

def user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'this_user': User.objects.get(id=user_id),
        'this_comment':  Comment.objects.filter(id=user_id).order_by('created_at'),
        'comments':  Comment.objects.filter(id=user_id).order_by('created_at'),
        'comments': Comment.objects.all()
        # 'comments':  Comment.objects.filter(id=user_id).order_by('created_at'),
        # 'commenter': Comment.objects.filter(commenter_id=user_id),
        # 'users': User.objects.all(),
        
    }
    return render(request, 'new_courses/user.html', context)
    

# def edit(request, user_id):
#     context = {
#         'user': User.objects.get(id=user_id)
#     }
#     return render(request, 'new_courses/user.html', context)