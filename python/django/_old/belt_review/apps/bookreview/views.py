# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User, Book
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

def index(request):
    if 'user_id' in request.session:
        return redirect('/dashboard')
    return render(request, 'bookreview/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully registered!")
    return redirect('/dashboard')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id
    messages.success(request, "Successfully logged in!")
    return redirect('/dashboard')

def logout(request):
    try:
        del request.session['user_id']
    except KeyError:
        return redirect('/dashboard')
    return redirect('/dashboard')

def dashboard(request):
    try:
        request.session['user_id']
    except:
        return redirect('/')
    request.session['user_id']
    context ={
        'user': User.objects.get(id=request.session['user_id']),
        'users': User.objects.all(),
        'books': Book.objects.all()
    }
    return render(request, 'bookreview/dashboard.html', context)

def show(request, user_id):
    # user = User.objects.get(id=request.session['user_id'])
    # unique_ids = user.reviews_left.all().values("book").distinct()
    # unique_books = []
    # for book in unique_ids:
    #     unique_books.append(Book.objects.get(id=book['book']))
    context = {
        # 'users': User.objects.all(),
        'user': User.objects.get(id=request.session['user_id']),
        'users': User.objects.get(id=user_id)
        # 'unique_book_reviews': unique_books
    }
    return render(request, 'bookreview/user.html', context)

def bookform(request):
    user = User.objects.get(id=request.session['user_id'])
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'bookreview/bookform.html', context)

def add(request):
    user = User.objects.get(id=request.session['user_id'])
    Book.objects.create(
        title=request.POST['title'],
        author=request.POST['author'],
        review=request.POST['review'],
        rating=request.POST['rating']
    )
    context = {
        'user': User.objects.get(id=request.session['user_id']),
    }
    return redirect('/dashboard', context)

def bookpage(request, book_id):
    context = {
        
        'book': Book.objects.get(id=book_id)
    }
    return render(request, 'bookreview/bookpage.html', context)

def minireview(request, book_id):
    user = User.objects.get(id=request.session['user_id'])
    book = Book.objects.get(id=book_id)
    Book.objects.create(
        title=Book.objects.get(id=book_id),
        author=Book.objects.get(author=book.author),
        review=request.POST['review'],
        rating=request.POST['rating'],
    )
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'book': Book.objects.get(id=book_id),
        'books': Book.objects.filter(review='review')
    }
    return render(request, 'bookreview/bookpage.html', context)