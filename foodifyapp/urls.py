
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^new_recipe/$', views.new_recipe, name='new_recipe'),
    url(r'^recipe_list/$', views.recipe_list, name='recipe_list')
]
