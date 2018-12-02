
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup/', views.signup, name='signup'),
    path('new_recipe/', views.new_recipe, name='new_recipe'),
    path('recipe_list/', views.recipe_list, name='recipe_list'),
    path('<int:pk>/recipe_edit', views.edit_recipe, name='recipe_edit'),
    path('<int:pk>/recipe_delete', views.delete_recipe, name='recipe_delete'),
]
