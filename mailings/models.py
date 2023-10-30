from django.db import models

from config import settings

NULLABLE = {'blank': True, 'null': True}


class Client(models.Model):
    """Модель, описывающая клиента"""

    email = models.EmailField(verbose_name='Электронная почта', unique=True)
    name = models.CharField(max_length=150, verbose_name='ФИО')
    comment = models.TextField(verbose_name='Комментарий', **NULLABLE)

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name='Пользователь',
                             **NULLABLE)

    class Meta:
        verbose_name = 'клиент'
        verbose_name_plural = 'клиенты'

    def __str__(self):
        return f'{self.email} - {self.name}'


class Mailings(models.Model):
    """Модель, описывающая настройки рассылки"""
    ...


class Message(models.Model):
    """Модель, описывающая тему и сообщение рассылки"""
    ...


class MailingsLogs(models.Model):
    """Модель, описывающая логи рассылки"""
    ...

