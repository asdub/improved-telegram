from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string

from checkout.models import Order, Image
from .models import Product, Category
from .forms import ProductForm
from .forms import CompleteOrderForm


# All products/ services view.
def all_products(request):
    """ View to show products and sorting """

    products = Product.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey == 'lower_name'
                products = products.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            products = products.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            products = products.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "Please check your search term and try again.")
                return redirect(reverse('products'))

            queries = Q(name__icontains=query) | Q(description__icontains=query)
            products = products.filter(queries)

    current_sorting = f'{sort}_{direction}'

    context = {
        'products': products,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'products/products.html', context)


# Products/ Services individual view.
def product_detail(request, product_id):
    """ View to show individual product/ service details """

    product = get_object_or_404(Product, pk=product_id)

    context = {
        'product': product,
    }

    return render(request, 'products/product_detail.html', context)


# Add Products/ Services view via management.
@login_required
def add_product(request):
    """ Add a product to the store & list pending orders """
    orders = Order.objects.filter(order_status="Pending")
    ordered_orders = orders.order_by('-date')

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store administrators can add products.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form_product = ProductForm(request.POST, request.FILES)
        if form_product.is_valid():
            product = form_product.save()
            messages.success(request, 'Successfully added product!')
            return redirect(reverse('product_detail', args=[product.id]))

        else:
            messages.error(
                request, 'Failed to add product.Please ensure the form is valid.')
    else:
        form_product = ProductForm()

    template = 'products/add_product.html'
    context = {
        'form_product': form_product,
        'orders': ordered_orders,
    }

    return render(request, template, context)


# Edit Products/ Services view via management.
@login_required
def edit_product(request, product_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store administrators can edit products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated product!')
            return redirect(reverse('product_detail', args=[product.id]))
        else:
            messages.error(request, 'Failed to update product. Please ensure the form is valid.')
    else:
        form = ProductForm(instance=product)
        messages.info(request, f'You are editing {product.name}')

    template = 'products/edit_product.html'
    context = {
        'form': form,
        'product': product,
    }

    return render(request, template, context)


# Delete Products/ Services view via management.
@login_required
def delete_product(request, product_id):
    """ Delete a product from the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store administrators can delete products.')
        return redirect(reverse('home'))

    product = get_object_or_404(Product, pk=product_id)
    product.delete()
    messages.success(request, 'Product deleted!')
    return redirect(reverse('products'))


# Email User on order status change.
def send_order_confirmation_email(request, orders):
    """Send user email confriming artwork upload"""
    cust_email = orders.email
    subject = render_to_string(
        'checkout/confirmation_emails/order_email_subject.txt',
        {'order': orders})

    context = {'order': orders}
    html_content = render_to_string(
        'checkout/confirmation_emails/order_email_body.html',
        {'order': orders})

    context = {'order': orders, 'contact_email': settings.DEFAULT_FROM_EMAIL}
    plain_text = render_to_string(
        'checkout/confirmation_emails/order_email_body.txt',
        context, request=request)

    send_mail(
        subject,
        plain_text,
        html_content,
        settings.DEFAULT_FROM_EMAIL,
        [cust_email],
        html_message=html_content
    )


# Add Products/ Services view via management.
@login_required
def customer_order(request, order_id):
    """ Add a product to the store """

    if not request.user.is_superuser:
        messages.error(
            request, 'Sorry, only store administrators can add products.'
            )
        return redirect(reverse('home'))

    orders = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        form_update = CompleteOrderForm(
            request.POST, request.FILES, instance=orders
            )
        if form_update.is_valid():
            for img in request.FILES.getlist('image'):
                Image.objects.create(order_id=orders.id, image=img)
            form_update.save()
            orders.order_status = 'Completed'
            orders.save()
            send_order_confirmation_email(request, orders)
            messages.success(
                request, 'Successfully completed order! \
                            Confirmation email sent to Customer'
                )
            return redirect(reverse('add_product'))

        else:
            messages.error(
                request, 'Failed to update order. \
                            Please ensure the form is valid.'
                )
    else:
        form_update = CompleteOrderForm()

    template = 'products/customer_order.html'
    context = {
        'form_update': form_update,
        'order': orders,
    }

    return render(request, template, context)
