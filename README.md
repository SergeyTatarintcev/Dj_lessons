# CapyDjango — учебный проект на Django

Тестовый сайт с несколькими статичными страницами и модулем новостей. Проект делается в ходе практики: Django + шаблоны (`extends/include`), статика, админка и работа с моделями.

## Что уже сделано

- **Приложение `main`:**
  - Шаблоны: главная, new, about, contacts, team, jobs, faq.
  - Базовый макет `layout.html` + общие фрагменты `nav.html`, `footer.html`.
  - Подключён Bootstrap (CDN) и собственные стили `main/static/main/css/main.css`.
- **Приложение `news`:**
  - Модель `News_post` с полями: `title`, `short_description`, `text`, `pub_date`, `author` (*ForeignKey → User*).
  - Сортировка по дате публикации (новые сверху).
  - Админка: список с колонками **Название / Автор / Дата**, фильтры и поиск.
  - AppConfig с русским именем раздела: **«Новости»** в сайдбаре админки.
  - Шаблон `news/news.html` — вывод новостей из БД «карточками».

## Структура (основное)

```
zerocod/
├─ main/
│  ├─ static/main/css/main.css
│  ├─ static/main/img/...
│  ├─ templates/main/
│  │  ├─ layout.html, nav.html, footer.html
│  │  ├─ index.html, new.html, about.html, contacts.html, team.html, jobs.html, faq.html
│  └─ urls.py, views.py, apps.py
├─ news/
│  ├─ templates/news/news.html
│  ├─ admin.py, models.py, urls.py, views.py, apps.py
├─ zerocod/
│  ├─ settings.py, urls.py, wsgi.py
├─ manage.py
└─ README.md
```

## Установка и запуск

```bash
# 1) Клонирование (пример)
git clone <repo_url>
cd Dj_lessons/zerocod

# 2) Виртуальное окружение
python -m venv .venv
# Активировать окружение:
#  Windows PowerShell
.\.venv\Scripts\activate
#  macOS / Linux
source .venv/bin/activate

# 3) Зависимости (минимум)
pip install django

# 4) Миграции
python manage.py migrate

# 5) Суперпользователь для админки
python manage.py createsuperuser

# 6) Запуск
python manage.py runserver
```

Открой: **http://127.0.0.1:8000/**  
Админка: **http://127.0.0.1:8000/admin/**

> PowerShell tip (ExecutionPolicy):
> ```powershell
> Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
> ```

## Приложение «Новости»

### Модель
```python
from django.db import models
from django.contrib.auth.models import User

class News_post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    short_description = models.CharField(max_length=200, verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Новость')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    author = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True, blank=True,
        verbose_name='Автор',
        related_name='news_posts'
    )

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
```

### Админка
```python
from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ('title', 'short_description', 'text')
    autocomplete_fields = ('author',)
```

### Вьюха и URL
```python
# news/views.py
from django.shortcuts import render
from .models import News_post

def home(request):
    items = News_post.objects.all()
    return render(request, 'news/news.html', {'news': items, 'caption': 'CapyDjango'})
```
```python
# news/urls.py
from django.urls import path
from . import views

app_name = 'news'
urlpatterns = [
    path('', views.home, name='news_home'),
]
```

Подключение в проекте:
```python
# zerocod/urls.py
from django.urls import path, include

urlpatterns = [
    path('', include('main.urls')),
    path('news/', include('news.urls')),
]
```

### Шаблон
```django
{% extends 'main/layout.html' %}
{% block title %}Новостная лента{% endblock %}

{% block content %}
  <h1>Добро пожаловать на сайт {{ caption }}</h1>
  <h2>Читайте новости</h2>

  <style>
    .news-list { display: grid; gap: 16px; }
    .news-card {
      border: 1px solid #e5e7eb; border-radius: 12px; padding: 16px;
      background: #fff; box-shadow: 0 1px 4px rgba(0,0,0,0.05);
    }
    .news-title { margin: 0 0 8px; }
    .news-meta { color:#6b7280; font-size: 0.9rem; margin-bottom: 8px; }
    .news-text { margin: 0; }
  </style>

  {% if news %}
    <div class="news-list">
      {% for n in news %}
        <article class="news-card">
          <h3 class="news-title">{{ n.title }}</h3>
          <div class="news-meta">
            {{ n.pub_date|date:"d.m.Y H:i" }}
            {% if n.author %} • Автор: {{ n.author.username }}{% endif %}
          </div>
          <p class="news-text">{{ n.short_description }}</p>
        </article>
      {% endfor %}
    </div>
  {% else %}
    <p>Пока нет новостей.</p>
  {% endif %}
{% endblock %}
```

## Дальше в планах
- Вынести стили карточек в `static/css/news.css`.
- Детальная страница новости (`/news/<id>/`).
- Форма добавления новости на сайте с автоподстановкой автора.
- Пагинация списка новостей.
