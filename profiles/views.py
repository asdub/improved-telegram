from django.shortcuts import render, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from checkout.models import Order, Image
from .models import UserProfile
from .forms import UserProfileForm


# User profile view
@login_required
def profile(request):
    """ Display the user's profile. """
    profile = get_object_or_404(UserProfile, user=request.user)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile had been updated.')
        else:
            messages.error(
                request, 'Update failed. Please ensure the form is valid.'
                )
    else:
        form = UserProfileForm(instance=profile)
    orders = profile.orders.all()

    template = 'profiles/profile.html'
    context = {
        'form': form,
        'orders': orders,
        'on_profile_page': True
    }

    return render(request, template, context)


def order_history(request, order_number):
    """ Redirect user to orginal order confirmation from profile view """
    order = get_object_or_404(Order, order_number=order_number)

    messages.info(request, (
        f'This is a past confirmation for order number {order_number}. '
        'A confirmation email was sent on the order date.'
    ))

    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
        'from_profile': True,
    }

    return render(request, template, context)


# View for user/ customer artwork and download
def artwork(request, order_id):
    """ Display Artwork to User. """
    images = Image.objects.filter(order_id=order_id)
    order = Order.objects.get(id=order_id)

    template = 'profiles/artwork.html'
    context = {
        'images': images,
        'order': order,
    }

    return render(request, template, context)
