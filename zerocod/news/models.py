from django.db import models

class News_post(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название новости')
    short_description = models.CharField(max_length=200, verbose_name='Краткое описание')
    text = models.TextField(verbose_name='Новость')
    pub_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата публикации')

    class Meta:
        verbose_name = 'Новость'
        verbose_name_plural = 'Новости'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title  # <-- берёт текст из поля "Название новости"
