from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.models import Group
from .forms import CustomUserCreationForm, CustomUserForm, UserProfileForm
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

@login_required
def profile_view(request):
    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'profile': request.user.profile,  # If applicable
    })

@login_required
def edit_profile_view(request):
    if request.method == 'POST':
        u_form = CustomUserForm(request.POST, instance=request.user)
        p_form = UserProfileForm(request.POST, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = CustomUserForm(instance=request.user)
        p_form = UserProfileForm(instance=request.user.profile)

    return render(request, 'accounts/edit_profile.html', {
        'u_form': u_form,
        'p_form': p_form
    })