# CapyDjango

**Тестовый сайт на Django**

## Описание
Проект `CapyDjango` — информационный сайт о капибарах, слонах и бегемотах, созданный с использованием Django и Bootstrap.

## Структура проекта
```
zerocod/
├── main/
│   ├── migrations/
│   ├── static/
│   │   └── main/
│   │       ├── css/
│   │       │   └── main.css
│   │       └── img/
│   │           ├── capy.png
│   │           └── team.jpg
│   ├── templates/
│   │   └── main/
│   │       ├── layout.html
│   │       ├── nav.html
│   │       ├── footer.html
│   │       ├── index.html
│   │       ├── new.html
│   │       ├── about.html
│   │       ├── contacts.html
│   │       ├── team.html
│   │       ├── jobs.html
│   │       └── faq.html
│   ├── views.py
│   ├── urls.py
│   └── apps.py
├── zerocod/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
└── README.md
```

## Установка и запуск

1. Клонировать репозиторий:
   ```bash
   git clone <repo_url>
   cd Dj_lessons/zerocod
   ```

2. Создать и активировать виртуальное окружение:
   ```bash
   python -m venv .venv
   .\.venv\Scripts\activate  # Windows
   source .venv/bin/activate     # macOS/Linux
   ```

3. Установить зависимости:
   ```bash
   pip install django
   ```

4. Применить миграции:
   ```bash
   python manage.py migrate
   ```

5. Запустить сервер разработки:
   ```bash
   python manage.py runserver
   ```

6. Открыть в браузере: `http://127.0.0.1:8000/`

## О проекте

- Используются шаблоны Django с include для меню и футера.
- Bootstrap 5 подключен через CDN для стилизации элементов.
- Статические файлы (`css`, `img`) лежат в `main/static/main/`.
- Шаблоны в `main/templates/main/`.

## Контакты и страницы

- **Главная:** `/`
- **Среда обитания:** `/new/`
- **О нас:** `/about/`
- **Контакты:** `/contacts/`
- **Наша команда:** `/team/`
- **Вакансии:** `/jobs/`
- **Вопрос–Ответ:** `/faq/`

## 👨‍💻 Автор

Сделано [SergeyTatarintcev](https://github.com/SergeyTatarintcev)
