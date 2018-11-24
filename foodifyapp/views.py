from django.shortcuts import render

def post_list(request):
    return render(request, 'foodifyapp/days_list.html', {})