# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from ..reglogin.models import User
from .models import Book, Review
from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages

# Create your views here.
def dashboard(request):
    if not 'user_id' in request.session:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'users': User.objects.all(),
        'books': Book.objects.all().order_by('title'),
        'other_books': Book.objects.all().order_by('title')[4:],
        'reviews': Review.objects.all().order_by('-created_at')[:3]
        # 'reviews': Review.objects.all().exclude(reviewer=request.session['user_id']).order_by('-created_at')[:3]
    }
    return render(request, 'bookreview/dashboard.html', context)

def bookform(request):
    context = {
        'books': Book.objects.all()
    }
    return render(request, 'bookreview/bookform.html', context)

def addbook(request):
    result = Book.objects.validate_book(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/books/bookform')
    else:
        if len(request.POST['new_author']) > 1:
            Book.objects.create(
                title=request.POST['title'],
                author=request.POST['new_author']
            )
            Review.objects.create(
                review=request.POST['review'],
                rating=request.POST['rating'],
                reviewer=User.objects.get(id=request.session['user_id']),
                book=Book.objects.get(title=request.POST['title'])
            )
        else:
            Book.objects.create(
                title=request.POST['title'],
                author=request.POST['author']
            )
            Review.objects.create(
                review=request.POST['review'],
                rating=request.POST['rating'],
                reviewer=User.objects.get(id=request.session['user_id']),
                book=Book.objects.get(title=request.POST['title'])
            )
        return redirect('/books')

def book(request, book_id):
    user = request.session['user_id']
    context = {
        'user': User.objects.get(id=request.session['user_id']),
        'users': User.objects.all(),
        'book': Book.objects.get(id=book_id),
        'reviews': Review.objects.filter(id=book_id).order_by('-created_at')
    }
    return render(request, 'bookreview/book.html', context)

def addreview(request, book_id):
    result = Book.objects.validate_review(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/books/{}'.format(book_id))
    else:        
        Review.objects.create(
            review=request.POST['review'],
            rating=request.POST['rating'],
            reviewer=User.objects.get(id=request.session['user_id']),
            book=Book.objects.get(id=book_id)
        )
        return redirect('/books/{}'.format(book_id))

def deletereview(request, book_id):
    context = {
        'reviews': Review.objects.all(),
        'books': Book.objects.all(),
        'book': Book.objects.get(id=book_id)
    }
    Review.objects.get(id=review_id).delete()
    return redirect('/books/{}'.format(book_id))

