from django import forms
from .models import Booking, Appointment

class BookingForm(forms.ModelForm):
    appointment = forms.ModelChoiceField(
        queryset=Appointment.objects.filter(is_booked=False),
        empty_label="Select a date and time",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Booking
        fields = ['treatment', 'appointment']
