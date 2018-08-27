# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    response = 'placeholder to later display all the list of blogs'
    return HttpResponse(response)

def new(request):
    response = 'display "placeholder to display a new form to create a new blog'
    return HttpResponse(response)

def create(request):
    return redirect('/blogs')

def show(request, blog_id):
    response = 'placeholder to display blog {}'.format(blog_id)
    return HttpResponse(response)

def edit(request, blog_id):
    response = 'placeholder to edit blog {}'.format(blog_id)
    return HttpResponse(response)

def delete(request, blog_id):
    response = 'placeholder to delete blog {}'.format(blog_id)
    print response
    return redirect('/blogs')