from django.urls import path
from .views import get_menu
from . import views

urlpatterns = [
    path("api/menu/", get_menu, name="get_menu"),
    path("contact/", views.contact_us, name="contact"),
    path("contact/success/", views.contact_us, name="contact_success"),
]