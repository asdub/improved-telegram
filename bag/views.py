from django.shortcuts import render, redirect, reverse
from products.models import Product
from django.contrib import messages

import uuid

# Create your views here.


def view_bag(request):
    """ View to render shopping bag order contents """

    return render(request, 'bag/bag.html')


def add_to_order(request, item_id):
    """ Add quantity of the specified product/ service to the bag """

    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order')
    ref = uuid.uuid4().hex
    cus_order = {
            "order_ref": ref,
            "item_id": item_id,
            "quantity": int(request.POST.get("quantity")),
            "artwork_request": request.POST.get("artwork_request"),
            "product_size": request.POST.get("product_size"),
            "product_text_content": request.POST.get("product_text_content"),
            "artwork_colour": request.POST.get("artwork_colour"),
            "final_price": 0,
            "order_list": [],
        }

    if order is not None:
        order.append(cus_order.copy())
    else:
        order = []
        order.append(cus_order.copy())
    request.session['order'] = order
    return redirect(redirect_url)


def update_order(request, item_id):
    """ Update quantity of the specified product/ service to the bag """

    quantity = int(request.POST.get('quantity'))
    order = request.session.get('order')
    ref = request.POST.get('order_ref')

    if order:
        for data in order:
            if data['order_ref'] == ref:
                if quantity > 0:
                    data['quantity'] = quantity
                else:
                    order.remove(data)
    request.session['order'] = order
    return redirect(reverse('view_bag'))
