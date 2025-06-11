from django.core.management.base import BaseCommand
from bookings.models import Appointment

class Command(BaseCommand):
    help = "Delete all appointment records from the database"

    def handle(self, *args, **kwargs):
        count, _ = Appointment.objects.all().delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {count} appointment(s) successfully."))
