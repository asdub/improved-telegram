from django.shortcuts import render, redirect, reverse
from django.contrib import messages

from .forms import OrderForm

# Create your views here.


def checkout(request):
    order = request.session.get('order')
    if not order:
        messages.error(request, "No orders found.")
        return redirect(reverse('products'))

    order_form = OrderForm()
    template = 'checkout/checkout.html'
    context = {
        'order_form': order_form,
        'stripe_public_key': 'pk_test_51JgeIWFQi3WuvSnPBMD2MFkIqrArpb5ZYuZfLfCUDRLyzwCrcUInyoZfo2W3GHWy2QzDzeuZMV0mjM0haBXNorfP0081p248xP',
        'client_secret': 'test client secret',
    }

    return render(request, template, context)
