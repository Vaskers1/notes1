# Generated by Django 5.0.4 on 2024-04-30 13:46

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_alter_group_group_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='creator',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='group_creation', to=settings.AUTH_USER_MODEL, verbose_name='Создатель'),
        ),
    ]