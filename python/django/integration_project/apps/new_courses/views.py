# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse
from .models import Course

def index(request):
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
    return redirect('/')

def remove(request, course_id):
    context = {
        'course': Course.objects.get(id=course_id)
    }
    return render(request, 'new_courses/remove.html', context) 

def delete(request, course_id):
    course = Course.objects.get(id=course_id).delete()
    return redirect('/')