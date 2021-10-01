from django.db import models


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'
  
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


SIZE_CHOICES = (
    ('A0', 'A0'),
    ('A1', 'A1'),
    ('A2', 'A2'),
    ('A3', 'A3'),
    ('A4', 'A4'),
    ('A5', 'A5'),
    ('A6', 'A6'),
)

COLOUR_CHOICES = [('full_colour', 'Full Colour'), ('black_white', 'Black & White')]


class Order(models.Model):
    item_id = models.CharField(max_length=254, null=True, blank=True)
    artwork_request = models.TextField(max_length=1024, null=True, blank=True)
    product_size = models.CharField(max_length=6, choices=SIZE_CHOICES, default='A4')
    product_text_content = models.TextField(max_length=1024, null=True, blank=True)
    artwork_colour = models.CharField(max_length=32, choices=COLOUR_CHOICES, default='full_colour')
    status = models.CharField(max_length=254, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)


def __str__(self):
    return self.item_id
