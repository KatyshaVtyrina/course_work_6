from django.db import models


NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель, описывающая клиента"""

    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f'{self.email} - {self.name}'


class Newsletter(models.Model):
    """Модель, описывающая настройки рассылки"""
    ...


