from django.test import TestCase
from django.core.exceptions import ValidationError
from .models import Subscriber

class SubscriberModelTest(TestCase):
    
    def setUp(self):
        """
        Set up a test subscriber for use in the tests.
        """
        self.subscriber = Subscriber.objects.create(
            email='test@example.com'
        )

    def test_subscriber_creation(self):
        """
        Test that a subscriber can be created and saved to the database.
        """
        # Check if the subscriber exists in the database
        self.assertEqual(Subscriber.objects.count(), 1)
        self.assertEqual(Subscriber.objects.get().email, 'test@example.com')

    def test_subscriber_email_unique(self):
        """
        Test that the email field is unique.
        """
        # Try to create another subscriber with the same email
        with self.assertRaises(ValidationError):
            new_subscriber = Subscriber(
                email='test@example.com'
            )
            new_subscriber.full_clean()  # This will validate the model and raise a ValidationError if email is not unique

    def test_subscriber_email_format(self):
        """
        Test that the email field validates email format.
        """
        invalid_email = Subscriber(
            email='invalid-email'
        )
        with self.assertRaises(ValidationError):
            invalid_email.full_clean()  # This will validate the model and raise a ValidationError if email format is invalid

    def test_subscriber_str_method(self):
        """
        Test the __str__ method of the Subscriber model.
        """
        self.assertEqual(str(self.subscriber), 'test@example.com')
