from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, RecipeForm
from .models import Recipe


@login_required
def home(request):
    return render(request, 'foodifyapp/home.html')


@login_required
def new_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        post = form.save(commit=False)
        post.save()
        return redirect('recipe_list')
    else:
        form = RecipeForm()
    return render(request, 'foodifyapp/new_recipe.html', {'form': form})


@login_required
def recipe_list(request):
    if request.method == 'GET':
        recipes = Recipe.objects.values('name', 'servings', 'ingredients', 'method', 'category')
    return render(request, 'foodifyapp/recipe_list.html', {'recipes': recipes})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'foodifyapp/signup.html', {'form': form})

