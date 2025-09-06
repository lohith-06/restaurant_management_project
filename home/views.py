# from django.shortcuts import render
# from django.conf import settings

# def home_view(request):
#     context = {
#         'restaurant_name': settings.RESTAURANT_NAME
#     }
#     return render(request, 'home/index.html', context)

# def about_view(request):
#     return render(request, 'home/about.html')# views.py
# from django.shortcuts import render
# from .models import RestaurantLocation

# def home(request):
#     location = RestaurantLocation.objects.first()  # get first saved location
#     return render(request, "home.html", {"location": location})# views.py
# from django.shortcuts import render
# from .models import MenuItem, RestaurantLocation

# def home(request):
#     query = request.GET.get("q")  # search keyword
#     if query:
#         menu_items = MenuItem.objects.filter(name__icontains=query)
#     else:
#         menu_items = MenuItem.objects.all()

#     location = RestaurantLocation.objects.first()

#     return render(
#         request,
#         "home.html",
#         {"menu_items": menu_items, "location": location, "query": query},
# def home_view(request):
#     restaurant = Restaurant.objects.first()  # assuming one restaurant
#     return render(request, "home.html", {"restaurant": restaurant})
from django.shortcuts import render
from django.utils import timezone
from .models import Restaurant
from .utils import get_cart_count

def home_view(request):
    restaurant = Restaurant.objects.first()
    cart_count = get_cart_count(request)
    current_time = timezone.now()
    return render(request, "home.html", {
        "restaurant": restaurant,
        "cart_count": cart_count,
        "current_time": current_time
    })
