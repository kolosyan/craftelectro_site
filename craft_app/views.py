from django.shortcuts import render
from django.http import HttpResponse

def page_one(request):
    return render(request, 'craft_app/home.html')

def page_two(request):
    return render(request, 'craft_app/about.html')

def page_three(request):
    return render(request, 'craft_app/contact.html')

# Create your views here.
