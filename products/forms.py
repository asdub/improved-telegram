from django import forms
from .widgets import CustomClearableFileInput
from .models import Product, Category
from checkout.models import Order, Image


# Form for updating products as superuser
class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image', required=False, widget=CustomClearableFileInput)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control rounded-1'


# Form for completing orders as superuser
class CompleteOrderForm(forms.ModelForm):

    class Meta:
        model = Image
        fields = ['image']

    # Multiple attrs selected to for orders with many items
    image = forms.ImageField(label='', required=True, widget=CustomClearableFileInput(attrs={'multiple': True}))

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control rounded-1'
