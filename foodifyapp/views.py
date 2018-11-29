from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import DaysOfTheWeek
from django.contrib.auth import login, authenticate
from foodifyapp.forms import SignUpForm

@login_required
def home(request):
    days = DaysOfTheWeek.objects.all().order_by('pk')
    return render(request, 'foodifyapp/home.html', {'days': days})



def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'foodifyapp/signup.html', {'form': form})