from django.urls import path
from . import views
from .views import booking_events

urlpatterns = [
    path('book/', views.book_appointment, name='book_appointment'),
    path('confirmation/<int:booking_id>/', views.booking_confirmation, name='booking_confirmation'),
    path('booking_events/', views.booking_events, name='booking_events'),
]
