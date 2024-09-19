from django.contrib.auth.models import User 
from django.db import models
from django.core.exceptions import ValidationError
from treatment_details.models import Treatment

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    # Admin confirmation of the booking
    is_confirmed = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ("can_view_own_booking", "Can view own booking"),
            ("can_edit_own_booking", "Can edit own booking"),
            ("can_delete_own_booking", "Can delete own booking"),
        ]

    def clean(self):
        # Exclude the current booking instance from the query to avoid self-validation
        if Booking.objects.filter(date=self.date, time_slot=self.time_slot).exclude(id=self.id).exists():
            raise ValidationError("This time slot is already booked.")

    def save(self, *args, **kwargs):
        self.clean()  # Run validation before saving
        super().save(*args, **kwargs)

    def status(self):
        return "Confirmed" if self.is_confirmed else "Pending"

    def __str__(self):
        return f"{self.user} - {self.treatment} on {self.date} at {self.time_slot}"

class Appointment(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.title