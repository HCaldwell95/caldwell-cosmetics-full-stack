from django.urls import path
from . import views

urlpatterns = [
    path('', views.treatment_details, name='treatment_details'),
]
