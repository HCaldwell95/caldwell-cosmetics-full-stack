from django.shortcuts import render

def treatment_view(request):
    return render(request, 'treatment_details/treatment_details.html')
