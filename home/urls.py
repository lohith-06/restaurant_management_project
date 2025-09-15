from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [\
    path("order/confirmation/", views.order_confirmation_view, name="order_confirmation"),
    path("", views.home_view, name="home"),  
    path("login/", auth_views.LoginView.as_view(template_name="login.html"), name="login"),
    path("logout/", auth_views.LogoutView.as_view(next_page="home"), name="logout"),
path("menu/", views.menu_view, name="menu"),   
 path('', views.home_view, name='home'),
    path('faq/', views.faq_view, name='faq'), path('contact/', views.contact_us, name='contact_us'),
    path('about/', views.about_view, name='about'), 
    path('privacy-policy/', views.privacy_policy_view, name='privacy_policy'),path('add-to-cart/<int:item_id>/', views.add_to_cart, name='add_to_cart'),
]