from django.shortcuts import render, redirect

# Create your views here.


def view_bag(request):
    """ View to render shopping bag order contents """

    return render(request, 'bag/bag.html')


def add_to_order(request, item_id):
    """ Add  quantity of the specified product/ service to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    customer_order = None

    if 'artwork_request' in request.POST:
        artwork_request = request.POST['artwork_request']
        product_size = request.POST['product_size']
        product_text_content = request.POST['product_text_content']
        artwork_colour = request.POST['artwork_colour']
        
        customer_order = ({'item_id': item_id})
        customer_order.update({'artwork_request': artwork_request})
        customer_order.update({'product_size': product_size})
        customer_order.update({'product_text_content': product_text_content})
        customer_order.update({'artwork_colour': artwork_colour})

    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    print(customer_order)
    return redirect(redirect_url)
