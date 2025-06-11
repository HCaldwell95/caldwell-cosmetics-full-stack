from django.urls import path
from . import views
from .views import booking_events, events, booking_confirmation, bookings, create_booking

urlpatterns = [
    path('', bookings, name='my_bookings'),  # Handle /bookings/ URL
    path('book-appointment/', create_booking, name='book_appointment'),
    path('booking_events/', views.booking_events, name='booking_events'),
    path('events/', events, name='events'),
    path('booking-confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
]
