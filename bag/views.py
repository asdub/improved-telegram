from django.shortcuts import render, redirect
from .forms import OrderForm

# Create your views here.


def view_bag(request):
    """ View to render shopping bag order contents """

    return render(request, 'bag/bag.html')


def order_form(request):
    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()

    context = {
        'form': form
    }
    return render(request, 'bag/product_order.html', context)


def add_to_order(request, item_id):
    """ Add quantity of the specified product/ service to the bag """

    quantity = int(request.POST.get('quantity'))
    redirect_url = request.POST.get('redirect_url')
    bag = request.session.get('bag', {})

    if item_id in list(bag.keys()):
        bag[item_id] += quantity
    else:
        bag[item_id] = quantity

    request.session['bag'] = bag
    return redirect(redirect_url)
