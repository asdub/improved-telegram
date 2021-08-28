from django.shortcuts import render

# Create your views here.


def index(request):
    """ View to render index.html """
    
    return render(request, 'home/index.html')