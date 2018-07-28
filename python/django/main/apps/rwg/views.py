from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
import string, random

  # the index function is called when root is visited



def index(request):
    counter = request.session.get('counter', 0)
    request.session['counter'] = counter + 1  
    randomword = ''.join([random.choice(string.ascii_lowercase) for n in xrange(12)])
    context = {
        'randomword': randomword,
        'counter': counter
    }
    return render(request, "rwg/index.html", context)

def reset(request):
    try:
        del request.session['counter']
    except KeyError:
        pass
    return redirect('/')