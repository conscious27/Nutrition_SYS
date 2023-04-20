from django.shortcuts import render, redirect

# Create your views here.
from .forms import UserProfileForm
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout


def home(request):
    return render(request, 'home.html')
def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/success/')
    else:
        form = UserProfileForm()
    return render(request, 'create_user_profile.html', {'form': form})
