from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Booking, Treatment
from datetime import time, date
from django.core.exceptions import ValidationError

class BookingTestCase(TestCase):
    def setUp(self):
        """
        Set up the test environment by creating a test user, a test treatment, 
        logging in the user, and creating a booking for that user.
        This method runs before each test to ensure a consistent state.
        """
        # Create a test user for booking
        self.user = User.objects.create_user(username='testuser', password='testpass')
        
        # Create a test treatment to use for the booking
        self.treatment = Treatment.objects.create(name='Test Treatment')

        # Log in as the test user to simulate user actions
        self.client.login(username='testuser', password='testpass')

        # Create a booking instance for the test user
        self.booking = Booking.objects.create(
            user=self.user,
            treatment=self.treatment,
            date=date.today(),
            time_slot=time(14, 0),
            is_confirmed=False  # By default, the booking is not confirmed
        )

    def test_booking_creation(self):
        """
        Test if the booking instance is created successfully.
        Verifies that the booking count in the database is 1 after creation.
        """
        booking_count = Booking.objects.count()  # Count all Booking instances
        self.assertEqual(booking_count, 1)  # Ensure there is exactly 1 booking

    def test_booking_page_access(self):
        """
        Test if the 'My Bookings' page can be accessed by logged-in users.
        Verifies that the page returns a status code of 200 and uses the correct template.
        """
        # Get the URL for the 'My Bookings' page and check if it can be accessed
        response = self.client.get(reverse('my_bookings'))
        self.assertEqual(response.status_code, 200)  # Ensure page loads successfully
        self.assertTemplateUsed(response, 'bookings/bookings.html')  # Check template used
    
    def test_booking_display_on_page(self):
        """
        Test if the created booking is displayed on the 'My Bookings' page.
        Verifies that the treatment name and time slot are shown correctly.
        """
        # Load the 'My Bookings' page and check its content
        response = self.client.get(reverse('my_bookings'))
        self.assertContains(response, 'Test Treatment')  # Check treatment name
        self.assertContains(response, '14:00')  # Check time is displayed as 14:00 (24-hour format)
        self.assertContains(response, 'Pending')  # Check if 'Pending' status is shown (unconfirmed)
    
    def test_booking_time_slot_validation(self):
        """
        Test if the system prevents double-booking in the same time slot.
        Attempts to create another booking with the same date and time, 
        and checks if a ValidationError is raised.
        """
        # Try to create another booking with the same time slot and check for validation error
        with self.assertRaisesMessage(ValidationError, "This time slot is already booked."):
            Booking.objects.create(
                user=self.user,  # Same user
                treatment=self.treatment,  # Same treatment
                date=self.booking.date,  # Same date as the first booking
                time_slot=self.booking.time_slot  # Same time slot as the first booking
            )
    
    def test_admin_can_confirm_booking(self):
        """
        Test if an admin or the system can confirm the booking.
        Sets the 'is_confirmed' field to True and verifies the change.
        """
        # Fetch the booking, update its confirmation status, and save it
        booking = Booking.objects.get(id=self.booking.id)
        booking.is_confirmed = True  # Confirm the booking
        booking.save()  # Save the updated booking
        
        # Check if the booking is confirmed
        self.assertTrue(booking.is_confirmed)  # Ensure 'is_confirmed' is True
