# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from ..bookreview.models import Book, Review
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from django.contrib.auth import logout


# Create your views here.
def index(request):
    if 'user_id' in request.session:
        return redirect('/books')
    return render(request, 'reglogin/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect('/books')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    return redirect('/books')

def logout(request):
    del request.session['user_id']
    return redirect('/')

def user(request, user_id):
    context = {
        'user': User.objects.get(id=user_id),
        'reviews': Review.objects.filter(reviewer=user_id),
        'books': Book.objects.all(),
        'total_review': Review.objects.filter(reviewer=user_id).count()
    }
    return render(request, 'bookreview/user.html', context)