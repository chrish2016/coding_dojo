from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect

  # the index function is called when root is visited

def index(request):
    context = {
        'name': 'Chris',
        'email': 'chris_hamilton11@yahoo.com'
    }
    return render(request, "blogs/index.html", context)

def new(request):
    response = "placeholder to display a new form to create a new blog"
    return HttpResponse(response)

def create(request):
    if request.method == "POST":
		print "*"*50
		print request.POST
		print request.POST['name']
		print request.POST['desc']
		request.session['name'] = "test"  # more on session below
		print "*"*50
		return redirect("/")
    else:
		return redirect("/")

def show(request, id):
    response = 'placeholder to display blog {}'.format(id) + '.'
    return HttpResponse(response)

def edit(request, id):
    response = "placeholder to edit blog {}".format(id) + '.'
    return HttpResponse(response)

def destroy(request, id):
    print "placeholder to DESTROY blog #{}".format(id) + '.'
    return redirect('/')