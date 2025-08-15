from django import forms
from django.forms import TextInput, DateTimeInput, Textarea
from .models import News_post

class NewsForm(forms.ModelForm):
    class Meta:
        model = News_post
        fields = ('title', 'short_description', 'text', 'date')
        widgets = {
            'title': TextInput(attrs={'class': 'form-control', 'placeholder': 'Название новости'}),
            'short_description': TextInput(attrs={'class': 'form-control', 'placeholder': 'Краткое описание'}),
            'text': Textarea(attrs={'class': 'form-control', 'placeholder': 'Новость'}),
            'date': DateTimeInput(attrs={'class': 'form-control', 'placeholder': 'Дата публикации'}),
        }
