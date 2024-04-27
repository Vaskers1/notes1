from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Notes(models.Model):
    completion_status = (
        ('seen', 'Просмотрено'),
        ('in_progress', 'Принято в работу'),
        ('completed', 'Завершено'),
    )

    importance_status = (
        ('low', 'Может подождать'),
        ('medium', 'В порядке очереди'),
        ('high', 'Требуется немедленное вмешательство'),
    )
    note_id = models.AutoField(primary_key=True)
    note_title = models.CharField(max_length=150, verbose_name='Название заметки')
    note_text = models.TextField(max_length=9999999, verbose_name='Текст заметки')
    note_creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заметки')
    note_refresh_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения заметки')
    completion_status_tag = models.CharField(choices=completion_status, verbose_name='Статус завершения', blank=True, null=True)
    importance_status_tag = models.CharField(choices=importance_status, verbose_name='Важность', blank=True, null=False)

    def __str__(self):
        return self.note_title

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def get_completion_status_tag_display(self):
        return dict(self.completion_status)[self.completion_status_tag]

    def get_importance_status_tag_display(self):
        return dict(self.importance_status)[self.importance_status_tag]