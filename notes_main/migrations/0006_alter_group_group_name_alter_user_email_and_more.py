# Generated by Django 5.0.4 on 2024-04-21 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_main', '0005_notes_group_alter_notes_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='group_name',
            field=models.CharField(max_length=100, unique=True, verbose_name='Название группы'),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Имэйл'),
        ),
        migrations.AlterField(
            model_name='user',
            name='nickname',
            field=models.CharField(max_length=20, unique=True, verbose_name='Имя пользователя'),
        ),
    ]
