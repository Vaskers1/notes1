from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    user_id = models.AutoField(primary_key=True)
    avatar = models.ImageField("Аватар пользователя", upload_to='users/images/')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Group(models.Model):
    group_name = models.CharField(max_length=100, verbose_name='Название группы', unique=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_creation',
                                verbose_name='Создатель', null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"
