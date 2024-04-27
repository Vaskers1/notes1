from django.contrib.auth.hashers import make_password, check_password
from django.db import models


# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=20, verbose_name='Имя пользователя', unique=True)
    avatar = models.ImageField("Аватар пользователя", upload_to='users/images/')
    email = models.EmailField(max_length=254, verbose_name='Имэйл', unique=True)
    password = models.CharField(verbose_name='Пароль', blank=False, null=False)

    def save(self, *args, **kwargs):
        if self.password:
            self.password = make_password(self.password)  # Хэширование пароля перед сохранением
        super().save(*args, **kwargs)

    def __str__(self):
        return self.nickname

    def check_password(self, raw_password):
        return check_password(raw_password, self.password)

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
