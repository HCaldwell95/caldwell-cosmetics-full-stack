from django.shortcuts import render

def treatment_details(request):
    """
    Renders the treatments page.

    Args:
        request: The HTTP request object.

    Returns:
        HttpResponse: Rendered home page template.
    """
    return render(request, 'treatments.html')