from django.shortcuts import render, redirect, HttpResponse

# Create your views here.
def index(request):
    comment = 'This is your index to LOGIN'
    return HttpResponse(comment)