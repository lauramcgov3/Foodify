from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import DaysOfTheWeek


@login_required
def home(request):
    days = DaysOfTheWeek.objects.all().order_by('pk')
    return render(request, 'foodifyapp/home.html', {'days': days})


def loggedout(request):
    return render(request, 'foodify/loggedout.html')