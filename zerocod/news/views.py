from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import News_post
from .forms import NewsForm

def home(request):
    items = News_post.objects.all()
    return render(request, 'news/news.html', {'news': items, 'caption': 'CapyDjango'})

@login_required
def create_news(request):
    if request.method == 'POST':
        form = NewsForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user  # автор = текущий пользователь
            obj.save()
            return redirect('news:news_home')
    else:
        form = NewsForm()
    return render(request, 'news/add_new_post.html', {'form': form})
