from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = [
            'artwork_request',
            'product_size',
            'product_text_content',
            'artwork_colour'
        ]