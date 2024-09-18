# bookings/forms.py

from django import forms
from .models import Booking
from treatment_details.models import Treatment

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['treatment', 'date', 'time_slot']
        widgets = {
            'date': forms.SelectDateWidget(),  # Calendar date selector
            'time_slot': forms.TimeInput(attrs={'type': 'time'}),  # Time picker
        }
    
    def clean(self):
        cleaned_data = super().clean()
        treatment = cleaned_data.get('treatment')
        date = cleaned_data.get('date')
        time_slot = cleaned_data.get('time_slot')

        if Booking.objects.filter(date=date, time_slot=time_slot, treatment=treatment).exists():
            raise ValidationError('This time slot is not available.')