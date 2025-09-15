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
# from django.shortcuts import render
# from django.utils import timezone
# from .models import Restaurant
# from .utils import get_cart_count


# def order_confirmation_view(request):
#     # Generate a simple order number (in real apps, fetch from DB)
#     order_number = random.randint(1000, 9999)
#     return render(request, "order_confirmation.html", {"order_number": order_number})
# def home_view(request):
#     restaurant = Restaurant.objects.first()
#     cart_count = get_cart_count(request)
#     current_time = timezone.now()
#     return render(request, "home.html", {
#         "restaurant": restaurant,
#         "cart_count": cart_count,
#         "current_time": current_time
#     })
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem, RestaurantInfo # assume you already have this model

def contact_us(request): 
    if request.method == 'POST':
        name = request.POST.get('name')
        message = request.POST.get('message')
        Contact.objects.create(name=name, message=message)
        return redirect('thank_you')
    return render(request, 'contact_us.html')
def thank_you(request):
    return render(request, 'thank_you.html')
def add_to_cart(request, item_id):
    item = MenuItem.objects.get(id=item_id)
    cart = request.session.get('cart', {})
    cart[str(item_id)] = cart.get(str(item_id), 0) + 1
    request.session['cart'] = cart
    return redirect('view_cart')

def view_cart(request):
    cart = request.session.get('cart', {})
    items = []
    total = 0

    for item_id, qty in cart.items():
        item = MenuItem.objects.get(id=item_id)
        items.append({
            'item': item,
            'quantity': qty,
            'subtotal': item.price * qty
        })
        total += item.price * qty

    return render(request, 'cart.html', {'items': items, 'total': total})