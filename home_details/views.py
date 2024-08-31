from django.shortcuts import render

def home_details(request):
    return render(request, 'home.html')