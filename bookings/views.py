from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from .forms import BookingForm
from bookings.models import Booking
from .models import Appointment
from datetime import datetime, timedelta

@login_required
def bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)  # Filter by the logged-in user
    context = {'user_bookings': user_bookings}
    return render(request, 'bookings/bookings.html', context)

def create_booking(request):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.is_confirmed = True  # Or False depending on your flow
            booking.save()

            # Mark appointment as booked
            appointment = booking.appointment
            appointment.is_booked = True
            appointment.save()

            # Redirect to confirmation page or somewhere else
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    return render(request, 'bookings/create_booking.html', {'form': form})

@login_required
def booking_events(request):
    user = request.user
    bookings = Booking.objects.select_related('appointment').filter(user=user)
    
    data = []
    for booking in bookings:
        appointment = booking.appointment
        start_datetime = booking.appointment.start_time
        end_datetime = appointment.end_time if appointment.end_time else start_datetime + timedelta(hours=1)

        data.append({
            'title': str(booking.treatment),  # Display treatment name or any other relevant title
            'start': start_datetime.isoformat(),
            'end': end_datetime.isoformat(),
            'color': "#28a745" if booking.is_confirmed else "#ffc107",
        })

    return JsonResponse(data, safe=False)

def events(request):
    appointments = Appointment.objects.all()
    events = [{'title': appt.title, 'start': appt.start_time, 'end': appt.end_time} for appt in appointments]
    return JsonResponse(events, safe=False)

@login_required
def booking_confirmation(request, booking_id):
    try:
        booking = Booking.objects.get(id=booking_id, user=request.user)
    except Booking.DoesNotExist:
        return redirect('error_page')  # Redirect to an error page if booking doesn't exist
    return render(request, 'bookings/booking_confirmation.html', {'booking': booking})