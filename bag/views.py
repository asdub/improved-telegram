from django.shortcuts import render, redirect
from . models import *

# Create your views here.


def view_bag(request):
    """ View to render shopping bag order contents """

    return render(request, 'bag/bag.html')


def add_to_order(request, item_id):
    """ Add quantity of the specified product/ service to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    order = {}
    order['product_id'] = item_id
    order['quantity'] = quantity

    if 'artwork_request' in request.POST:
        order['artwork_request'] = request.POST['artwork_request']
        if 'product_size' in request.POST:
            order['product_size'] = request.POST['product_size']
            if 'product_text_content' in request.POST:
                order['product_text_content'] = request.POST['product_text_content']
                if 'artwork_colour' in request.POST:
                    order['artwork_colour'] = request.POST['artwork_colour']

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        order['quantity'] += quantity
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    request.session['order'] = order
    print(order)
    print(quantity)
    print(order['quantity'])
    return redirect(redirect_url)
