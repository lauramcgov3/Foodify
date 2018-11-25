from django.urls import path
from . import views

urlpatterns = [
    path('', views.days_list, name='days_list'),
]
