from django.shortcuts import render, get_object_or_404
from .models import Treatment

def treatment_details(request):
    """
    Renders the treatments page displaying all available treatments.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered treatments page template.
    """
    treatments = Treatment.objects.all()  # Fetch all treatments from the database
    return render(request, 'treatments.html', {'treatments': treatments})

def treatment_card_details(request, slug):
    treatment = get_object_or_404(Treatment, slug=slug)
    return render(request, 'treatments_information.html', {'treatment': treatment})