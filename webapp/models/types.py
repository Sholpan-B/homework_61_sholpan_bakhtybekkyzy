from django.db import models


class Type(models.Model):
    name = models.CharField(
        max_length=50,
        null=False,
        blank=False,
        verbose_name='Тип задачи'
    )

    def __str__(self):
        return self.name
