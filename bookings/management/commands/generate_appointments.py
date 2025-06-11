from django.core.management.base import BaseCommand
from bookings.models import Appointment
from datetime import datetime, timedelta, time, date


class Command(BaseCommand):
    help = "Generates 1-hour appointment slots for Tuesdays and Wednesdays from 09:30 to 16:30, 4 weeks ahead."

    def handle(self, *args, **kwargs):
        slot_length = timedelta(hours=1)
        open_days = [1, 2]  # Tuesday = 1, Wednesday = 2
        start_time = time(hour=9, minute=30)
        end_time = time(hour=16, minute=30)

        today = date.today()
        days_ahead = 28  # Generate for the next 4 weeks

        new_slots = 0

        for day_offset in range(days_ahead):
            current_date = today + timedelta(days=day_offset)
            if current_date.weekday() in open_days:
                current_slot = datetime.combine(current_date, start_time)
                slot_end_time = datetime.combine(current_date, end_time)

                while current_slot < slot_end_time:
                    slot_end = current_slot + slot_length

                    # Skip if already exists
                    if not Appointment.objects.filter(start_time=current_slot).exists():
                        Appointment.objects.create(
                            start_time=current_slot,
                            end_time=slot_end
                        )
                        new_slots += 1

                    current_slot += slot_length

        self.stdout.write(self.style.SUCCESS(f"✅ Created {new_slots} appointment slots."))
