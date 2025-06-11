from django.core.management.base import BaseCommand
from bookings.models import Appointment
from django.utils import timezone
from datetime import timedelta, datetime, time

class Command(BaseCommand):
    help = "Create appointment slots for next 4 weeks every Tuesday and Wednesday between 09:30 and 15:30"

    def handle(self, *args, **kwargs):
        # Settings
        days_of_week = [1, 2]  # Tuesday=1, Wednesday=2 (Monday=0)
        slot_start_time = time(9, 30)
        slot_end_time = time(15, 30)
        slot_duration = timedelta(hours=1)

        # Start from tomorrow or today depending on current time
        today = timezone.localdate()
        start_date = today

        # Define how many weeks ahead to generate slots
        weeks_ahead = 8
        end_date = start_date + timedelta(weeks=weeks_ahead)

        current_date = start_date
        created_slots = 0
        while current_date <= end_date:
            if current_date.weekday() in days_of_week:
                # Generate slots within the working hours
                slot_time = datetime.combine(current_date, slot_start_time)
                slot_time = timezone.make_aware(slot_time)
                slot_end_of_day = datetime.combine(current_date, slot_end_time)
                slot_end_of_day = timezone.make_aware(slot_end_of_day)

                while slot_time + slot_duration <= slot_end_of_day:
                    slot_finish = slot_time + slot_duration

                    # Avoid duplicating slots
                    exists = Appointment.objects.filter(start_time=slot_time).exists()
                    if not exists:
                        Appointment.objects.create(
                            title="Available Slot",
                            start_time=slot_time,
                            end_time=slot_finish,
                            is_booked=False
                        )
                        created_slots += 1

                    slot_time += slot_duration
            current_date += timedelta(days=1)

        self.stdout.write(self.style.SUCCESS(f"Created {created_slots} appointment slots."))
