from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from .forms import SignUpForm, RecipeForm, CustomRecipeForm
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
        recipes = Recipe.objects.values('pk', 'name', 'servings', 'ingredients', 'method', 'category')
        clean_recipes = [recipe for recipe in recipes]

        ingredients = []
        for recipe in clean_recipes:
            for ingredient in recipe['ingredients']:
                if ingredient not in ingredients:
                    ingredients.append(ingredient)

        print(ingredients)

    return render(request, 'foodifyapp/recipe_list.html', {'recipes': clean_recipes})


@login_required
def edit_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    payload = None
    if request.method == "POST":
        if 'master' in request.method:
            payload = update_master_recipe(request, recipe)
        else:
            payload = update_custom_recipe(request, recipe)

    else:
        payload = {'form': RecipeForm(instance=recipe)}
    return render(request, 'foodifyapp/recipe_edit.html', payload)


def update_master_recipe(request, recipe):
    form = RecipeForm(request.POST, instance=recipe)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('recipe_list')


def update_custom_recipe(request, recipe):
    form = CustomRecipeForm(request.POST, instance=recipe)
    if form.is_valid():
        post = form.save(commit=False)
        post.save()
        return redirect('recipe_list')


@login_required
def delete_recipe(request, pk):
    print(pk)
    recipe = get_object_or_404(Recipe, pk=pk)
    print(recipe)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            post = form.save(commit=False)
            post.delete()
            return redirect('recipe_list')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'foodifyapp/recipe_delete.html', {'form': form})


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

