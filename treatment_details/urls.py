from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.treatment_details, name='treatment_details'),
    path('<slug:slug>/', views.treatment_card_details, name='treatment_card_details'),  # Individual treatment page
]
