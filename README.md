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


## Дальше в планах
- Вынести стили карточек в `static/css/news.css`.
- Детальная страница новости (`/news/<id>/`).
- Форма добавления новости на сайте с автоподстановкой автора.
- Пагинация списка новостей.
