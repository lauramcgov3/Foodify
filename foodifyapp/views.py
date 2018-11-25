from django.shortcuts import render
from .models import DaysOfTheWeek

def home(request):
    days = DaysOfTheWeek.objects.all().order_by('pk')
    return render(request, 'foodifyapp/home.html', {'days':days})