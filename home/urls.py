from django.urls import path
from .views import *

urlpatterns = [
    path('', home_view, name='home'),
path("menu/", views.menu_view, name="menu"),   
 path('', views.home_view, name='home'),
    path('faq/', views.faq_view, name='faq'),
    path('about/', views.about_view, name='about'), 
]