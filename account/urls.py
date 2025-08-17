from django.urls import path
from .views import *

urlpatterns = [
    path('feedback/', views.feedback_view, name='feedback'),
    path('feedback/thankyou/', views.feedback_thankyou, name='feedback_thankyou'),
]