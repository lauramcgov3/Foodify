from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Recipe, CustomRecipes


CATEGORY_CHOICES = [
    ('breakfast', 'Breakfast'),
    ('lunch', 'Lunch'),
    ('dinner', 'Dinner')
]


class SignUpForm(UserCreationForm):
    password1 = forms.CharField(max_length=32,
                               widget=forms.PasswordInput,
                               required=True,
                               help_text='Must be 8+ characters')
    password2 = forms.CharField(max_length=32,
                               widget=forms.PasswordInput,
                               required=True,
                               help_text='Confirm password')
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class RecipeForm(forms.ModelForm):

    category = forms.CharField(label='Select a category', widget=forms.Select(choices=CATEGORY_CHOICES))

    class Meta:
        model = Recipe
        fields = ('name', 'servings', 'ingredients', 'method', 'category')


class CustomRecipeForm(forms.ModelForm):
    class Meta:
        model = CustomRecipes
        fields = ('name', 'servings', 'ingredients', 'method', 'category', 'user')