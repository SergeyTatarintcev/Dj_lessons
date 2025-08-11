from django.contrib import admin
from .models import News_post

@admin.register(News_post)
class NewsPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'pub_date')
    list_filter = ('author', 'pub_date')
    search_fields = ('title', 'short_description', 'text')
    autocomplete_fields = ('author',)
