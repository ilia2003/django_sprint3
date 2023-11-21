from django.db import models
from django.contrib.auth import get_user_model

from core.models import BaseModel


User = get_user_model()


class Category(BaseModel):
    description = models.TextField(
        verbose_name='Описание',)
    slug = models.SlugField(
        verbose_name='Идентификатор',
        help_text=('Идентификатор страницы для URL; разрешены'
                   ' символы латиницы, цифры, дефис и подчёркивание.'),
        unique=True)

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.title


class Location(BaseModel):
    name = models.CharField(verbose_name='Название места', max_length=256)

    class Meta:
        verbose_name = 'местоположение'
        verbose_name_plural = 'Местоположения'

    def __str__(self):
        return self.title


class Post(BaseModel):
    text = models.TextField(verbose_name='Текст', max_length=256)
    pub_date = models.DateTimeField(
        verbose_name='Дата и время публикации',
        help_text='Если установить дату и время'
        ' в будущем — можно делать отложенные публикации.')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Автор публикации',)
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='post_list',
        verbose_name='Категория')
    location = models.ForeignKey(
        Location,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name='Местоположение',)

    class Meta:
        verbose_name = 'публикация'
        verbose_name_plural = 'Публикации'
        ordering = ['-pub_date']

    def __str__(self):
        return self.title
