from django.urls import path
from .views import get_menu

urlpatterns = [
    path("api/menu/", get_menu, name="get_menu"),
]