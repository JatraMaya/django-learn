from django.shortcuts import render, redirect
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

def register(req):

    if req.method == 'POST':
        form = RegistrationForm(req.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(req, f'Welcome back {username}.')
            return redirect('Login')
    else:
        form = RegistrationForm()
    return render(req, 'users/register.html', {'form': form})

@login_required
def profile(req):
    return render(req, 'users/profile.html')
