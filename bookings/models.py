from django.contrib.auth.models import User
from django.db import models
from treatment_details.models import Treatment

class Appointment(models.Model):
    title = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField(null=True, blank=True)
    is_booked = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.title} - {self.start_time.strftime('%Y-%m-%d %H:%M')}"

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    is_confirmed = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)  # Optional soft-delete

    def status(self):
        return "Confirmed" if self.is_confirmed else "Pending"

    def __str__(self):
        return f"{self.user.username} - {self.treatment} at {self.appointment.start_time.strftime('%Y-%m-%d %H:%M')}"
