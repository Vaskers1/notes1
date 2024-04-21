from django.db import models


# Create your models here.

class User(models.Model):
    user_id = models.PositiveIntegerField(primary_key=True)
    nickname = models.CharField(max_length=20, verbose_name='Имя пользователя', unique=True)
    avatar = models.ImageField("Аватар пользователя", upload_to='users/images/')
    email = models.EmailField(max_length=254, verbose_name='Имэйл', unique=True)
    friend_code = models.CharField(max_length=10, null=True, unique=True)

    def __str__(self):
        return self.nickname

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class Group(models.Model):
    group_name = models.CharField(max_length=100, verbose_name='Название группы', unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


class UserGroup(models.Model):
    ROLES = (
        ('member', 'Member'),
        ('administrator', 'Administrator'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, choices=ROLES, default='member')

    class Meta:
        unique_together = ['user', 'group']


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
    note_id = models.PositiveIntegerField(primary_key=True)
    note_title = models.CharField(max_length=150, verbose_name='Название заметки')
    note_text = models.TextField(max_length=9999999, verbose_name='Текст заметки')
    note_creation_date = models.DateTimeField(auto_now_add=True, verbose_name='Дата создания заметки')
    note_refresh_date = models.DateTimeField(auto_now=True, verbose_name='Дата последнего изменения заметки')
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор')
    completion_status_tag = models.CharField(choices=completion_status, verbose_name='Статус завершения', null=True)
    importance_status_tag = models.CharField(choices=importance_status, verbose_name='Важность', blank=True, null=False)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, blank=True, null=True, verbose_name='Группа')

    def __str__(self):
        return self.note_title

    class Meta:
        verbose_name = "Заметка"
        verbose_name_plural = "Заметки"

    def get_completion_status_tag_display(self):
        return dict(self.completion_status)[self.completion_status_tag]

    def get_importance_status_tag_display(self):
        return dict(self.importance_status)[self.importance_status_tag]