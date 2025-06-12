from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from treatment_details.models import Treatment


class Appointment(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.start_time.strftime('%d-%m-%Y %H:%M')}"


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)  # Optional soft-delete

    def status(self):
        return "Confirmed" if self.is_confirmed else "Pending"

    def save(self, *args, **kwargs):
        if self.pk:
            # Editing an existing booking: unbook the old appointment if changed
            original = Booking.objects.get(pk=self.pk)
            if original.appointment != self.appointment:
                original.appointment.is_booked = False
                original.appointment.save()

        # Check if the appointment is already booked by another booking
        if self.appointment.is_booked:
            # If new booking or appointment changed, raise error
            if not self.pk or (self.pk and self.appointment != Booking.objects.get(pk=self.pk).appointment):
                raise ValidationError("This appointment slot is already booked.")

        # Mark the current appointment as booked
        self.appointment.is_booked = True
        self.appointment.save()

        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        # Unbook the appointment when deleting the booking
        if self.appointment:
            self.appointment.is_booked = False
            self.appointment.save()
        super().delete(*args, **kwargs)

    def __str__(self):
        return f"{self.user.username} - {self.treatment} at {self.appointment.start_time.strftime('%Y-%m-%d %H:%M')}"
