from django.shortcuts import render
from .models import DaysOfTheWeek

def days_list(request):
    days = DaysOfTheWeek.objects.all().order_by('pk')
    return render(request, 'foodifyapp/days_list.html', {'days':days})