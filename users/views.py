from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from users.forms import UserRegistrationForm, UserLoginForm, GroupForm
from users.models import Group, User


def user_registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            user = form.instance
            auth.login(request, user)
            return redirect('notes_main:note_creation')
    else:
        form = UserRegistrationForm()
    return render(request, 'users/user_registration.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)
            if user:
                auth.login(request, user)
                return redirect('notes_main:note_creation')
    else:
        form = UserLoginForm()
    return render(request, 'users/user_login.html', {'form': form})


@login_required
def logout(request):
    auth.logout(request)
    return redirect('notes_main:index')


@login_required
def create_group(request):
    if request.method == 'POST':
        form = GroupForm(data=request.POST)
        if form.is_valid():
            group = form.save(commit=False)
            group.creator = request.user
            form.save()
            return redirect('notes_main:group_notes')
    else:
        form = GroupForm()
    return render(request, 'users/group_creation.html', {'form': form})


def all_groups(request):
    return render(request, 'users/user_groups.html')
