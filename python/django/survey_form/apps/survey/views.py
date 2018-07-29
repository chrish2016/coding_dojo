from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import string, random

  # the index function is called when root is visited

def index(request):
    return render(request, "survey/index.html")

def process(request):
    counter = request.session.get('counter', 0)
    if request.method == "POST":
        request.session['name'] = request.POST['name']
        request.session['location'] = request.POST['location']
        request.session['language'] = request.POST['language']
        request.session['comment'] = request.POST['comment']
        request.session['counter'] = counter + 1
        return redirect('/result')
    else:
        return redirect('/')


def result(request):
    context = {
        'name': request.session['name'],
        'location': request.session['location'],
        'language': request.session['language'],
        'comment': request.session['comment'],
        'counter': request.session.get('counter', 0)
    }
    return render(request, "survey/result.html", context)

def reset(request):
    try:
        del request.session['counter']
    except KeyError:
        pass
    return redirect('/')