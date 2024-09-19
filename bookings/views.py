from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from .forms import BookingForm
from .models import Booking
from .models import Appointment

@login_required
def bookings(request):
    user_bookings = Booking.objects.filter(user=request.user)  # Filter by the logged-in user
    context = {'user_bookings': user_bookings}
    return render(request, 'bookings/bookings.html', context)

@login_required
def book_appointment(request):
    if not request.user.is_authenticated:
        return redirect('signup')
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user  # Link to the logged-in user
            booking.save()
            return redirect('booking_confirmation', booking_id=booking.id)
    else:
        form = BookingForm()
    
    return render(request, 'bookings/book_appointment.html', {'form': form})

@login_required
def booking_events(request):
    bookings = Booking.objects.filter(user=request.user)  # Adjust filter as needed
    events = []
    for booking in bookings:
        events.append({
            'title': str(booking.treatment),  # Display treatment name or any other relevant title
            'start': booking.date.isoformat() + 'T' + str(booking.time_slot)  # Format the date and time
        })
    return JsonResponse(events, safe=False)

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