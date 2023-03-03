from django.db import models


class Type(models.Model):
    models.ForeignKey(
        to='webapp.Task',
        verbose_name='Тип задачи',
        related_name='types',
        on_delete=models.RESTRICT
    )
    name = models.CharField(max_length=50, verbose_name='Тип задачи', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Тип'
        verbose_name_plural = 'Типы'
