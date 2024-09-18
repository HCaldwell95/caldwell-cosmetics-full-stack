from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, UserProfileForm
from .models import UserProfile

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            # Assign the user to a default group
            client_group, created = Group.objects.get_or_create(name='Client')
            user.groups.add(client_group)

            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'accounts/signup.html', {'form': form})

def profile(request):
    # Load the user's profile, or create one if it doesn't exist
    profile, created = UserProfile.objects.get_or_create(user=request.user)

    if request.method == 'POST':
        u_form = CustomUserCreationForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, instance=profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = CustomUserCreationForm(instance=request.user)
        p_form = UserProfileForm(instance=profile)

    context = {
        'u_form': u_form,
        'p_form': p_form,
    }

    return render(request, 'accounts/profile.html', context)