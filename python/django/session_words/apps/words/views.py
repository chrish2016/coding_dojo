from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import string, random

def index(request):
    if 'word' not in request.session:
        request.session['words'] = []

    return render(request, "words/index.html")

def process(request):
    if 'word' not in request.session:
        request.session['wordlist'] = []
    
    word = request.POST['word']
    new_word = {
        'word': word
    }
    request.session['wordlist'].append(new_word)
    request.session.modified = True
    return redirect('/')

# def result(request):    
#     context = {
#         'wordlist': request.session.get('wordlist', 0)
#     }
#     # return render(request, "words/index.html", context)
#     return redirect('/', context)

def reset(request):
    try:
        del request.session['wordlist']
    except KeyError:
        pass
    return redirect('/')