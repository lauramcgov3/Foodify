from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('createFamily/', views.createFamily, name='createFamily'),
    path('createMember/', views.createMember, name='createMember'),
]