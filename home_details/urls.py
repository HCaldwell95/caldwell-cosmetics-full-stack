# treatment_details/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_details, name='home_details'),
    # Add other patterns here
]
