from django import forms
from checkout.models import Image
from .models import Product, Category
from .widgets import CustomClearableFileInput


class ProductForm(forms.ModelForm):
    """ Form for updating products as superuser """
    class Meta:
        """ Form model and fields selection """
        model = Product
        fields = '__all__'

    image = forms.ImageField(
                label='Image', required=False, widget=CustomClearableFileInput
                )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control rounded-1'


class CompleteOrderForm(forms.ModelForm):
    """ Form for completing orders as superuser """

    class Meta:
        """ Form model and fields selection """
        model = Image
        fields = ['image']

    # Multiple attrs selected for orders with many items
    image = forms.ImageField(
            label='', required=True, widget=CustomClearableFileInput(
                        attrs={'multiple': True}
                        )
                    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control rounded-1'
