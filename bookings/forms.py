from django import forms
from django.utils import timezone
from .models import Booking, Appointment

class BookingForm(forms.ModelForm):
    appointment = forms.ModelChoiceField(
        queryset=Appointment.objects.none(),  # empty initially
        empty_label="Select a date and time",
        widget=forms.Select(attrs={"class": "form-control"})
    )

    class Meta:
        model = Booking
        fields = ['treatment', 'appointment']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        now = timezone.now()
        # Update queryset to future and unbooked appointments only
        self.fields['appointment'].queryset = Appointment.objects.filter(
            start_time__gte=now,
            is_booked=False
        ).order_by('start_time')
