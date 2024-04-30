from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


class User(AbstractUser):
    avatar = models.ImageField("Аватар пользователя", upload_to='users/images/')

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Group(models.Model):
    group_name = models.CharField(max_length=100, verbose_name='Название группы', unique=True, null=False)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='group_creation', verbose_name='Создатель',
                                null=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.group_name

    class Meta:
        verbose_name = "Группа"
        verbose_name_plural = "Группы"


def assign_creator_as_admin(sender, instance, created, **kwargs):
    if created:
        UserGroup.objects.create(user=instance.creator, group=instance, role='Administrator')


class UserGroup(models.Model):
    ROLES = (
        ('Member', 'Член группы'),
        ('Administrator', 'Администратор группы'),
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    joined_at = models.DateTimeField(auto_now_add=True)
    role = models.CharField(max_length=100, choices=ROLES, default='member')

    class Meta:
        unique_together = ['user', 'group']

    def get_completion_status_tag_display(self):
        return dict(self.ROLES)[self.role]

    def get_importance_status_tag_display(self):
        return dict(self.ROLES)[self.role]
