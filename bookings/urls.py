from django.urls import path
from .views import book_appointment, booking_events, events, booking_confirmation, bookings

urlpatterns = [
    path('', bookings, name='my_bookings'),  # Handle /bookings/ URL
    path('book-appointment/', book_appointment, name='book_appointment'),
    path('booking-events/', booking_events, name='booking_events'),
    path('events/', events, name='events'),
    path('booking-confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
]
