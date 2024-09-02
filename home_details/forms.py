from django import forms
from .models import Subscriber

class NewsletterSubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscriber
        fields = ['email']
