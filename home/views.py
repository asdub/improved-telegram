from django.shortcuts import render
from checkout.models import Image

# Create your views here.


def index(request):
    """ View to render index.html """
    images = Image.objects.all()

    template = 'home/index.html'
    context = {
        'images': images,
    }
    return render(request, template, context)
