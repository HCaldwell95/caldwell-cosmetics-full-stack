from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils import timezone
from django.utils.dateparse import parse_date
from .forms import BookingForm
from bookings.models import Booking
from .models import Appointment
from datetime import datetime, timedelta
from django.contrib import messages


@login_required
def bookings_and_create(request):
    user_bookings = Booking.objects.filter(user=request.user)
    now = timezone.now()
    available_appointments = Appointment.objects.filter(start_time__gte=now, is_booked=False).order_by('start_time')

    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.is_confirmed = True
            booking.save()

            appointment = booking.appointment
            appointment.is_booked = True
            appointment.save()

            messages.success(request, 'Booking created successfully!')
            return redirect('bookings_and_create')
    else:
        form = BookingForm()

    context = {
        'user_bookings': user_bookings,
        'form': form,
        'available_appointments': available_appointments,
    }
    return render(request, 'bookings/bookings_and_create.html', context)


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