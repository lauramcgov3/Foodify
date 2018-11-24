from django.views.generic import DetailView, ListView, UpdateView, CreateView
from .models import DaysOfTheWeek
from .forms import DaysOfTheWeekForm


class DaysOfTheWeekListView(ListView):
    model = DaysOfTheWeek


class DaysOfTheWeekCreateView(CreateView):
    model = DaysOfTheWeek
    form_class = DaysOfTheWeekForm


class DaysOfTheWeekDetailView(DetailView):
    model = DaysOfTheWeek


class DaysOfTheWeekUpdateView(UpdateView):
    model = DaysOfTheWeek
    form_class = DaysOfTheWeekForm