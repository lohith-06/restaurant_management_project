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
    path('faq/', views.faq_view, name='faq'),
    path('about/', views.about_view, name='about'), 
]