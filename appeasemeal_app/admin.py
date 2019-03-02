from django.contrib import admin
from .models import Family, FamilyMembers

# Register your models here.

admin.site.register(Family)
admin.site.register(FamilyMembers)
