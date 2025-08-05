# zerocod/main/urls.py
from django.urls import path
from . import views

app_name = 'main'

urlpatterns = [
    path('',         views.index,    name='home'),
    path('new/',     views.new,      name='page2'),
    path('about/',   views.about,    name='about'),
    path('contacts/',views.contacts, name='contacts'),
    path('team/',    views.team,     name='team'),
    path('jobs/',    views.jobs,     name='jobs'),
    path('faq/',     views.faq,      name='faq'),
]
