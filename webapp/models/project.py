from django.db import models


class Project(models.Model):
    models.ForeignKey(
        to='webapp.Task',
        verbose_name='Проект',
        related_name='projects',
        on_delete=models.CASCADE
    )
    start_date = models.DateField(verbose_name='Дата начала', null=False, blank=False)
    end_date = models.DateField(verbose_name='Дата окончания', null=True, blank=True)
    title = models.CharField(verbose_name='Название проекта', max_length=100, null=False, blank=False)
    description = models.TextField(verbose_name='Описание', max_length=2500, null=True, blank=True)

    class Meta:
        verbose_name = 'Проект'
        verbose_name_plural = 'Проекты'

    def __str__(self):
        return f"{self.title} - {self.pk}"
