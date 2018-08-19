from products import items
from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "items": items
    }
    return render(request, "amadon_app/index.html", context)

def buy(request, item_id):
    for item in items:
        if item['id'] == int(item_id):
            amount_charged = item['price'] * int(request.POST['quantity'])    
    try:
        request.session['total_charged']
    except KeyError:
        request.session['total_charged'] = 0

    try:
        request.session['total_items']
    except KeyError:
        request.session['total_items'] = 0        

    request.session['total_charged'] += amount_charged
    request.session['total_items'] += int(request.POST['quantity'])
    request.session['last_transaction'] = amount_charged
    return redirect('/checkout')

def checkout(request):
    return render(request, "amadon_app/checkout.html")

def clear_basket(request):
    try:
        del request.session['total_charged']
        del request.session['total_items']
    except KeyError:
        pass
    return redirect('/checkout')