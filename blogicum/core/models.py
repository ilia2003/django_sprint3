from django.db import models


class BaseModel(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=256)
    created_at = models.DateTimeField(
        verbose_name='Добавлено',
        auto_now_add=True)
    is_published = models.BooleanField(
        verbose_name='Опубликовано',
        help_text='Снимите галочку, чтобы скрыть публикацию.',
        default=True)

    class Meta:
        abstract = True
