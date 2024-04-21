# Generated by Django 5.0.4 on 2024-04-20 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_main', '0002_alter_notes_completion_status_tag_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='completion_status_tag',
            field=models.CharField(choices=[('Принято в работу', 'in_progress'), ('Завершено', 'completed')], verbose_name='Статус завершения'),
        ),
        migrations.AlterField(
            model_name='notes',
            name='importance_status_tag',
            field=models.CharField(choices=[('Может подождать', 'low'), ('В порядке очереди', 'medium'), ('Требуется немедленное вмешательство', 'high')], verbose_name='Важность'),
        ),
    ]
