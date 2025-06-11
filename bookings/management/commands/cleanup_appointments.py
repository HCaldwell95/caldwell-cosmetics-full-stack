from django.core.management.base import BaseCommand
from bookings.models import Appointment
from django.utils import timezone

class Command(BaseCommand):
    help = "Delete past appointment slots"

    def handle(self, *args, **kwargs):
        deleted_count, _ = Appointment.objects.filter(end_time__lt=timezone.now()).delete()
        self.stdout.write(self.style.SUCCESS(f"Deleted {deleted_count} past appointment(s)."))
