from django.contrib import admin
from .models import Recipe, CustomRecipes


admin.site.register(Recipe)
admin.site.register(CustomRecipes)
