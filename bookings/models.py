from django.contrib.auth.models import User 
from django.db import models
from treatment_details.models import Treatment

class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    treatment = models.ForeignKey(Treatment, on_delete=models.CASCADE)
    date = models.DateField()
    time_slot = models.TimeField()
    # Admin confirmation of the booking
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user} - {self.treatment} on {self.date} at {self.time_slot}"
