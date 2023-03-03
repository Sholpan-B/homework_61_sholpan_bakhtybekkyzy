from django.db import models


class Status(models.Model):
    models.ForeignKey(
        to='webapp.Status',
        verbose_name='Статус',
        related_name='status',
        on_delete=models.RESTRICT

    )
    name = models.CharField(max_length=50, verbose_name='Cтатус', null=False, blank=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Статус'
        verbose_name_plural = 'Статусы'
