from django.db import models


class Task(models.Model):
    summary = models.CharField(max_length=300, null=False, blank=False, verbose_name='Заголовок')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name='Описание')
    status = models.ManyToManyField(
        to='webapp.Status',
        verbose_name='Статус',
        related_name='tasks',
        blank=False,
    )
    type = models.ManyToManyField(
        to='webapp.Type',
        verbose_name='Тип задачи',
        related_name='types',
        blank=False,
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")

    def __str__(self):
        return f"{self.summary} - {self.description} - {self.status} -{self.type}"

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
        ordering = ['created_at']
