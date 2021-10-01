from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):

    bag_items = []
    total = 0
    product_count = 0
    bag = request.session.get('bag', {})
    print(f'BAG----->>> {bag}')
    order = request.session.get('order')
    print(f'ORDER----->>> {order}')

    if order is not None:
        for data in order:
            print(data['item_id'])
            print(data['quantity'])

    if order is not None:
        for data in order:
            product = get_object_or_404(Product, pk=data['item_id'])
            total += int(data['quantity']) * product.price
            data['subtotal'] = int(data['quantity']) * product.price
            data['product'] = product

    if total < settings.FREE_DELIVERY_THRESHOLD:
        delivery = total * Decimal(settings.STANDARD_DELIVERY_PERCENTAGE / 100)
        free_delivery_delta = settings.FREE_DELIVERY_THRESHOLD - total
    else:
        delivery = 0
        free_delivery_delta = 0

    grand_total = delivery + total

    context = {
        'order': order,
        'total': total,
        'product_count': product_count,
        'delivery': delivery,
        'free_delivery_delta': free_delivery_delta,
        'free_delivery_threshold': settings.FREE_DELIVERY_THRESHOLD,
        'grand_total': grand_total,
    }
    return context
