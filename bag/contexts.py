from decimal import Decimal
from django.conf import settings
from django.shortcuts import get_object_or_404
from products.models import Product


def bag_contents(request):
    total = 0
    product_count = 0
    order = request.session.get('order')

    if order is not None:
        for data in order:
            product = get_object_or_404(Product, pk=data['item_id'])
            if data['product_size'] == 'A0':
                data['final_price'] = int(product.price) + 50
                data['order_list'].append('A0 Size artwork, additional €50.00')
            elif data['product_size'] == 'A1':
                data['final_price'] = int(product.price) + 45
            elif data['product_size'] == 'A2':
                data['final_price'] = int(product.price) + 40
            elif data['product_size'] == 'A3':
                data['final_price'] = int(product.price) + 35
            elif data['product_size'] == 'A5':
                data['final_price'] = int(product.price) - 10
            elif data['product_size'] == 'A6':
                data['final_price'] = int(product.price) - 15
            elif data['product_size'] == 'A7':
                data['final_price'] = int(product.price) - 20
            elif data['product_size'] == 'A8':
                data['final_price'] = int(product.price) - 25
            else:
                data['final_price'] = int(product.price)

            if data['artwork_colour'] == 'Full Colour':
                data['final_price'] = int(data['final_price']) + 25
            total += int(data['quantity']) * int(data['final_price'])
            printthis = data['order_list']
            print(f' ORDER--->>> {printthis}')
            data['subtotal'] = int(data['quantity']) * data['final_price']
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
