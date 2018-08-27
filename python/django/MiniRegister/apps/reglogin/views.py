# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect, HttpResponse
from .forms import RegisterForm

def index(request):
    form = RegisterForm()
    context = { "regForm": form }
    return render(request, 'reglogin/index.html', context)

def register(request):
    if request.method == "POST": # Confirm that the HTTP verb was a POST
        bound_form = RegisterForm(request.POST) # Bind the POST data to an instance of our RegisterForm
        print bound_form.is_valid() # True or False, based on the validations that were set!
        print bound_form.errors # Any errors in this form as a dictionary
	return redirect('index')

def login(request):
    return HttpResponse("you have LOGGED IN!")