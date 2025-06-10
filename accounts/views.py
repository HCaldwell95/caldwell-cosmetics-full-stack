from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import Group
from django.shortcuts import render, redirect
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

    profile = request.user.profile

    profile_fields = [
        ('Full Name', f'{request.user.first_name} {request.user.last_name}'),
        ('Phone Number', getattr(profile, 'phone_number', 'Not provided') or "Not provided"),
        ('Address', getattr(profile, 'address', 'Not provided') or "Not provided"),
        ('Age', getattr(profile, 'age', 'Not provided') or "Not provided"),
        ('Hair Colour', getattr(profile, 'hair_colour', 'Not provided') or "Not provided"),
    ]

    return render(request, 'accounts/profile.html', {
        'user': request.user,
        'profile': profile,
        'profile_fields': profile_fields,
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

@login_required
def delete_account(request):
    if request.method == 'POST':
        user = request.user
        user.is_active = False
        user.save()
        logout(request)
        messages.success(request, 'Your account has been deleted.')
        return redirect('home')
    return render(request, 'accounts/delete_account.html')