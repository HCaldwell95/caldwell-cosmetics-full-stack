from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home_details, name='home_details'),
    path('subscribe/', views.subscribe_to_newsletter, name='subscribe_to_newsletter'),
    # Add other URL patterns for home_details here
]