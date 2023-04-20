from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserProfileForm
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm

def home(request):
    return render(request, 'base.html')

def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login_view')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def login_views(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Invalid credentials')
    return render(request, 'login.html')

def logout_views(request):
    logout(request)
    return redirect('home')

def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = UserProfileForm()
    return render(request, 'create_user_profile.html', {'form': form})
