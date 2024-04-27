from django.contrib.auth import login, authenticate
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from users.forms import UserRegistrationForm, UserLoginForm
from users.models import User


# Create your views here.

def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
    else:
        form = UserRegistrationForm()
    return render(request, 'users/user_registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            if user is not None:
                login(request, user)
                return redirect('notes_main:note_creation')
            else:
                return render(request, 'users/user_login.html',
                              {'form': form, 'error_message': 'Invalid email or password'})
    else:
        form = UserLoginForm()
    return render(request, 'users/user_login.html', {'form': form})
