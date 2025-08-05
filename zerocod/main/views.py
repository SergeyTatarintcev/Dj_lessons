# zerocod/main/views.py
from django.shortcuts import render

def index(request):
    return render(request, 'main/index.html', {'caption': 'CapyDjango'})

def new(request):
    return render(request, 'main/new.html')

def about(request):
    return render(request, 'main/about.html')

def contacts(request):
    return render(request, 'main/contacts.html')

def team(request):
    return render(request, 'main/team.html')

def jobs(request):
    return render(request, 'main/jobs.html')

def faq(request):
    return render(request, 'main/faq.html')
