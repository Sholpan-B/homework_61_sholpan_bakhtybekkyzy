from django.db import models
from django.utils import timezone

from webapp.managers import TaskManager
from webapp.models.project import Project


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
    project = models.ForeignKey('webapp.Project', related_name='tasks', verbose_name='Проект', null=True, blank=True,
                                on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата и время создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата и время обновления")
    is_deleted = models.BooleanField(verbose_name='Удалено', null=False, default=False)
    deleted_at = models.DateTimeField(verbose_name='Дата удаления', null=True, default=None)

    def __str__(self):
        return f"{self.summary} - {self.description} - {self.status} -{self.type} - {self.project}"

    def delete(self, using=None, keep_parents=False):
        self.is_deleted = True
        self.deleted_at = timezone.now()
        self.save()

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'
