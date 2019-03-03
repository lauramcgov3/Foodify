from django.shortcuts import render, redirect
from .forms import FamilyForm, MemberForm

# Create your views here.


def home(request):
    return render(request, 'app/home.html')


def createFamily(request):

    if request.method == "POST":

        form = FamilyForm(request.POST)
        if form.is_valid():

            

            post = form.save(commit=False)
            post.save()
            return redirect('/createMember')
    else:
        form = FamilyForm()

    return render(request, 'app/signup.html', {'form': form})


def createMember(request):

    if request.method == "POST":
        form = MemberForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('/createMember')
    else:
        form = MemberForm()

    return render(request, 'app/createuser.html', {'form': form})
