from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.conf import settings

def home_view(request):
    context = {
        'restaurant_name': settings.RESTAURANT_NAME
    }
    return render(request, 'home/index.html', context)