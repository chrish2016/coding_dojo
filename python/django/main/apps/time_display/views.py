from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime

  # the index function is called when root is visited

def index(request):
    context = {
        'somekey': str(datetime.now())
    }
    return render(request, "time_display/index.html", context)