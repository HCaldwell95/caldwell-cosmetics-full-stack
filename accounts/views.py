from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})
def profile(request):
    if request.method == 'POST':
        u_form = CustomUserCreationForm(request.POST, instance=request.user)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = CustomUserCreationForm(instance=request.user)

    context = {
        'u_form': u_form,
    }
    return render(request, 'accounts/profile.html', context)
