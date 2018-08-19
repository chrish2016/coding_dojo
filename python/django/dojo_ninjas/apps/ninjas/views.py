from django.shortcuts import render, redirect, HttpResponse

def index(request):
    comment = "this is INDEX ninjas"
    return HttpResponse(comment)