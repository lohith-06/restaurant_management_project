from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(["GET"])
def get_menu(request):
    # Hardcoded menu data (dish name, description, price)
    menu = [
        {"name": "Margherita Pizza", "description": "Classic cheese and tomato pizza.", "price": 8.99},
        {"name": "Pasta Alfredo", "description": "Creamy Alfredo pasta with mushrooms.", "price": 10.49},
        {"name": "Caesar Salad", "description": "Fresh romaine lettuce, croutons & Caesar dressing.", "price": 6.99},
        {"name": "Grilled Chicken", "description": "Tender chicken breast with herbs.", "price": 12.50},
    ]
    return Response(menu)