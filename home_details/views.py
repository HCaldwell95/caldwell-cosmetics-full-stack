from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string
from django.http import JsonResponse
from .forms import NewsletterSubscriptionForm
from .models import Subscriber

def home_details(request):
    """
    Renders the home page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'home.html')



def subscribe_to_newsletter(request):
    """
    Handles subscription to the newsletter.

    Args:
        request: The HTTP request object, expected to be a POST request with form data.

    Returns:
        JsonResponse: Contains success status and form errors if applicable.
    """
    if request.method == 'POST':
        # Create a form instance with POST data
        form = NewsletterSubscriptionForm(request.POST)

        # Check if the form is valid
        if form.is_valid():
            # Save the subscriber to the database
            subscriber = form.save()
            
            # Prepare email content
            context = {'email': subscriber.email}
            email_content = render_to_string('letter/subscription_thank_you.html', context)
            email_subject = 'Thank you for Subscribing'
            recipient_list = [subscriber.email]
            from_email = settings.EMAIL_HOST_USER

            # Send a thank you email to the subscriber
            send_mail(
                email_subject,
                '',
                from_email,
                recipient_list, 
                html_message=email_content, 
                fail_silently=False
            )

            # Respond to AJAX request if form is not valid
            return JsonResponse({'success': True})
        else:
            # Respond with form errors if form is not valid
            return JsonResponse({'success': False, 'errors': form.errors})

    # Respond with an error if the request method is not POST
    return JsonResponse({'success': False, 'error': 'Invalid request'})
