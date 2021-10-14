from django.shortcuts import render, redirect, reverse, get_object_or_404
from products.models import Product
from checkout.models import OrderLineItem
from django.utils.html import format_html
from django.contrib import messages

# Create your views here.


def view_bag(request):
    """ View to render shopping bag order contents """

    return render(request, 'bag/bag.html')


def add_to_order(request, item_id):
    """ Add quantity of the specified product/ service to the bag """

    product = Product.objects.get(pk=item_id)
    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order')
    cus_order = {
            "order_ref": item_id + "-" + request.POST.get("quantity"),
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

    for data in order:
        product = get_object_or_404(Product, pk=data['item_id'])
        if data['product_size'] == 'A0':
            data['final_price'] = int(product.price) + 50
            data['order_list'].append(f'+ A0 Size artwork, additional €50.00 ({product.name})')
        elif data['product_size'] == 'A1':
            data['final_price'] = int(product.price) + 45
            data['order_list'].append(f'+ A1 Size artwork, additional €45.00 ({product.name})')
        elif data['product_size'] == 'A2':
            data['final_price'] = int(product.price) + 40
            data['order_list'].append(f'+ A2 Size artwork, additional €40.00 ({product.name})')
        elif data['product_size'] == 'A3':
            data['final_price'] = int(product.price) + 35
            data['order_list'].append(f'+ A3 Size artwork, additional €35.00 ({product.name})')
        elif data['product_size'] == 'A5':
            data['final_price'] = int(product.price) - 10
            data['order_list'].append(f'- A5 Size artwork, €10.00 reduction ({product.name})')
        elif data['product_size'] == 'A6':
            data['final_price'] = int(product.price) - 15
            data['order_list'].append(f'- A6 Size artwork, €15.00 reduction ({product.name})')
        elif data['product_size'] == 'A7':
            data['final_price'] = int(product.price) - 20
            data['order_list'].append(f'- A7 Size artwork, €20.00 reduction ({product.name})')
        elif data['product_size'] == 'A8':
            data['final_price'] = int(product.price) - 25
            data['order_list'].append(f'- A8 Size artwork, €25.00 reduction ({product.name})')
        else:
            data['final_price'] = int(product.price)

        if data['artwork_colour'] == 'Full Colour':
            data['final_price'] = int(data['final_price']) + 25
            data['order_list'].append(f'+ Full Colour, additional €25.00 ({product.name})')
        data['subtotal'] = int(data['quantity']) * data['final_price']

    message = format_html(f'<strong>+ {product.name}</strong> Added to your order.' + '<br><a class="btn" href="{}">View Orders.</a>', reverse('view_bag'))
    messages.error(request, message)
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
