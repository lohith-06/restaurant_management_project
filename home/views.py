from django.conf import settings
import requests
from django.shortcuts import render

def homepage(request):
    # Call your own API (adjust URL if needed)
    response = requests.get("http://localhost:8000/api/menu/")  
    menu_items = response.json() if response.status_code == 200 else []

    return render(request, "homepage.html", {"menu_items": menu_items})