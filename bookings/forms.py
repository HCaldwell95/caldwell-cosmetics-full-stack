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
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['treatment'].queryset = Treatment.objects.all()  # Load available treatments
