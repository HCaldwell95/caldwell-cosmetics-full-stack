from django import forms
from .models import Subscriber

# Subscription Newsletter
class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
