# Generated by Django 4.1.7 on 2023-03-03 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0003_remove_task_type_task_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='type',
            field=models.ManyToManyField(blank=True, related_name='tasks', to='webapp.type', verbose_name='Тип задачи'),
        ),
    ]