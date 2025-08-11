from django.shortcuts import render
from .models import News_post

def home(request):
    items = News_post.objects.all()
    return render(request, 'news/news.html', {'news': items, 'caption': 'CapyDjango'})
