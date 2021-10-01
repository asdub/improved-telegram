from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ View to render shopping bag order contents """

    return render(request, 'bag/bag.html')


def add_to_order(request, item_id):
    """ Add quantity of the specified product/ service to the bag """

    redirect_url = request.POST.get('redirect_url')
    order = request.session.get('order')
    cus_order = {
            "item_id": item_id,
            "quantity": int(request.POST.get("quantity")),
            "artwork_request": request.POST.get("artwork_request"),
            "product_size": request.POST.get("product_size"),
            "product_text_content": request.POST.get("product_text_content"),
            "artwork_colour": request.POST.get("artwork_colour"),
            "final_price": 0,
            "order_list": []
        }

    if order is not None:
        order.append(cus_order.copy())
    else:
        order = []
        order.append(cus_order.copy())

    request.session['order'] = order
    return redirect(redirect_url)
