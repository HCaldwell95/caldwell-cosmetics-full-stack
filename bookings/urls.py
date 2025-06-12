from django.urls import path
from .views import bookings_and_create, booking_events, events, booking_confirmation, booking_edit, booking_delete

urlpatterns = [
    path('', bookings_and_create, name='my_bookings'),  # root bookings page
    path('bookings/', bookings_and_create, name='bookings_and_create'),
    path('booking_events/', booking_events, name='booking_events'),
    path('events/', events, name='events'),
    path('booking-confirmation/<int:booking_id>/', booking_confirmation, name='booking_confirmation'),
    path('edit/<int:booking_id>/', booking_edit, name='booking_edit'),
    path('delete/<int:booking_id>/', booking_delete, name='booking_delete'),
]
