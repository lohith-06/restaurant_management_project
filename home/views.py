# from django.shortcuts import render
# from django.conf import settings

# def home_view(request):
#     context = {
#         'restaurant_name': settings.RESTAURANT_NAME
#     }
#     return render(request, 'home/index.html', context)

# def about_view(request):
#     return render(request, 'home/about.html')# views.py
from django.shortcuts import render
from .models import RestaurantLocation

def home(request):
    location = RestaurantLocation.objects.first()  # get first saved location
    return render(request, "home.html", {"location": location})