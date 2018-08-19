from django.shortcuts import render, redirect, HttpResponse
from time import gmtime, strftime
from datetime import datetime
import random

# Create your views here.
def index(request):
    context = {
        'gold': request.session['gold'],
        'time': request.session['time']
            # 'transaction': request.session['transaction']
    }
    return render(request, 'ninja/index.html', context)

def places(request):
    
    time = request.session.get('time')
    gold = request.session.get('gold', 0)
    building = request.POST['building']
    if building == 'farm':
        request.session['gold'] = random.randrange(10,20+1)
        print 'this is the farm', gold, time
    if building == 'cave':
        request.session['gold'] = random.randrange(5,10+1)
        print 'This is the cave', gold, time
    if building == 'house':
        request.session['gold'] = random.randrange(2,5+1)
        print 'This is the house', gold, time
    if building == 'casino':
        request.session['gold'] = random.randrange(-50,50+1)
        print 'This is the casino', gold, time

    request.session['building'] = building
    request.session['time'] = strftime("%Y-%m-%d %H:%M %p", gmtime())
    request.session['gold'] += gold

    request.session.modified = True
    return redirect('/')

def reset(request):
    try:
        del request.session['gold']
    except KeyError:
        pass
    return redirect('/places')