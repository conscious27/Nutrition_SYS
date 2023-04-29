from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserProfileForm
from .forms import SignUpForm
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth import get_user_model

# get current user
User = get_user_model()

# if login else open login.html page
@login_required
def home(request):
    user = request.user

    # if user is invalid 
    if not isinstance(user, User):
        return HttpResponseBadRequest('Invalid user')
    
    # if user's profile is valid create new profile button will change into edit profile
    if hasattr(user, 'profile'):
        button_text = 'Edit Profile'
    else:
        button_text = 'Create New Profile'

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST)
        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = request.user
            profile.save()
            return redirect('home')
    else:
        profile_form = UserProfileForm()
    return render(request, 'base.html', {'button_text':button_text, 'profile_form':profile_form})
    # return render(request, 'base.html')

# form for sign up and create an account for user
def signup_views(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.is_active =  True
            user.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# if username and password match authenticate the user
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

@login_required
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            if not user.is_authenticated:
                user = User.objects.create_user(username=request.POST['username'], password=request.POST['password1'])
            profile = form.save(commit=False, user=user)
            profile.user = user
            profile.save()
            return redirect('home')
    else:
        form = UserProfileForm()
    return render(request, 'create_user_profile.html', {'form': form})

@login_required
def edit_user_profile(request):
    user = request.user
    profile = user.profile

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = UserProfileForm(instance=profile)

    return render(request, 'edit_user_profile.html', {'form' : form})